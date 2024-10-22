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
from elasticai_api.common.master_client import GlobalMasterClient


class ElasticWorkerService(object):
    def __init__(self):
        self._master_client = GlobalMasterClient.MASTER_CLIENT

    def get_running_workers(self):
        running_nodes = self._master_client.get_running_nodes()
        running_workers = []
        for node in running_nodes:
            if node.type == "worker":
                running_workers.append(node)
        return running_workers
