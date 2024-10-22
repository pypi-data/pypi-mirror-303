# Copyright 2020 The EasyDL Authors. All rights reserved.
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

import os
import random
import socket
import time
from contextlib import closing

from google.protobuf import empty_pb2

from easydl.proto import easydl_pb2
from elasticai_api.common.constants import PodEnv
from elasticai_api.proto import elasticai_api_pb2, elasticai_api_pb2_grpc
from elasticai_api.util.grpc_utils import Message, ReaderProfile, build_channel
from elasticai_api.util.log_utils import default_logger as logger


def retry_grpc_request(func):
    def wrapper(self, *args, **kwargs):
        retry = kwargs.get("retry", 10)
        execption = None
        for i in range(retry):
            try:
                return func(self, *args, **kwargs)
            except Exception as e:
                logger.warning(
                    "Retry %s to %s.%s with failure",
                    i,
                    self.__class__.__name__,
                    func.__name__,
                )
                execption = e
                time.sleep(15)
        if execption:
            raise execption

    return wrapper


class MasterClient(object):
    """MasterClient provides some APIs connect with the master
    service via gRPC call.

    Usage:
        channel = elasticai_api.util.grpc_utils.build_channel(
            "localhost:50001"
        )
        mc = MasterClient(channel, work_id=0)
        # get task unit from master service
        mc.get_task(...)
    """

    def __init__(self, master_addr, worker_id, worker_type):
        """Initialize a master client.
        Args:
            master_addr: the master address

            worker_id: int
            the unique and ordered worker ID assigned
            by elasticdl command-line.
        """
        self._master_addr = master_addr
        self._channel = build_channel(master_addr)
        self._stub = elasticai_api_pb2_grpc.MasterStub(self._channel)
        self._worker_id = worker_id
        self._worker_type = worker_type
        self._worker_host = os.getenv("MY_POD_IP", "localhost")
        self._worker_local_process_id = int(os.getenv("LOCAL_RANK", 0))
        self._ddp_server_port = self.find_free_port()

    def __del__(self):
        self._channel.close()

    def close_channel(self):
        logger.info("EasyDL master client closes the GRPC channel!!!")
        self._channel.close()

    def open_channel(self):
        logger.info("EasyDL master client opens the GRPC channel!!!")
        self._channel = build_channel(self._master_addr)
        self._stub = elasticai_api_pb2_grpc.MasterStub(self._channel)

    def find_free_port(self):
        with closing(
            socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.bind(("localhost", 0))
            _, port = sock.getsockname()
            return port

    @retry_grpc_request
    def reset_dataset(self, dataset_name):
        """Reset a dataset

        Args:
            dataset_name: name of the dataset, must not be None.
        """
        if dataset_name:
            req = elasticai_api_pb2.ResetDatasetRequest()
            req.dataset_name = dataset_name
            self._stub.reset_dataset(req)

    def get_task(self, task_type=None):
        """Get a task from master.

        Args:
            task_type: elasticdl_pb.TaskType
            the training phase, c.f. /elasticai_api/proto/elasticai_api.proto

        Returns:
            the task unit assigned by master,
            c.f. /elasticai_api/proto/elasticai_api.proto
        """
        req = elasticai_api_pb2.GetTaskRequest()
        req.worker_id = self._worker_id
        if task_type is not None:
            req.task_type = task_type

        success = False
        try:
            res = self._stub.get_task(req)
            success = True
        except Exception:
            # the master node would stop the gRPC service if no more tasks.
            # And this will result a gRPC call exception.
            res = elasticai_api_pb2.Task()
        return success, res

    def get_dataset_task(self, dataset_name):
        """Get a task from master.

        Args:
            dataset_name: string
            the training phase, c.f. /elasticai_api/proto/elasticai_api.proto

        Returns:
            the task unit assigned by master,
            c.f. /elasticai_api/proto/elasticai_api.proto
        """

        req = elasticai_api_pb2.GetDatasetTaskRequest()
        req.worker_id = self._worker_id
        req.dataset_name = dataset_name
        req.worker_type = self._worker_type

        success = False
        res = None
        for _ in range(10):
            try:
                res = self._stub.get_dataset_task(req)
                success = True
                break
            except Exception as e:
                logger.warning(e)
                time.sleep(15)
        if not res:
            res = elasticai_api_pb2.Task()
        return success, res

    @retry_grpc_request
    def report_task_result(
        self, task_id, err_msg, dataset_name=None, exec_counters=None
    ):
        """Report task result to master.

        Args:
          task_id: int
          the task ID assigned by master

          err_msg: string
          the error message on training.

          exec_counters: dict
          statistics of the task being executed.
        """
        if dataset_name:
            request = elasticai_api_pb2.ReportDatasetTaskResultRequest()
            request.dataset_name = dataset_name
        else:
            request = elasticai_api_pb2.ReportTaskResultRequest()
        request.task_id = task_id

        request.err_message = err_msg
        if isinstance(exec_counters, dict):
            request.exec_counters.update(exec_counters)
        if dataset_name:
            return self._stub.report_dataset_task_result(request)
        else:
            return self._stub.report_task_result(request)

    @retry_grpc_request
    def reset_sync(self, rendezvous_id):
        req = elasticai_api_pb2.DdpResetSyncRequest()
        req.rendezvous_id = rendezvous_id
        req.worker_host = self._worker_host
        req.worker_local_process_id = self._worker_local_process_id
        return self._stub.reset_sync(req)

    @retry_grpc_request
    def barrier_sync(self, rendezvous_id):
        req = elasticai_api_pb2.DdpInitSyncRequest()
        req.rendezvous_id = rendezvous_id
        req.worker_host = self._worker_host
        req.worker_local_process_id = self._worker_local_process_id
        return self._stub.barrier_sync(req)

    @retry_grpc_request
    def get_comm_rank(self):
        req = elasticai_api_pb2.GetCommRankRequest()
        req.worker_host = self._worker_host
        req.worker_local_process_id = self._worker_local_process_id
        return self._stub.get_comm_rank(req)

    @retry_grpc_request
    def report_training_loop_status(self, status):
        req = elasticai_api_pb2.ReportTrainingLoopStatusRequest()
        req.worker_host = self._worker_host
        req.worker_local_process_id = self._worker_local_process_id
        req.status = status
        req.ddp_server_port = self._ddp_server_port
        return self._stub.report_training_loop_status(req)

    @retry_grpc_request
    def report_training_params(
        self,
        batch_size,
        num_epochs=None,
        dataset_size=None,
        shuffle=False,
        shuffle_shards=False,
        num_minibatches_per_shard=0,
        dataset_name=None,
        task_type=elasticai_api_pb2.NONE,
        remainder=None,
    ):
        request = elasticai_api_pb2.ReportDatasetShardParamsRequest()
        request.batch_size = batch_size
        request.shuffle = shuffle
        request.shuffle_shards = shuffle_shards
        request.task_type = task_type
        request.dataset_name = dataset_name
        if num_epochs is not None:
            request.num_epochs = num_epochs
        if dataset_size is not None:
            request.dataset_size = dataset_size
        if remainder is not None:
            request.remainder = remainder
        request.num_minibatches_per_shard = num_minibatches_per_shard
        return self._stub.report_dataset_shard_params(request)

    @retry_grpc_request
    def query_relaunch_ps_pod(self):
        request = empty_pb2.Empty()
        return self._stub.query_relaunch_ps_pod(request)

    @retry_grpc_request
    def ready_for_ps_relaunch(self):
        request = empty_pb2.Empty()
        self._stub.ready_for_ps_relaunch(request)

    @retry_grpc_request
    def get_shard_checkpoint(self, dataset_name):
        request = elasticai_api_pb2.GetShardCheckpointRequest()
        request.dataset_name = dataset_name if dataset_name else ""
        return self._stub.get_shard_checkpoint(request)

    @retry_grpc_request
    def report_shard_checkpoint(self, shard_checkpoint):
        request = elasticai_api_pb2.ShardCheckpoint()
        request.content = shard_checkpoint
        return self._stub.report_shard_checkpoint(request)

    @retry_grpc_request
    def worker_sync(self, sync_name):
        request = elasticai_api_pb2.WorkerSyncRequest()
        request.sync_name = sync_name
        request.worker_id = self._worker_id
        return self._stub.worker_sync(request)

    @retry_grpc_request
    def wait_worker_sync(self, sync_name, notify):
        request = elasticai_api_pb2.WaitWorkerSyncRequest()
        request.sync_name = sync_name
        request.notify = notify
        return self._stub.wait_worker_sync(request)

    @retry_grpc_request
    def delete_worker_sync(self, sync_name):
        request = elasticai_api_pb2.DeleteWorkerSyncRequest()
        request.sync_name = sync_name
        request.delete_all = False
        return self._stub.delete_worker_sync(request)

    @retry_grpc_request
    def delete_all_worker_sync(self):
        request = elasticai_api_pb2.DeleteWorkerSyncRequest()
        request.delete_all = True
        return self._stub.delete_worker_sync(request)

    @retry_grpc_request
    def report_used_resource(self, memory, cpu):
        request = elasticai_api_pb2.ReportUsedResourceRequest()
        request.memory = memory
        request.cpu = cpu
        request.worker_id = self._worker_id
        request.worker_type = self._worker_type
        return self._stub.report_used_resource(request)

    @retry_grpc_request
    def get_dataset_epoch(self, dataset_name):
        request = elasticai_api_pb2.GetDatasetEpochRequest()
        request.dataset_name = dataset_name if dataset_name else ""
        return self._stub.get_dataset_epoch(request)

    @retry_grpc_request
    def report_model_metric(self, tensor_stats, op_stats):
        metric_msg = elasticai_api_pb2.ModelMetric()
        tensor_msg = metric_msg.tensor_stats
        tensor_msg.variable_count = tensor_stats.variable_count
        tensor_msg.total_variable_size = tensor_stats.total_variable_size
        tensor_msg.max_variable_size = tensor_stats.max_variable_size
        tensor_msg.tensor_alloc_bytes.update(tensor_stats.tensor_alloc_bytes)
        tensor_msg.kv_embedding_dims.extend(tensor_stats.kv_embedding_dims)

        op_msg = metric_msg.op_stats
        op_msg.op_count = op_stats.op_count
        op_msg.update_op_count = op_stats.update_op_count
        op_msg.read_op_count = op_stats.read_op_count
        op_msg.input_fetch_dur = op_stats.input_fetch_dur
        op_msg.flops = op_stats.flops
        op_msg.runtime_flops = int(op_stats.runtime_flops)
        op_msg.recv_op_count = op_stats.recv_op_count
        return self._stub.report_model_metric(metric_msg)

    @retry_grpc_request
    def report_global_step(self, global_step, timestamp):
        record = elasticai_api_pb2.GlobalStepRecord()
        record.global_step = global_step
        record.timestamp = timestamp
        return self._stub.report_global_step(record, timeout=10)

    @retry_grpc_request
    def get_cluster_version(self, version_type, task_type, task_id):
        request = elasticai_api_pb2.GetClusterVersionRequest()
        request.task_id = task_id
        request.version_type = version_type
        request.task_type = task_type
        return self._stub.get_cluster_version(request)

    @retry_grpc_request
    def update_cluster_version(
        self, version_type, version, task_type, task_id
    ):
        request = elasticai_api_pb2.UpdateClusterVersionRequest()
        request.task_id = task_id
        request.version_type = version_type
        request.version = version
        request.task_type = task_type
        self._stub.update_cluster_version(request)

    @retry_grpc_request
    def query_ps_nodes(self):
        request = empty_pb2.Empty()
        response = self._stub.query_ps_nodes(request)
        return response.ps_nodes, response.new_ps_ready

    @retry_grpc_request
    def query_training_status(self):
        request = empty_pb2.Empty()
        response = self._stub.query_training_status(request)
        return response.status

    @retry_grpc_request
    def init_remote_lock(self, name, timeout, retry=3):
        request = elasticai_api_pb2.InitRemoteLockRequest()
        request.name = name
        request.timeout = timeout
        request.worker_id = self._worker_id
        self._stub.init_remote_lock(request)

    @retry_grpc_request
    def acquire_remote_lock(self, name, timeout):
        request = elasticai_api_pb2.AcquireRemoteLockRequest()
        request.name = name
        request.timeout = timeout
        request.worker_id = self._worker_id
        res = self._stub.acquire_remote_lock(request)
        return res.success

    @retry_grpc_request
    def release_remote_lock(self, name):
        request = elasticai_api_pb2.ReleaseRemoteLockRequest()
        request.name = name
        self._stub.release_remote_lock(request)

    @retry_grpc_request
    def report_autotune_status(self, auto_ps, auto_worker):
        request = elasticai_api_pb2.AutoResourceConfig()
        request.auto_ps = auto_ps
        request.auto_worker = auto_worker
        self._stub.report_autotune_status(request)

    def update_critical_worker(self, critical_workers):
        try:
            request = elasticai_api_pb2.UpdateCriticalWorkerRequest()
            for worker_id, num in critical_workers.items():
                request.critical_workers[worker_id] = num
            self._stub.update_critical_worker(request)
            return True
        except Exception as e:
            logger.warning(e)
        return False

    def set_job_resource(
        self,
        ps_num=0,
        ps_cpu=0,
        ps_mem=0,
        worker_num=0,
        worker_cpu=0,
        worker_mem=0,
    ):
        opt_res = easydl_pb2.OptimizeResponse()
        plan = opt_res.job_optimize_plans.add()
        if ps_num > 0:
            group_resource = plan.resource.task_group_resources["ps"]
            group_resource.count = ps_num
            group_resource.resource.cpu = ps_cpu
            group_resource.resource.memory = ps_mem
        if worker_num > 0:
            group_resource = plan.resource.task_group_resources["worker"]
            group_resource.count = worker_num
            group_resource.resource.cpu = worker_cpu
            group_resource.resource.memory = worker_mem
        self._stub.optimize(opt_res)

    def migrate_nodes(self, nodes):
        """
        Args:
            nodes: list of dicts
                {"name":"ps-0", "cpu":10, "memory":1024}
        """
        opt_res = easydl_pb2.OptimizeResponse()
        plan = opt_res.job_optimize_plans.add()
        for node in nodes:
            pod_resource = plan.resource.pod_resources[node["name"]]
            pod_resource.cpu = node["cpu"]
            pod_resource.memory = node["memory"]
        self._stub.optimize(opt_res)

    def report_prestop(self):
        req = elasticai_api_pb2.ReportPreStopRequest()
        req.worker_host = self._worker_host
        logger.info("Worker {} report prestop hook".format(self._worker_host))
        return self._stub.report_prestop(req)

    def get_running_nodes(self):
        request = empty_pb2.Empty()
        response = self._stub.query_running_nodes(request)
        return response.nodes

    def _report(self, data: Message):
        msg = elasticai_api_pb2.Message()
        msg.node_id = self._worker_id
        msg.node_type = self._worker_type
        msg.data = data.serialize()
        response = self._stub.report(msg)
        return response.success

    def report_reader_profile(self, record_num, elapsed_time):
        data = ReaderProfile(
            record_num=record_num,
            elapsed_time=elapsed_time,
        )
        self._report(data)


class LocalDataset(object):
    def __init__(
        self,
        batch_size,
        num_epochs,
        dataset_size,
        shuffle,
        shuffle_shards,
        num_minibatches_per_shard,
        task_type=elasticai_api_pb2.NONE,
    ):
        self._batch_size = batch_size
        self._num_epochs = num_epochs
        self._dataset_size = dataset_size
        self._shuffle = shuffle
        self._shuffle_shards = shuffle_shards
        self._records_per_shard = batch_size * num_minibatches_per_shard
        self._todo = []
        self._epoch = 0
        self._task_type = task_type

    def create_tasks(self):
        start = 0
        if self._records_per_shard <= 0:
            raise ValueError(
                "records_per_shard {} can not be less than 1".format(
                    self._record_per_shard
                )
            )
        while start < self._dataset_size:
            end = min(start + self._records_per_shard, self._dataset_size)
            self._todo.append((start, end))
            start = end
        if self._shuffle_shards:
            random.shuffle(self._todo)

    def get_task(self, task_type=None):
        start = -1
        end = -1
        if not self._todo and self._epoch < self._num_epochs:
            self.create_tasks()
            self._epoch += 1
        if self._todo:
            start, end = self._todo.pop(0)
        return start, end

    def get_current_epoch(self):
        return self._epoch

    def reset(self):
        self._epoch = 0
        self._todo = []


class LocalMasterClient(object):
    """MockedMasterClient provides the same API as MasterClient without
    any RPC call.
    """

    def __init__(self, worker_id):
        """Initialize a master client.
        Args:
            worker_id: int
            the unique and ordered worker ID assigned
            by elasticdl command-line.
        """
        self._worker_id = worker_id
        self._num_minibatches_per_shard = 0
        self._datasets = {}
        self._task_type = None

    def reset_dataset(self, dataset_name):
        """Reset a dataset

        Args:
            dataset_name: name of the dataset, must not be None.
        """
        dataset = self._datasets.get(dataset_name, None)
        dataset.reset()

    def get_task(self, task_type=None):
        shard = elasticai_api_pb2.Shard()
        res = elasticai_api_pb2.Task(shard=shard)
        return True, res

    def get_dataset_task(self, dataset_name):
        """Get a task from master.

        Args:
            dataset_name: string
            the training phase, c.f. /elasticai_api/proto/elasticai_api.proto

        Returns:
            the task unit assigned by master,
            c.f. /elasticai_api/proto/elasticai_api.proto
        """

        shard = elasticai_api_pb2.Shard()
        res = elasticai_api_pb2.Task(shard=shard)
        dataset = self._datasets.get(dataset_name, None)
        if dataset:
            start, end = dataset.get_task()
            if start != -1 and end != -1:
                res.shard.start = start
                res.shard.end = end
                res.type = self._task_type
        return True, res

    def report_task_result(
        self, task_id, err_msg, dataset_name=None, exec_counters=None
    ):
        """Report task result to master.

        Args:
          task_id: int
          the task ID assigned by master

          err_msg: string
          the error message on training.

          exec_counters: dict
          statistics of the task being executed.
        """
        return empty_pb2.Empty()

    def get_comm_rank(self):
        res = elasticai_api_pb2.GetCommRankResponse()
        res.rank_id = 0
        res.world_size = 1
        res.rendezvous_id = 0
        res.rendezvous_port = 12345
        res.local_rank = 0
        res.local_size = 1
        res.cross_rank = 0
        res.cross_size = 1
        return res

    def report_training_loop_status(self, status):
        return True

    def report_training_params(
        self,
        batch_size,
        num_epochs=None,
        dataset_size=None,
        shuffle=False,
        shuffle_shards=False,
        num_minibatches_per_shard=0,
        dataset_name=None,
        task_type=elasticai_api_pb2.NONE,
        remainder=None,
    ):
        dataset = LocalDataset(
            batch_size,
            num_epochs,
            dataset_size,
            shuffle,
            shuffle_shards,
            num_minibatches_per_shard,
            task_type,
        )
        self._task_type = task_type
        self._datasets[dataset_name] = dataset

    def get_dataset_epoch(self, dataset_name):
        dataset = self._datasets.get(dataset_name, None)
        res = elasticai_api_pb2.GetDatasetEpochResponse()
        if dataset:
            res.epoch = dataset.get_current_epoch()
        return res

    def report_model_metric(self, *args):
        return empty_pb2.Empty()

    def report_used_resource(self, memory, cpu):
        return empty_pb2.Empty()


def build_master_client(master_addr=None):
    if master_addr is None:
        master_addr = os.getenv(PodEnv.DLROVER_MASTER_ADDR, "")
    worker_id = int(os.getenv(PodEnv.WORKER_ID, 0))
    worker_type = os.getenv(PodEnv.WORKER_TYPE, "worker")

    if master_addr:
        master_client = MasterClient(master_addr, worker_id, worker_type)
    else:
        master_client = LocalMasterClient(worker_id)

    return master_client


class GlobalMasterClient(object):
    MASTER_CLIENT = build_master_client()
