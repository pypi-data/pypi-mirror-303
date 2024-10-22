# Copyright 2021 The ElasticDL Authors. All rights reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import io
import os
import time
from contextlib import contextmanager
from datetime import timedelta

import numpy
import torch
import torch.distributed as dist
import torch.distributed.distributed_c10d as c10d
from torch.distributed import PrefixStore, TCPStore
from torch.nn.parallel import DistributedDataParallel as DDP

from elasticai_api.common.constants import (
    CommunicationBackend,
    DDPEnv,
    TrainingLoopStatus,
)
from elasticai_api.common.master_client import GlobalMasterClient
from elasticai_api.util.log_utils import default_logger as logger

DEFAULT_SECS_TO_CHECK_RENDEZVOUS = 30
GET_COMM_RANK_RETRY_NUM = 5
RETRY_RANK_INFO_INTERVAL_SECS = 30


class State:
    def __init__(self, ddp_model, optimizer):
        self.model = ddp_model
        self.optimizer = optimizer

    def capture_snapshot(self):
        return {
            "state_dict": self.model.state_dict(),
            "optimizer": self.optimizer.state_dict(),
        }

    def apply_snapshot(self, obj):
        self.model.load_state_dict(obj["state_dict"])
        self.optimizer.load_state_dict(obj["optimizer"])


