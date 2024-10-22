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


class RemoteLock(object):
    def __init__(self, name, timeout=-1):
        """Remote lock for workers
        Args:
            name: The unique name of the lock
            timeout: The maximum blocked time of the lock.
        """
        self._name = name
        self._master_client = GlobalMasterClient.MASTER_CLIENT
        self._master_client.init_remote_lock(self._name, timeout)

    def acquire(self, timeout=-1):
        return self._master_client.acquire_remote_lock(self._name, timeout)

    def release(self):
        self._master_client.release_remote_lock(self._name)

    def __enter__(self):
        self.acquire()

    def __exit__(self, type, value, traceback):
        self.release()
