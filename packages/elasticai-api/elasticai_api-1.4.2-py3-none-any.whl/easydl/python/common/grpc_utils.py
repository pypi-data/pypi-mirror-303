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

import socket
import telnetlib
import time
from contextlib import closing

import grpc

from elasticdl.python.common.log_utils import default_logger as logger


class GRPC(object):
    # gRPC limits the size of message by default to 4MB.
    # It's too small to send model parameters.
    MAX_SEND_MESSAGE_LENGTH = 256 * 1024 * 1024
    MAX_RECEIVE_MESSAGE_LENGTH = 256 * 1024 * 1024


def build_channel(addr):
    if not addr_connected(addr):
        return None
    logger.info(f"Build channel with address {addr}.")
    channel = grpc.insecure_channel(
        addr,
        options=[
            ("grpc.max_send_message_length", GRPC.MAX_SEND_MESSAGE_LENGTH),
            (
                "grpc.max_receive_message_length",
                GRPC.MAX_RECEIVE_MESSAGE_LENGTH,
            ),
            ("grpc.enable_retries", True),
            (
                "grpc.service_config",
                """{ "retryPolicy":{ "maxAttempts": 5, \n
"initialBackoff": "0.2s", \n
"maxBackoff": "3s", "backoffMutiplier": 2, \n
"retryableStatusCodes": [ "UNAVAILABLE" ] } }""",
            ),
        ],
    )
    return channel


def addr_connected(addr):
    if not addr:
        return False
    host_port = addr.split(":")
    if len(host_port) != 2:
        return False
    host = host_port[0]
    port = int(host_port[1])
    try:
        telnetlib.Telnet(host=host, port=port, timeout=3)
        return True
    except socket.gaierror:
        logger.warning(f"Service {addr} is not connected.")
        return False
    except Exception as e:
        logger.error(f"Service {addr} is not connected.", e)
    return False


def find_free_port():
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind(("", 0))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return s.getsockname()[1]


def grpc_server_ready(channel, retry=10) -> bool:
    if not channel:
        return False
    for _ in range(retry):
        try:
            grpc.channel_ready_future(channel).result(timeout=3)
            return True
        except grpc.FutureTimeoutError:
            logger.error(f"GRPC channel {channel} is not ready.")
        time.sleep(3)
    return False
