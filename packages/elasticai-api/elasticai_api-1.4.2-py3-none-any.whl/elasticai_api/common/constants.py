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


class GRPC(object):
    # gRPC limits the size of message by default to 4MB.
    # It's too small to send model parameters.
    MAX_SEND_MESSAGE_LENGTH = 256 * 1024 * 1024
    MAX_RECEIVE_MESSAGE_LENGTH = 256 * 1024 * 1024


class HorovodEnv(object):
    RENDEZVOUS_ADDR = "HOROVOD_GLOO_RENDEZVOUS_ADDR"
    RENDEZVOUS_PORT = "HOROVOD_GLOO_RENDEZVOUS_PORT"
    RANK = "HOROVOD_RANK"
    SIZE = "HOROVOD_SIZE"
    CONTROLLER = "HOROVOD_CONTROLLER"
    CPU_OPERATIONS = "HOROVOD_CPU_OPERATIONS"
    HOSTNAME = "HOROVOD_HOSTNAME"
    ELASTIC = "HOROVOD_ELASTIC"
    GLOO_TIMEOUT_SECONDS = "HOROVOD_GLOO_TIMEOUT_SECONDS"
    HOROVOD_LOCAL_RANK = "HOROVOD_LOCAL_RANK"
    HOROVOD_LOCAL_SIZE = "HOROVOD_LOCAL_SIZE"
    HOROVOD_CROSS_RANK = "HOROVOD_CROSS_RANK"
    HOROVOD_CROSS_SIZE = "HOROVOD_CROSS_SIZE"


class DDPEnv(object):
    NCCL_BLOCKING_WAIT = "NCCL_BLOCKING_WAIT"
    RANK = "RANK"
    SIZE = "WORLD_SIZE"
    LOCAL_RANK = "LOCAL_RANK"
    DDP_MASTER_ADDR = "MASTER_ADDR"
    DDP_MASTER_PORT = "MASTER_PORT"


class CommunicationBackend(object):
    NCCL = "nccl"
    GLOO = "gloo"


class PodEnv(object):
    RELAUNCHED_POD = "RELAUNCHED_POD"
    ELASTICDL_ENABLED = "ELASTICDL_ENABLED"
    DLROVER_MASTER_ADDR = "DLROVER_MASTER_ADDR"
    WORKER_TYPE = "WORKER_TYPE"
    WORKER_ID = "WORKER_ID"
    WORKER_NUM = "WORKER_NUM"


class TrainingLoopStatus(object):
    START = 1
    END = 2
    PENDING = 3


class DefaultDatasetName(object):
    TRAINING = "_EDL_DEFAULT_TRAINING_DATA"
    EVALUATION = "_EDL_DEFAULT_EVALUATION_DATA"


class ClusterVersionType(object):
    GLOBAL = "GLOBAL"
    LOCAL = "LOCAL"
    RESTORED = "RESTORED"


class PsTaskType(object):
    WORKER = "worker"
    PS = "ps"
    EVALUATOR = "evaluator"


class DatasetShardRemainder(object):
    FILL = "fill"
    DROP = "drop"