class RendevousManager(object):
    def __init__(self):
        self._master_client = GlobalMasterClient.MASTER_CLIENT

    # elegant method for processes synchronization,
    # this will be used to replace 'barrier_sync'
    def _store_based_barrier_with_name(
        self, rank, world_size, name, store, timeout
    ):
        STORE_BASED_BARRIER_PREFIX = "store_based_barrier_key"
        store_key = "{}:{}".format(STORE_BASED_BARRIER_PREFIX, name)
        store.add(store_key, 1)
        worker_count = store.add(store_key, 0)
        logger.info(
            "barrier for rank:{} => key:{}, key_count:{},"
            "added to store.".format(rank, store_key, worker_count)
        )

        start = time.time()
        log_time = time.time()
        while worker_count != world_size:
            time.sleep(1)
            worker_count = store.add(store_key, 0)
            if timedelta(seconds=(time.time() - log_time)) > timedelta(
                seconds=10
            ):
                logger.warning(
                    "Waiting in store based barrier to initialize process"
                    "group for rank: {}, key: {} (world_size={}, "
                    "worker_count={}, timeout={})".format(
                        rank, store_key, world_size, worker_count, timeout
                    )
                )
                log_time = time.time()

            if timedelta(seconds=(time.time() - start)) > timeout:
                raise RuntimeError(
                    "Timed out initializing process group in store based"
                    "barrier on rank: {}, for key: {} "
                    "(world_size={}, worker_count={}, timeout={})".format(
                        rank, store_key, world_size, worker_count, timeout
                    )
                )

        logger.info(
            "Rank {}: Completed store-based barrier for key:{} "
            "with {} nodes.".format(rank, store_key, world_size)
        )

    def process_group_helper_sync(self, rdzv_id, rank_id, timeout=60):
        while True:
            sync = self._master_client.barrier_sync(rdzv_id)
            if sync.reset:
                return True
            logger.warning(
                "=> Process_group sync false,"
                "rank:{} timeout remain:{}s.".format(rank_id, timeout)
            )
            time.sleep(1)
            if timeout is not None:
                timeout -= 1
                if timeout <= 0:
                    return False

    def init_default_pg_with_store(
        self,
        backend,
        store,
        rank,
        world_size,
        group_name,
        sync_id,
        timeout=timedelta(seconds=20),
    ):
        if c10d.GroupMember.WORLD is not None:
            raise RuntimeError(
                "trying to initialize the default process group twice!"
            )

        backend = c10d.Backend(backend)
        default_pg = c10d._new_process_group_helper(
            world_size,
            rank,
            [],
            backend,
            store,
            pg_options=None,
            group_name=group_name,
            timeout=timeout,
        )
        c10d._update_default_pg(default_pg)
        c10d._pg_group_ranks[c10d.GroupMember.WORLD] = {
            i: i for i in range(c10d.GroupMember.WORLD.size())
        }
        c10d._backend = c10d._pg_map[c10d.GroupMember.WORLD][0]
        c10d._default_pg_init_method = None

        barrier_sync = self.process_group_helper_sync(sync_id, rank)
        if not barrier_sync:
            logger.error("=> Not all workers rebuild process group!")

    def set_DDP_env(self, rank_response):
        os.environ[DDPEnv.RANK] = str(rank_response.rank_id)
        os.environ[DDPEnv.SIZE] = str(rank_response.world_size)
        os.environ[DDPEnv.LOCAL_RANK] = str(rank_response.local_rank)
        os.environ[DDPEnv.DDP_MASTER_ADDR] = str(rank_response.master_addr)
        os.environ[DDPEnv.DDP_MASTER_PORT] = str(rank_response.master_port)

    def init_DDP_env(self, rank_response):
        self.set_DDP_env(rank_response)
        if torch.cuda.is_available():
            os.environ[DDPEnv.NCCL_BLOCKING_WAIT] = str(1)
            torch.cuda.set_device(rank_response.local_rank)
            logger.info(
                "Use NCCL as backend. This node has {} GPU(s), {} of which"
                " is/are used for training. => rank:{}, local_rank:{}, gpu"
                " type:{}, master_addr:{}, master_port:{}, rdzvid:{}.".format(
                    torch.cuda.device_count(),
                    str(rank_response.local_size),
                    str(rank_response.rank_id),
                    str(rank_response.local_rank),
                    torch.cuda.get_device_name(rank_response.local_rank),
                    str(rank_response.master_addr),
                    str(rank_response.master_port),
                    str(rank_response.rendezvous_id),
                )
            )
        else:
            logger.info(
                "gloo as backend. => "
                "rank:{}, addr:{}, port:{}, rdzvid:{}.".format(
                    str(rank_response.rank_id),
                    str(rank_response.master_addr),
                    str(rank_response.master_port),
                    str(rank_response.rendezvous_id),
                )
            )

    def get_rank_info(self):
        for _ in range(GET_COMM_RANK_RETRY_NUM):
            rank_response = self._master_client.get_comm_rank()
            if rank_response.rank_id < 0:
                logger.warning(
                    "=> rank_id < 0, can't get rank_info, sleep and retry."
                )
                time.sleep(RETRY_RANK_INFO_INTERVAL_SECS)
            else:
                break
        if rank_response.rank_id < 0:
            raise ValueError("Can't get rank information from EDL master.")
        else:
            return rank_response

    def get_need_init(self, local_rdzv):
        rank_response = self.get_rank_info()
        if str(rank_response.rendezvous_id) != str(local_rdzv):
            return True, rank_response
        else:
            return False, rank_response

    def reset_sync(self, rdzv_id, rank_id, timeout=90):
        while True:
            sync = self._master_client.reset_sync(rdzv_id)
            if sync.reset:
                return True
            logger.warning(
                "=> Sync false, rank:{} timeout remain:{}s.".format(
                    rank_id, timeout
                )
            )
            time.sleep(1)
            if timeout is not None:
                timeout -= 1
                if timeout <= 0:
                    return False

    def notify_training_loop_status(self, status):
        self._master_client.report_training_loop_status(status)


