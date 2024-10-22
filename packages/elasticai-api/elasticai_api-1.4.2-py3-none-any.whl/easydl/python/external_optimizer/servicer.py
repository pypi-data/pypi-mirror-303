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

from concurrent import futures

import grpc

from easydl.proto import easydl_pb2, easydl_pb2_grpc
from easydl.python.common.grpc_utils import GRPC
from easydl.python.common.log_utils import default_logger as logger
from easydl.python.external_optimizer.optimizer import NaiveOptimizer
from easydl.python.external_optimizer.rl_env_manager import RLEnvManager

optimizers = {
    "naive": NaiveOptimizer(),
}

NAMESPACE = "kubemaker"


def create_optimizer_server(port, optimizer_name=None):
    """Create GRPC server"""
    logger.info("Creating an optimizer server")
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=64),
        options=[
            ("grpc.max_send_message_length", GRPC.MAX_SEND_MESSAGE_LENGTH),
            (
                "grpc.max_receive_message_length",
                GRPC.MAX_RECEIVE_MESSAGE_LENGTH,
            ),
        ],
    )
    servicer = ExternalOptimizerServer(optimizer_name)
    easydl_pb2_grpc.add_ExternalOptimizerServicer_to_server(servicer, server)
    server.add_insecure_port("[::]:{}".format(port))
    logger.info("The port of the external server is: %d", port)
    return server


class ExternalOptimizerServer(easydl_pb2_grpc.ExternalOptimizerServicer):
    """ExternalOptimizer service implementation"""

    def __init__(self, optimizer_name):
        optimizer_name = optimizer_name if optimizer_name else "naive"
        self._optimizer = optimizers[optimizer_name]
        self._env_manager = RLEnvManager(NAMESPACE, self._optimizer)
        self._env_manager.start()

    def optimize(self, request, _):
        opt_res = easydl_pb2.OptimizeResponse()
        for job in request.jobs:
            opt_res.job_optimize_plans.add()
            plan = opt_res.job_optimize_plans[0]
            self._optimizer.optimize(job, plan)
        opt_res.response.success = True
        return opt_res

    def stop_rl_env(self, request, _):
        res = easydl_pb2.Response()
        self._env_manager.stop_job(res.name)
