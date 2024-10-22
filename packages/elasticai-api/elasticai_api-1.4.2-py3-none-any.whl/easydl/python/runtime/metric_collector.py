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

import json

from easydl.proto import easydl_pb2
from easydl.python.runtime.easydl_client import (
    GlobalEasydlClient,
    JobMeta,
    init_job_metrics_message,
)


class TaskResource(object):
    def __init__(self, num=None, cpu=None, memory=None, gpu=None, rdma=None):
        self.num = num
        self.cpu = cpu
        self.memory = memory
        self.gpu = gpu
        self.rdma = rdma


class JobResource(object):
    def __init__(self, worker_resource=None, ps_resource=None):
        self.worker = worker_resource
        self.ps = ps_resource

    def to_json(self):
        data = {}
        if self.worker:
            data["worker"] = json.dumps(self.worker.__dict__)
        if self.ps:
            data["ps"] = json.dumps(self.ps.__dict__)
        return json.dumps(data)


class MetricCollector(object):
    def __init__(self):
        self._easydl_client = GlobalEasydlClient.EASYDL_CLIENT

    def report_job_meta(
        self, job_uuid, job_name, user_id, namespace="", cluster=""
    ):
        """Report the job meta to EasyDL DB.
        Args:
            job_uuid: str, the unique id of the job which is usually
                the uuid in the job yaml of k8s.
            job_name: str, the name of training job.
            user_id: the user id.
        """
        job_meta = JobMeta(
            uuid=job_uuid,
            name=job_name,
            namespace=namespace,
            cluster=cluster,
            user=user_id,
        )
        job_metrics = init_job_metrics_message(job_meta)
        job_metrics.metrics_type = easydl_pb2.MetricsType.Workflow_Feature
        metrics = job_metrics.workflow_feature
        metrics.job_name = job_name
        metrics.user_id = user_id
        self._easydl_client.report_metrics(job_metrics)

    def report_job_type(self, job_uuid, job_type):
        """Report the job type to EasyDL DB.
        Args:
            job_uuid: str, the unique id of the job which is usually
                the uuid in the job yaml of k8s.
            job_type: str, the type of training job like "alps", "atorch",
                "penrose" and so on.
        """
        job_meta = JobMeta(uuid=job_uuid)
        job_metrics = init_job_metrics_message(job_meta)
        job_metrics.metrics_type = easydl_pb2.MetricsType.Type
        job_metrics.type = job_type
        self._easydl_client.report_metrics(job_metrics)

    def report_job_resource(self, job_uuid, job_resource):
        """Report the job resource to EasyDL DB.
        Args:
            job_uuid: str, the unique id of the job which is usually
                the uuid in the job yaml of k8s.
            job_resource: JobResource instance.
        Example:
        ```Python
        >>> import os
        >>> from easydl.python.runtime.metric_collector import MetricCollector
        >>> from dlrover.python.master.resource.job import JobResource
        >>> from dlrover.python.common.node import (
        ...     NodeGroupResource,
        ...     NodeResource,
        ... )

        >>> collector = MetricCollector()

        >>> job_resource = JobResource()
        >>> job_resource.node_group_resources["worker"] = NodeGroupResource(
        ...     2, NodeResource(8, 1024)
        ... )

        >>> collector.report_job_resource(
        ...    job_uuid="easydl-test-job-0",
        ...    job_resource=job_resource,
        ... )
        ```
        """
        job_meta = JobMeta(uuid=job_uuid)
        job_metrics = init_job_metrics_message(job_meta)
        job_metrics.metrics_type = easydl_pb2.MetricsType.Resource
        job_metrics.resource = job_resource.to_json()
        self._easydl_client.report_metrics(job_metrics)

    def report_model_meta(
        self, job_uuid, model_size=0, variable_count=0, ops_count=0
    ):
        """Report the model meta to EasyDL DB.
        Args:
            job_uuid: str, the unique id of the job which is usually
                the uuid in the job yaml of k8s.
            model size: int, the size of the NN model.
            variable_count: int, the total count of variables in the model.
            ops_count: int, the total count of ops in the model.
        """
        job_meta = JobMeta(uuid=job_uuid)
        job_metrics = init_job_metrics_message(job_meta)
        job_metrics.metrics_type = easydl_pb2.MetricsType.Model_Feature
        metrics = job_metrics.model_feature
        metrics.total_variable_size = model_size
        metrics.variable_count = variable_count
        metrics.op_count = ops_count
        self._easydl_client.report_metrics(job_metrics)

    def report_customized_data(self, job_uuid, cutomized_data):
        """Report the job resource to EasyDL DB.
        Args:
            job_uuid: str, the unique id of the job which is usually
                the uuid in the job yaml of k8s.
            cutomized_data: A dictionary.

        Example:
        ```Python
        >>> import os
        >>> from easydl.python.runtime.metric_collector import MetricCollector
        >>> collector = MetricCollector()
        >>> cutomized_data = {"feature0": "1"}
        >>> collector.report_customized_data(
        ...     job_uuid="easydl-test-job-0",
        ...     cutomized_data=cutomized_data,
        ... )
        ```
        """
        job_meta = JobMeta(uuid=job_uuid)
        job_metrics = init_job_metrics_message(job_meta)
        job_metrics.metrics_type = easydl_pb2.MetricsType.Customized_Data
        job_metrics.customized_data = json.dumps(cutomized_data)
        self._easydl_client.report_metrics(job_metrics)

    def report_runtime_info(self, job_uuid, runtime_metrics):
        """Report the runtime stats information to EasyDL DB.
        EasyDL Brain saves the runtime metrics into a sequence and
        the latest runtime metric will locate at the end.

        Args:
            job_uuid (`str`): the unique id of the job which is usually
                the uuid in the job yaml of k8s.
            runtime_metrics: dlrover.python.master.stats.
                training_metrics.RuntimeMetric instances.

        Example:
        ```python
        >>> import os
        >>> from easydl.python.runtime.metric_collector import MetricCollector
        >>> from dlrover.python.common.node import (
        ...     Node,
        ...     NodeGroupResource,
        ...     NodeResource,
        ... )

        >>> collector = MetricCollector()

        >>> for i in range(3):
        ...     worker = Node(
        ...         NodeType.WORKER, i, config_resource=NodeResource(6, 4096)
        ...     )
        ...     worker.used_resource = NodeResource(1, 2048)
        ...     nodes.append(worker)
        ... metrics = RuntimeMetric(
        ...    nodes, global_step=step, speed=10, timestamp=10000,
        ... )
        >>> collector.report_runtime_info(
        ...    job_uuid="easdy-test-job-9",
        ...    runtime_metrics=metrics,
        ...)
        ```
        """
        job_meta = JobMeta(uuid=job_uuid)
        self._easydl_client.report_node_runtime_stats(
            job_meta, runtime_metrics
        )
