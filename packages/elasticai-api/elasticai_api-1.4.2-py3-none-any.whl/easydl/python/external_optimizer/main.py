# Copyright 2022 The ElasticDL Authors. All rights reserved.
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

import argparse
import time

from easydl.python.external_optimizer.servicer import create_optimizer_server

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="External Optimizer Parser")
    parser.add_argument("--optimizer_name", type=str, default="naive")
    args = parser.parse_args()

    server = create_optimizer_server(3333, args.optimizer_name)
    server.start()
    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)
