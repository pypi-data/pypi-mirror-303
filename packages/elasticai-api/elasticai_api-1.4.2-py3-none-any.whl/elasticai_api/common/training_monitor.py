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

import json
import os
import threading
import time

import psutil

from elasticai_api.common.master_client import GlobalMasterClient
from elasticai_api.util.log_utils import default_logger as logger
from elasticai_api.util.singleton_utils import singleton

READER_PROFILE_DIR = "/tmp/aistudio_reader/"


def is_tf_chief():
    TF_CONFIG = os.getenv("TF_CONFIG", "")
    if not TF_CONFIG:
        return False
    config = json.loads(TF_CONFIG)
    task = config.get("task", None)
    if not task:
        return False
    if task.get("type", None) == "chief" and task.get("index", None) == 0:
        return True
    return False


def get_process_cpu_percent():
    """Get the cpu percent of the current process."""
    try:
        procTotalPercent = 0
        result = {}
        proc_info = []
        # 分析依赖文件需要获取 memory_maps
        # 使用进程占用的总CPU计算系统CPU占用率
        for proc in psutil.process_iter(
            ["pid", "ppid", "name", "username", "cmdline"]
        ):
            proc_percent = proc.cpu_percent()
            procTotalPercent += proc_percent
            proc.info["cpu_percent"] = round(proc_percent, 2)
            proc_info.append(proc.info)
        # 暂时不上报进程数据，看下数据量的情况
        result["proc_info"] = proc_info
        cpu_count = psutil.cpu_count(logical=True)
        cpu_percent = round(procTotalPercent / cpu_count, 2)
    except Exception:
        cpu_percent = 0.0
    return cpu_percent / 100.0


def get_used_memory():
    """ "Get the used memory of the container"""
    mem = psutil.virtual_memory()
    return mem.used


@singleton
class ResourceMonitor(object):
    def __init__(self):
        """
        The monitor samples the used memory and cpu percent
        reports the used memory and cpu percent to the ElasticDL master.
        """
        self._total_cpu = psutil.cpu_count(logical=True)
        if (
            os.getenv("DLROVER_MASTER_ADDR")
            and os.getenv("ELASTICDL_ENABLED", "") == "true"
        ):
            threading.Thread(
                target=self._monitor_resource,
                name="monitor_resource",
                daemon=True,
            ).start()

    def start_monitor_cpu(self):
        get_process_cpu_percent()

    def report_resource(self):
        try:
            used_mem = get_used_memory()
            cpu_percent = get_process_cpu_percent()
            current_cpu = round(cpu_percent * self._total_cpu, 2)
            record_num, elapsed_time = self._read_reader_profile()
            GlobalMasterClient.MASTER_CLIENT.report_reader_profile(
                record_num=record_num,
                elapsed_time=elapsed_time,
            )
            GlobalMasterClient.MASTER_CLIENT.report_used_resource(
                used_mem, current_cpu
            )
            logger.info(
                "Report resource CPU : %s, Memory %s", current_cpu, used_mem
            )
        except Exception as e:
            logger.info(e)

    def _monitor_resource(self):
        logger.info("Start to monitor resource usage")
        while True:
            self.report_resource()
            time.sleep(60)

    def _read_reader_profile(self):
        """The ODPS tunnel reader will write the profiling data
        into a file withe one line like "50000,10000"
        """
        record_num = 0
        elapsed_time = 0
        if os.path.exists(READER_PROFILE_DIR):
            for file in os.listdir(READER_PROFILE_DIR):
                if not file.endswith("_profile.txt"):
                    continue
                path = os.path.join(READER_PROFILE_DIR, file)
                with open(path, "r") as f:
                    data = f.read()
                    record_num += int(data.split(",")[0])
                    elapsed_time += int(data.split(",")[1])
        return record_num, elapsed_time


@singleton
class TrainingProcessReporter(object):
    def __init__(self):
        self._resource_monitor = ResourceMonitor()
        self._last_timestamp = 0
        self._start_time = 0
        self.called_in_tf_hook = False
        self._is_tf_chief = is_tf_chief()

    def set_start_time(self):
        if self._start_time == 0:
            timestamp = int(time.time())
            self._last_timestamp = timestamp
            self._start_time = timestamp
            self._resource_monitor.start_monitor_cpu()
            logger.info(
                "Start training process reporter in TF hooks : %s",
                self.called_in_tf_hook,
            )

    def report_resource_with_step(self, step):
        if not self._is_tf_chief:
            return
        try:
            timestamp = int(time.time())
            secs = self.get_wait_seconds(timestamp)
            if step > 0 and timestamp - self._last_timestamp > secs:
                self._resource_monitor.report_resource()
                logger.info("Report global step = {}".format(step))
                self._last_timestamp = timestamp
                GlobalMasterClient.MASTER_CLIENT.report_global_step(
                    step, self._last_timestamp
                )
        except Exception as e:
            logger.warning(e)

    def get_wait_seconds(self, timestamp):
        """Adjust the waited seconds by the training time"""
        if timestamp - self._start_time < 1800:
            return 60
        elif timestamp - self._start_time < 3600:
            return 180
        else:
            return 300
