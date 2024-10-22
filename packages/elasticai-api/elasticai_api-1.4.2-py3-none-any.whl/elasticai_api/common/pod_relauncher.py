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


from elasticai_api.common.master_client import GlobalMasterClient


def build_pod_relauncher():
    return PodRelauncher(master_client=GlobalMasterClient.MASTER_CLIENT)


class PodRelauncher(object):
    def __init__(
        self,
        master_client,
    ):
        self._mc = master_client

    def query_relaunch_ps_pod(self):
        return self._mc.query_relaunch_ps_pod()

    def ready_for_ps_relaunch(self):
        return self._mc.ready_for_ps_relaunch()

    def update_critical_worker(self, critical_workers):
        """Set critical workers.
        Args:
            critical_workers: A dictionary where keys are worker ids
                and values are the relaunched number of workers.
        """
        return self._mc.update_critical_worker(critical_workers)
