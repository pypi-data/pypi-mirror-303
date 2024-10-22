# Copyright 2023 The EasyDL Authors. All rights reserved.
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

import os
import threading
import time
from typing import Dict, Set

from kubernetes import client, config

from easydl.python.common.log_utils import default_logger as logger
from easydl.python.external_optimizer.optimizer import Optimizer

LABEL_RL_JOB_KEY = "easydl.rl-env-name"
LABEL_RL_ENV_VALUE = "rl-training-environment"


class k8sClient(object):
    def __init__(self, namespace):
        """
        ElasticDL k8s client.

        Args:
            image_name: Docker image path for ElasticDL pod.
            namespace: The name of the Kubernetes namespace where ElasticDL
                pods will be created.
            job_name: ElasticDL job name, should be unique in the namespace.
                Used as pod name prefix and value for "elastic" label.
            event_callback: If not None, an event watcher will be created and
                events passed to the callback.
            periodic_call_func: If not None, call this method periodically.
        """
        try:
            if os.getenv("KUBERNETES_SERVICE_HOST"):
                # We are running inside a k8s cluster
                config.config.load_incluster_config()
                logger.info("Load the incluster config.")
        except Exception as ex:
            logger.error(
                "Failed to load configuration for Kubernetes:\n%s", ex
            )

        self.client = client.CoreV1Api()
        self.api_instance = client.CustomObjectsApi()
        self._namespace = namespace

    def create_custom_resource(self, group, version, plural, body):
        try:
            self.api_instance.create_namespaced_custom_object(
                group=group,
                version=version,
                namespace=self._namespace,
                plural=plural,
                body=body,
            )
        except client.rest.ApiException as e:
            logger.error(
                "Exception when calling CustomObjectsApi->",
                "create_namespaced_custom_object: %s" % e,
            )

    def list_custom_resource(self, group, version, plural, label_selector):
        try:
            jobs = self.api_instance.list_namespaced_custom_object(
                group=group,
                version=version,
                plural=plural,
                namespace=self._namespace,
                label_selector=label_selector,
            )
            return jobs
        except client.rest.ApiException as e:
            logger.error(
                "Exception when calling CustomObjectsApi->",
                "list_namespaced_custom_object: %s" % e,
            )

    def delete_custom_resource(self, group, version, plural, name):
        try:
            self.api_instance.delete_namespaced_custom_object(
                group=group,
                version=version,
                namespace=self._namespace,
                plural=plural,
                name=name,
            )
        except client.rest.ApiException:
            logger.error("Fail to delete %s", name)


class RLEnvManager(object):
    """RLEnvManager manages DL training jobs of the RL env.
    The manager will mointor training jobs with the label:
    ```
    labels:
        easydl.rl-env-name: aistudio-wide-deep
        easydl.scenario: rl-training-environment
    name:
        aistudio-wide-deep-0
    ```
    """

    def __init__(self, namespace, rl_optimizer: Optimizer) -> None:
        self._namespace = namespace
        self._rl_optimizer = rl_optimizer
        self._k8s_client = k8sClient(namespace)
        self._env_jobs: Dict[str, dict] = {}
        self._job_uids: Set[str] = set()

    def start(self):
        if os.getenv("KUBERNETES_SERVICE_HOST"):
            threading.Thread(
                target=self._monitor_jobs,
                name="monitor_jobs",
                daemon=True,
            ).start()
            threading.Thread(
                target=self._periodical_restart_env,
                name="periodical_restart_env",
                daemon=True,
            ).start()

    def _monitor_jobs(self):
        while True:
            jobs = self.list_jobs()
            alive_job_uids = []
            for job in jobs:
                rl_job_name = job["metadata"]["labels"][LABEL_RL_JOB_KEY]
                self.clear_job_runtime_info(job)
                self._env_jobs[rl_job_name] = job
                job_uid = job["metadata"]["uid"]
                alive_job_uids.append(job_uid)
                if job_uid not in self._job_uids:
                    self._job_uids.add(job_uid)
                    self._rl_optimizer.add_training_job(job_uid)
                for env_name, job in self._env_jobs.items():
                    logger.info(
                        "Env %s with job %s", env_name, job["metadata"]["name"]
                    )
            for job_uid in self._job_uids:
                if job_uid not in alive_job_uids:
                    self._job_uids.remove(job_uid)
                    self._rl_optimizer.remove_training_job(job_uid)
            time.sleep(30)

    def _periodical_restart_env(self):
        while True:
            for env_name, job in self._env_jobs.items():
                job_name = job["metadata"]["name"]
                if self._rl_optimizer.check_restart_job(job_name):
                    self.restart_job(env_name)
            time.sleep(15)

    def restart_job(self, rl_job_name):
        logger.info("restart job %s", rl_job_name)
        job = self._env_jobs[rl_job_name]
        if "uid" in job["metadata"]:
            job["metadata"].pop("uid")
        job_name = job["metadata"]["name"]
        self._k8s_client.delete_custom_resource(
            group="jobs.kubemaker.alipay.net",
            version="v1beta1",
            plural="trainings",
            name=job_name,
        )
        index_position = job_name.rindex("-") + 1
        job["metadata"]["name"] = job_name[:index_position] + str(
            int(job_name[index_position:]) + 1
        )
        logger.info(
            "Create a job %s for env %s", job["metadata"]["name"], rl_job_name
        )
        self._k8s_client.create_custom_resource(
            group="jobs.kubemaker.alipay.net",
            version="v1beta1",
            plural="trainings",
            body=job,
        )

    def stop_job(self, rl_job_name):
        if rl_job_name not in self._env_jobs:
            logger.info("RL env %s not found.", rl_job_name)
            return
        job = self._env_jobs.pop(rl_job_name)
        job_name = job["metadata"]["name"]
        self._k8s_client.delete_custom_resource(
            group="jobs.kubemaker.alipay.net",
            version="v1beta1",
            plural="trainings",
            name=job_name,
        )

    def list_jobs(self):
        label_selector = "easydl.scenario={}".format(LABEL_RL_ENV_VALUE)
        jobs = self._k8s_client.list_custom_resource(
            group="jobs.kubemaker.alipay.net",
            version="v1beta1",
            plural="trainings",
            label_selector=label_selector,
        )
        if jobs:
            return jobs["items"]
        return []

    def clear_job_runtime_info(self, job):
        job["metadata"].pop("resourceVersion", None)
        job["metadata"].pop("selfLink", None)
        job.pop("status", None)
