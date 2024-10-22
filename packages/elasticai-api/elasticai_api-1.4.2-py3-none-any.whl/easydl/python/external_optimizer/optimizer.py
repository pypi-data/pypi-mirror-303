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

from abc import ABCMeta, abstractmethod

from easydl.python.common.log_utils import default_logger as logger


class Optimizer(metaclass=ABCMeta):
    def __init__(self):
        self._training_jobs = set()

    @abstractmethod
    def optimize(self, job_meta, plan):
        """Optimize a job resource configuration
        Args:
            job_meta: an instance of easydl_pb2.JobMeta.
                The attributes of job_meta contains:
                uid: the uuid of a job.
                namespace: the namespace of a job.
                cluster: the cluster of a job.
            plan: the output of the optimizer. We can set resources
            into the plan like:
            ```python
            group_resources = plan.resource.task_group_resources
            group_resources["worker"].count = 5
            group_resources["worker"].resource.memory = 8 * 1024 * 1024
            group_resources["worker"].resource.cpu = 16

            group_resources["ps"].count = 2
            group_resources["ps"].resource.memory = 8 * 1024 * 1024
            group_resources["ps"].resource.cpu = 16

            pod_resources = plan.resource.pod_resources
            pod_resource["worker-0"].memory = 8 * 1024 * 1024
            pod_resource["worker-0"].cpu = 16
            ```
        """
        pass

    def add_training_job(self, job_uid):
        self._training_jobs.add(job_uid)

    def remove_training_job(self, job_uid):
        self._training_jobs.remove(job_uid)

    def check_restart_job(self, job_name):
        """Check wether to restart a job"""
        pass


class NaiveOptimizer(Optimizer):
    def __init__(self):
        super(NaiveOptimizer, self).__init__()

    def optimize(self, job_meta, plan):
        logger.info("Optimizer job %s", job_meta)
        group_resources = plan.resource.task_group_resources
        group_resources["worker"].count = 5
        group_resources["worker"].resource.memory = 8 * 1024 * 1024 * 1024
        group_resources["worker"].resource.cpu = 16

        group_resources["ps"].count = 2
        group_resources["ps"].resource.memory = 8 * 1024 * 1024 * 1024
        group_resources["ps"].resource.cpu = 16
