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

from easydl.python.common.constants import EasydlOptRetriever
from easydl.python.common.log_utils import default_logger as logger
from easydl.python.runtime.easydl_client import (
    BASE_OPTIMIZE_PROCESSOR,
    GlobalEasydlClient,
)


def catch_easydl_optimization_exception(func):
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except Exception as e:
            logger.debug("Fail to execute %s by %s", func.__name__, e)

    return wrapper


class EDLJobResoureOptimizer(object):
    def __init__(self, job_uuid):
        self._job_uuid = job_uuid
        self._easydl_client = GlobalEasydlClient.EASYDL_CLIENT

    @catch_easydl_optimization_exception
    def get_optimization_plan(self, stage, config={}, processor=None):
        logger.info("Optimize at stage %s, with config %s", stage, config)
        res = self._easydl_client.get_optimization_plan(
            self._job_uuid,
            stage,
            EasydlOptRetriever.BASE_CONFIG_RETRIEVER,
            config,
            processor,
        )
        if not res.job_optimize_plans:
            logger.info("No any optimization plan for PS")
            return

        plan = self._select_job_plan(res.job_optimize_plans)
        logger.info(
            "The optimization plan of %s with config %s is %s",
            stage,
            config,
            plan,
        )
        return plan

    @catch_easydl_optimization_exception
    def get_oom_resource_plan(
        self, oom_pods, stage, config={}, processor=None
    ):
        res = self._easydl_client.get_oom_resource_plan(
            oom_pods,
            self._job_uuid,
            stage,
            EasydlOptRetriever.BASE_CONFIG_RETRIEVER,
            config,
            processor,
        )
        if not res.job_optimize_plans:
            logger.info("No any optimization plan for PS")
            return

        plan = self._select_job_plan(res.job_optimize_plans)
        logger.info("The optimization plan of %s is %s", stage, plan)
        return plan

    @catch_easydl_optimization_exception
    def get_estimated_resource_plan(self):
        config = {"optimizer": "job_resource_estimate_optimizer"}
        res = self._easydl_client.get_optimization_plan(
            job_uuid=self._job_uuid,
            stage="",
            opt_retriever=EasydlOptRetriever.BASE_CONFIG_RETRIEVER,
            config=config,
            processor=BASE_OPTIMIZE_PROCESSOR,
        )
        if not res.job_optimize_plans:
            logger.info("No any estimated plan for PS")
            return

        plan = self._select_job_plan(res.job_optimize_plans)
        logger.info("The estimated plan is %s", plan)
        return plan

    def _select_job_plan(self, plans):
        for plan in plans:
            if plan and plan.job.uid == self._job_uuid:
                return plan
        return None