class DDPController(object):
    """
    DDPController provides two main APIs 'elastic_DDP' and 'train_one_batch'
    for user to apply elastic DDP training.
    In detail, there are three problems remain to be explained:
        a. how to init process group;
        b. change membership while add/remove workers or pods;
        c. broadcast model and optimizer states to other workers.

    a. init process group(pg)
    PyTorch recommends 2 main ways to initialize a process group:
    https://pytorch.org/docs/master/distributed.html#initialization

    In DDPController, we build a pg with specifing store, rank, and world_size.
    'init_default_pg_with_store' creates default_pg while the TCPStore is built
    at worker0.

    b. change membership
        1. add new worker: 'init_process_group_if_needed' compares 'local_rdzv'
    with 'rank_response.rendezvous_id' periodically, and rebuild pg when
    they are not equal. '_reset_sync_and_init_DDP' destroy pg before build
    new default pg with 'init_default_pg_with_store'.

        2. pod killed/worker failed: wrap forward/backward with
    'train_one_batch'. If pod killed/worker failed, gradient all-reduce will
    raises exception (process_group timeout or NCCL exception). DDPController
    catchs exception in training loop and calls '_reset_sync_and_init_DDP'
    to reinit pg.

    c. broadcast states
        init process group -> warp DDP(model) -> sync_states
    'sync_states' broadcasts state with class 'State'. 'state.capture_snapshot'
    captures states on worker with rank0, and 'dist.broadcast' broadcasts the
    tensor to the whole group.


    Example::

        >>> if __name__ == "__main__":
        >>>     ...
        >>>     model = ...
        >>>     train_loader = ...
        >>>     DDP_controller = DDPController()

        >>>     with DDP_controller.scope():
        >>>         for batch_idx, (data, target) in enumerate(train_loader):
        >>>             ...
        >>>             DDP_controller.elastic_DDP(
        >>>                     model, wrap_optimizer)
        >>>             # return -1 if exception
        >>>             ans = DDP_controller.train_one_batch(
        >>>                 one_batch,
        >>>                 DDP_controller._model,
        >>>                 DDP_controller._optimizer,
        >>>                 data,
        >>>                 target)
        >>>             ...
        >>> # define forward/backward
        >>> def one_batch(model, optimizer, data, target):
        >>>     optimizer.zero_grad()
        >>>     output = model(data)
        >>>     loss = F.nll_loss(output, target)
        >>>     loss.backward()
        >>>     optimizer.step()
        >>>     # Return any object you want
        >>>     return loss
    """

    def __init__(self, data_shard_service):
        self._first_call = True
        self._allreduce_success = True
        self._is_last_rank0 = False
        self._reinit_grocess_group = False
        self._periodic_check_reinit = False

        self.base_store = None
        self.store = None
        self.model = None
        self.optimizer = None

        self._rendezvous_manager = RendevousManager()
        self.data_shard_service = data_shard_service

        self._local_rank = 0
        self._world_size = 0
        self._rank = 0
        self._local_size = 0
        self._local_rdzv = -1
        self._last_init_time = 0
        self.global_completed_batch_num = 0
        self.batch_count_per_epoch = (
            self.data_shard_service.get_minibatch_count_per_epoch()
        )

    def _update_global_completed_batch_num(self):
        self.global_completed_batch_num += torch.distributed.get_world_size()

    def train_one_batch(self, func, *args, **kwargs):
        """
        Wrap the user-defined training process.
        Args:
            func : function defines the forward/backward
            *args/**kwargs : parameters and data for func
        """
        try:
            result = func(*args, **kwargs)
            self._allreduce_success = True
            self.data_shard_service.report_batch_done()
            self._update_global_completed_batch_num()
        except Exception as e:
            logger.info(
                "---Rank {} catch a Exception when training:{}---".format(
                    self.get_rank(), e
                )
            )
            self._allreduce_success = False
            if self.optimizer:
                self.optimizer.zero_grad()
            result = -1
        finally:
            self._reinit_grocess_group = False
            return result

    def _place_model_to_device(self, model, device):
        """
        Move the model to the device after each init DDP.
        """
        if not device:
            return model
        else:
            model.to(device)
            return model

    def _wrap_optimizer(self, func, *args, **kwargs):
        """
        get ddp_model from wrap_model() and make
        optimizer with ddp_model.parameters().
        Args:
            func : function defines the optimizer
            *args : Usually set as a parameter of the DDP_model
        """
        self.optimizer = func(*args, **kwargs)

    def elastic_DDP(self, model, func_def_optimizer):
        """
        Move model to device and Init the DDP model. When reinit the network,
        you only need to load the model on rank0.
        torch.nn.parallel.distributed._sync_params_and_buffers is responsible
        for synchronizing the model state to other workers.
        Args:
            module (Module): module to be parallelized
            func_def_optimizer (function): define the optimizer
        """
        self.init_process_group_if_needed()

        local_rank = self.get_local_rank()
        device = torch.device("cuda:" + str(local_rank))

        # load 模型要在DDP包裹模型之前 且只需要在rank0上加载就行了
        # _sync_params_and_buffers 会自动同步model parmater
        if (
            self._first_call
            or self._periodic_check_reinit
            or not self._allreduce_success
        ):
            self._reinit_grocess_group = True
            model_on_device = self._place_model_to_device(model, device)
            try:
                ddp_model = DDP(
                    model_on_device,
                    device_ids=[local_rank],
                    output_device=local_rank,
                )
            except Exception as e:
                raise Exception(
                    "torch.nn.parallel.DistributedDataParallel raised an "
                    "Exception: {}".format(e)
                )
            else:
                self._wrap_optimizer(func_def_optimizer, ddp_model)
                # first round don't need to broadcast states
                if self._local_rdzv == 1:
                    self.set_model(ddp_model)
                else:
                    states = self.sync_states(
                        ddp_model, self.optimizer, local_rank
                    )
                    self.set_model(states.model)
                    self.set_optimizer(states.optimizer)

                self.model.train()
                if self._first_call:
                    self._first_call = False
                if not self._allreduce_success:
                    self._allreduce_success = True
                if self._periodic_check_reinit:
                    self._periodic_check_reinit = False

    def destroy_pg(self):
        if dist.is_initialized():
            rank = dist.get_rank()
            dist.destroy_process_group()
            logger.info(
                "=> rank:{}, after destroy_pg, pg is initialized:{}".format(
                    rank, dist.is_initialized()
                )
            )

    def set_store(self, rank_response, timeout=timedelta(seconds=30)):
        """
        TCPStore is something like etcd to store information.
        A single store can be reused by multiple groups with 'PrefixStr'.
        DDPController creates TCPStore when store is 'None' or rank0
        worker failed.
        """
        rank = rank_response.rank_id

        PrefixStr = "/worker/attempt_{}".format(rank_response.rendezvous_id)
        if not (rank == 0 and self._is_last_rank0):
            # rank0 changes only when last worker-0 is killed,
            # no need to set '_is_last_rank0' false
            if rank == 0:
                self._is_last_rank0 = True
            hostname = os.environ.get(DDPEnv.DDP_MASTER_ADDR, None)
            port = int(os.environ.get(DDPEnv.DDP_MASTER_PORT, None))
            if not hostname or not port:
                logger.error("=> Please set hostname and port!")

            start_daemon = rank == 0
            base_store = TCPStore(
                hostname,
                port,
                -1,
                start_daemon,
                timeout,
            )
            store = PrefixStore(PrefixStr, base_store)
            store = PrefixStore("default_pg", store)
            self.store = store
            self.base_store = base_store
        else:
            store = PrefixStore(PrefixStr, self.base_store)
            store = PrefixStore("default_pg", store)
            self.store = store

    def _reset_sync_and_init_DDP(self):
        logger.info("=> begin reset_sync_and_init_DDP")
        # 因为上一次训练中 pod killed 后需要留时间 master callback func 执行
        time.sleep(5)
        need_init, rank_response = self._rendezvous_manager.get_need_init(
            self._local_rdzv
        )
        logger.info(
            "=> last allreduce_success:{}, need_init:{}, "
            "rank_response:\nrank: {}\nworld_size: {}\n"
            "rendezvous_id: {}\nlocal_rank: {}\n"
            "local_size: {}\nmaster_port: {}\n"
            "master_addr: {}\n".format(
                self._allreduce_success,
                need_init,
                rank_response.rank_id,
                rank_response.world_size,
                rank_response.rendezvous_id,
                rank_response.local_rank,
                rank_response.local_size,
                rank_response.master_port,
                rank_response.master_addr,
            )
        )

        self.destroy_pg()
        # reset_sync 保证 all workers 已经重置 process_group
        ans = self._rendezvous_manager.reset_sync(
            rank_response.rendezvous_id, rank_response.rank_id
        )
        if ans:
            if torch.cuda.is_available():
                backend = CommunicationBackend.NCCL
            else:
                backend = CommunicationBackend.GLOO
            self._local_rdzv = rank_response.rendezvous_id
            self._local_rank = rank_response.local_rank
            self._world_size = rank_response.world_size
            self._rank = rank_response.rank_id
            self._local_size = rank_response.local_size

            self._rendezvous_manager.init_DDP_env(rank_response)
            self.set_store(rank_response, timeout=timedelta(seconds=30))
            self._rendezvous_manager.init_default_pg_with_store(
                backend,
                store=self.store,
                rank=rank_response.rank_id,
                world_size=rank_response.world_size,
                group_name=str(rank_response.rendezvous_id),
                sync_id=int(rank_response.rendezvous_id),
                timeout=timedelta(seconds=30),
            )

            self._last_init_time = time.time()
            try:
                self._broadcast_global_completed_batch_num()
            except RuntimeError as e:
                logger.error(
                    "Rank {} raise RunimeError: {}".format(self._rank, e)
                )
                raise e
        else:
            raise RuntimeError(
                "=> reset_sync failed! rank: {}, rendezvous_id:{} ".format(
                    rank_response.rank_id, rank_response.rendezvous_id
                )
            )

    def _broadcast_global_completed_batch_num(self):
        objects = [self.global_completed_batch_num]
        torch.distributed.broadcast_object_list(objects, src=0)
        self.global_completed_batch_num = int(objects[0])

    def init_process_group_if_needed(self):
        """
        This function checks whether the training network needs to
        init/reinit. If so, call '_reset_sync_and_init_DDP'.
        Init process group is required in three cases:
            - during the first operation,
            - the training raise exception,
            - the new workers are added.
        """
        if self._first_call or not self._allreduce_success:
            self._reset_sync_and_init_DDP()
        else:
            cur_time = time.time()
            if (
                cur_time - self._last_init_time
                > DEFAULT_SECS_TO_CHECK_RENDEZVOUS
            ):
                self._last_init_time = time.time()
                (
                    need_init,
                    rank_response,
                ) = self._rendezvous_manager.get_need_init(self._local_rdzv)
                logger.info(
                    "=> rank:{} check periodically-->\n"
                    "last allreduce_success:{}, need_init:{}, "
                    "rank_response:\n -> {}".format(
                        self.get_rank(),
                        self._allreduce_success,
                        need_init,
                        rank_response,
                    )
                )
                # 周期检查时发现新的 worker
                if need_init:
                    logger.info(
                        "Rank {} found new worker(s)".format(self.get_rank())
                    )
                    self._reset_sync_and_init_DDP()
                    self._periodic_check_reinit = True
                    logger.info(
                        "=> Reinit successfully after checking periodically."
                    )

    def set_model(self, model):
        self.model = model

    def set_optimizer(self, optimizer):
        self.optimizer = optimizer

    def is_process_group_reinit(self):
        return self._reinit_grocess_group

    def get_current_epoch(self):
        return self.global_completed_batch_num // self.batch_count_per_epoch

    def get_local_rank(self):
        return int(self._local_rank)

    def get_world_size(self):
        return int(self._world_size)

    def get_rank(self):
        return int(self._rank)

    def get_local_size(self):
        return int(self._local_size)

    def _notify_train_loop_start(self):
        self._rendezvous_manager.notify_training_loop_status(
            TrainingLoopStatus.START
        )

    def _notify_train_loop_end(self):
        logger.info("-----train_loop_end-----")
        self._rendezvous_manager.notify_training_loop_status(
            TrainingLoopStatus.END
        )

    @contextmanager
    def scope(self):
        self._notify_train_loop_start()
        yield
        self._notify_train_loop_end()

    def sync_states(self, model, optimizer, local_rank):
        state = State(model, optimizer)
        pg = c10d._get_default_group()
        if not pg:
            raise Exception("default_group doesn't exist")
        else:
            rank = int(os.environ.get(DDPEnv.RANK, None))
            # 内存中读写bytes
            with io.BytesIO() as f:
                torch.save(state.capture_snapshot(), f)
                raw_blob = numpy.frombuffer(f.getvalue(), dtype=numpy.uint8)

            blob_len = torch.tensor(len(raw_blob)).to(local_rank)
            dist.broadcast(blob_len, src=0, group=pg)
            logger.info("=> status broadcast size is: {}".format(blob_len))

            if rank != 0:
                blob = torch.zeros(blob_len.item(), dtype=torch.uint8).to(
                    local_rank
                )
            else:
                blob = torch.as_tensor(raw_blob, dtype=torch.uint8).to(
                    local_rank
                )

            dist.broadcast(blob, src=0, group=pg)
            logger.info("=> done broadcasting states.")

            if rank != 0:
                with io.BytesIO(blob.cpu().numpy()) as f:
                    local_rank_str = os.environ.get(DDPEnv.LOCAL_RANK, None)
                    if local_rank_str is not None:
                        local_rank = int(local_rank_str)
                        device = torch.device("cuda:{}".format(local_rank))
                        snapshot = torch.load(f, map_location=device)
                    else:
                        logger.info("Load model states to default deivce.")
                        snapshot = torch.load(f)
                state.apply_snapshot(snapshot)

            # wait till everyone has loaded the checkpoint
            dist.barrier(group=pg)

        logger.info("=> done restore from previous states.")
        return state
