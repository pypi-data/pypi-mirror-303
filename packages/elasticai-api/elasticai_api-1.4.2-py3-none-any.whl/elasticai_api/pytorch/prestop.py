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

import time

from elasticai_api.common.master_client import GlobalMasterClient


def prestop_hook(master_client):
    def report_prestop(sleep_time=0):
        master_client.report_prestop()
        time.sleep(sleep_time)
        return None

    return report_prestop


if __name__ == "__main__":
    report_prestop = prestop_hook(GlobalMasterClient.MASTER_CLIENT)
    report_prestop(120)
