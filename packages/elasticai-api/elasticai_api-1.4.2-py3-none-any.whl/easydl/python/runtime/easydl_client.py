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

import os
from typing import Dict

from easydl.proto import easydl_pb2, easydl_pb2_grpc
from easydl.python.common.grpc_utils import build_channel, grpc_server_ready
from easydl.python.common.log_utils import default_logger as logger

EASYDL_BRAIN_ADMINISTER_ADDR = "easydl-brain-administer.kubemaker.svc.\
em14.alipay.com:50001"
EASYDL_BRAIN_PROCESSOR_ADDR = "easydl-brain-processor.kubemaker.svc.\
em14.alipay.com:50001"
DATA_STORE = "data_store_elasticdl"
OPTIMIZE_PROCESSOR = "running_training_job_optimize_processor"
BASE_OPTIMIZE_PROCESSOR = "base_optimize_processor"


def catch_exception(func):
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except Exception as e:
            logger.warning(
                "Fail to %s.%s by %s",
                self.__class__.__name__,
                func.__name__,
                e,
            )

    return wrapper


def init_job_metrics_message(job_meta):
    job_metrics = easydl_pb2.JobMetrics()
    job_metrics.data_store = DATA_STORE
    job_metrics.job_meta.uuid = job_meta.uuid
    job_metrics.job_meta.name = job_meta.name
    job_metrics.job_meta.user = job_meta.user
    job_metrics.job_meta.cluster = job_meta.cluster
    job_metrics.job_meta.namespace = job_meta.namespace
    return job_metrics


class JobMeta(object):
    def __init__(self, uuid, name="", namespace="", cluster="", user=""):
        self.uuid = uuid
        self.name = name
        self.namespace = namespace
        self.cluster = cluster
        self.user = user


class EasydlClient(object):
    """EasyClient provides APIs to access EasyDL service via gRPC calls.

    Usage:
        channel = elasticai_api.util.grpc_utils.build_channel(
            "localhost:50001"
        )
        easydl_client = EasydlClient((channel, job_name="test")
        # Report metrics to EasyDL server
        easydl_client.report(...)
    """

    def __init__(self, administer_channel, processor_channel):
        """Initialize an EasyDL client.
        Args:
            administer_channel(str): channel for easydl-brain-administer.
            processor_channel(str): channel for easydl-brain-processor.
        """
        self._administer_stub = None
        self._processor_stub = None
        self.initialize_stub(administer_channel, processor_channel)

    def initialize_stub(self, administer_channel, processor_channel):
        if administer_channel is None and processor_channel is None:
            logger.info("Skip to initialize the channel with none channel.")
            return
        if grpc_server_ready(administer_channel):
            self._administer_stub = easydl_pb2_grpc.EasyDLStub(
                administer_channel
            )
            logger.info(
                f"Create administer stub with channel {self._administer_stub}"
            )
        else:
            logger.info("Channel to connect administer is not ready.")

        if grpc_server_ready(processor_channel):
            self._processor_stub = easydl_pb2_grpc.OptimizeProcessorStub(
                processor_channel
            )
            logger.info(
                f"Create administer stub with channel {self._processor_stub}"
            )
        else:
            logger.info("Channel to connect processor is not ready.")

    def report_metrics(self, job_metrics):
        """Report job metrics to administer service"""

        try:
            if self._administer_stub:
                return self._administer_stub.persist_metrics(job_metrics)
        except Exception as e:
            logger.warning(f"Report metrics got error: {str(e)}")

    def get_job_metrics(self, job_uuid):
        """Get the job metrics by the job uuid.
        Examples:
        ```
        >>> import json

        >>> client = build_easydl_client(None, None)
        >>> metrics_res = client.get_job_metrics("xxxx")
        >>> metrics = json.loads(metrics_res.job_metrics)
        ```
        """
        request = easydl_pb2.JobMetricsRequest()
        request.job_uuid = job_uuid

        try:
            if self._administer_stub:
                return self._administer_stub.get_job_metrics(request)
        except Exception as e:
            logger.warning(f"Get job metrics got error: {str(e)}")

    def request_optimization(self, opt_request):
        """Get the optimization plan from the processor service"""
        logger.debug(
            "Optimization request %s is send to %s",
            opt_request,
            EASYDL_BRAIN_PROCESSOR_ADDR,
        )

        try:
            if self._processor_stub:
                return self._processor_stub.optimize(opt_request)
        except Exception as e:
            logger.warning(f"Request optimization got error: {str(e)}")

    def report_training_hyper_params(self, job_meta, hyper_params):
        job_metrics = init_job_metrics_message(job_meta)
        job_metrics.metrics_type = easydl_pb2.MetricsType.Training_Hyper_Params
        metrics = job_metrics.training_hyper_params
        metrics.batch_size = hyper_params.batch_size
        metrics.epoch = hyper_params.epoch
        metrics.max_steps = hyper_params.max_steps
        return self.report_metrics(job_metrics)

    def report_workflow_feature(self, job_meta, workflow_feature):
        job_metrics = init_job_metrics_message(job_meta)
        job_metrics.job_meta.name = workflow_feature.job_name
        job_metrics.job_meta.user = workflow_feature.user_id
        job_metrics.metrics_type = easydl_pb2.MetricsType.Workflow_Feature

        metrics = job_metrics.workflow_feature
        metrics.job_name = workflow_feature.job_name
        metrics.user_id = workflow_feature.user_id
        metrics.code_address = workflow_feature.code_address
        metrics.workflow_id = workflow_feature.workflow_id
        metrics.node_id = workflow_feature.node_id
        metrics.odps_project = workflow_feature.odps_project
        metrics.is_prod = workflow_feature.is_prod
        metrics.priority = workflow_feature.priority
        metrics.app = workflow_feature.app
        return self.report_metrics(job_metrics)

    def report_training_set_metric(self, job_meta, dataset_metric):
        job_metrics = init_job_metrics_message(job_meta)
        job_metrics.metrics_type = easydl_pb2.MetricsType.Training_Set_Feature
        metrics = job_metrics.training_set_feature
        metrics.dataset_size = dataset_metric.size
        metrics.dataset_name = dataset_metric.name
        sparse_features = dataset_metric.sparse_features
        metrics.sparse_item_count = sparse_features.item_count
        metrics.sparse_features = ",".join(sparse_features.feature_names)
        metrics.sparse_feature_groups = ",".join(
            [str(i) for i in sparse_features.feature_groups]
        )
        metrics.sparse_feature_shapes = ",".join(
            [str(i) for i in sparse_features.feature_shapes]
        )
        metrics.dense_features = ",".join(
            dataset_metric.dense_features.feature_names
        )
        metrics.dense_feature_shapes = ",".join(
            [str(i) for i in dataset_metric.dense_features.feature_shapes]
        )
        metrics.storage_size = dataset_metric.storage_size
        return self.report_metrics(job_metrics)

    def report_model_feature(self, job_meta, tensor_stats, op_stats):
        job_metrics = init_job_metrics_message(job_meta)
        job_metrics.metrics_type = easydl_pb2.MetricsType.Model_Feature
        metrics = job_metrics.model_feature
        metrics.variable_count = tensor_stats.variable_count
        metrics.total_variable_size = tensor_stats.total_variable_size
        metrics.max_variable_size = tensor_stats.max_variable_size
        metrics.kv_embedding_dims.extend(tensor_stats.kv_embedding_dims)
        metrics.tensor_alloc_bytes.update(tensor_stats.tensor_alloc_bytes)
        metrics.op_count = op_stats.op_count
        metrics.update_op_count = op_stats.update_op_count
        metrics.read_op_count = op_stats.read_op_count
        metrics.input_fetch_dur = op_stats.input_fetch_dur
        metrics.flops = op_stats.flops
        metrics.recv_op_count = op_stats.recv_op_count
        return self.report_metrics(job_metrics)

    def report_node_runtime_stats(self, job_meta, runtime_metric):
        job_metrics = init_job_metrics_message(job_meta)
        job_metrics.metrics_type = easydl_pb2.MetricsType.Runtime_Info
        metrics = job_metrics.runtime_info
        metrics.global_step = runtime_metric.global_step
        metrics.time_stamp = runtime_metric.timestamp
        metrics.speed = runtime_metric.speed
        for pod in runtime_metric.running_nodes:
            pod_meta = easydl_pb2.PodMeta()
            pod_meta.pod_name = pod.name
            pod_meta.mem_usage = pod.used_resource.memory
            pod_meta.cpu_usage = pod.used_resource.cpu
            metrics.running_pods.append(pod_meta)
        return self.report_metrics(job_metrics)

    def get_optimization_plan(
        self,
        job_uuid,
        stage,
        opt_retriever,
        config={},
        processor=None,
        job_resource={},
    ):
        """Get optimization plan from Brain service.
        Args:
            job_uuid: the UUID of k8s training object.
            job_resource: Dict like `
            {
                'ps': {'count': 10, 'memory': 8589934592, 'cpu': 10},
                'worker': {'count': 10, 'memory': 8589934592, 'cpu': 10}
            }
        """
        if processor is None:
            processor = OPTIMIZE_PROCESSOR
        request = easydl_pb2.OptimizeRequest()
        request.type = stage
        request.config.optimizer_config_retriever = opt_retriever
        request.config.data_store = DATA_STORE
        request.config.brain_processor = processor
        for key, value in config.items():
            request.config.customized_config[key] = str(value)
        request.jobs.add()
        job_meta = request.jobs[0]
        job_meta.uid = job_uuid

        for task_group, resource_conf in job_resource.items():
            group_resource = job_meta.resource.task_group_resources[task_group]
            group_resource.count = resource_conf.get("count", 0)
            group_resource.resource.cpu = resource_conf.get("cpu", 0)
            group_resource.resource.memory = resource_conf.get("memory", 0)
        return self.request_optimization(request)

    def get_oom_resource_plan(
        self,
        oom_pods,
        job_uuid,
        stage,
        opt_retriever,
        config={},
        processor=None,
    ):
        if processor is None:
            processor = OPTIMIZE_PROCESSOR
        request = easydl_pb2.OptimizeRequest()
        request.type = stage
        request.config.optimizer_config_retriever = opt_retriever
        request.config.data_store = DATA_STORE
        request.config.brain_processor = OPTIMIZE_PROCESSOR
        for key, value in config.items():
            request.config.customized_config[key] = value
        request.jobs.add()
        job = request.jobs[0]
        job.uid = job_uuid
        for pod_name in oom_pods:
            job.state.pods[pod_name].is_oom = True
            job.state.pods[pod_name].name = pod_name
        return self.request_optimization(request)

    def report_job_exit_reason(self, job_meta, reason):
        job_metrics = init_job_metrics_message(job_meta)
        job_metrics.metrics_type = easydl_pb2.MetricsType.Job_Exit_Reason
        job_metrics.job_exit_reason = reason
        return self.report_metrics(job_metrics)

    @catch_exception
    def get_config(self, config_key="", group_key="default"):
        request = easydl_pb2.ConfigRequest()
        request.config_key = config_key
        request.group_key = group_key
        if self._administer_stub:
            response = self._administer_stub.get_config(request)
            if response.response.success:
                logger.info(
                    f"get config {group_key}:{config_key}:"
                    f" {response.config_values}"
                )
                if len(config_key) > 0:
                    return response.config_values[config_key]
                confs: Dict[str, str] = {}
                for k, v in response.config_values.items():
                    confs[k] = str(v)
                return confs
        return None

    def customized_request(self, request_type, data):
        request = easydl_pb2.CustomizedRequest()
        request.type = request_type
        for k, v in data.items():
            request.customized_data[k] = str(v)

        try:
            response = self._processor_stub.customized(request)
            if not response.success:
                logger.error(f"fail to executed customized request: {request}")
        except Exception as e:
            logger.warning(f"Customize request got error: {str(e)}")


def build_easydl_client(brain_admin_server_addr, brain_opt_server_addr):
    """Build a client of the EasyDL server.

    Example:
        ```
        import os
        os.environ["EASYDL_BRAIN_ADMINISTER_ADDR"] = "xxx"
        client = build_easydl_client()
        ```
    """
    admin_channel, processor_channel = build_easydl_channel(
        brain_admin_server_addr, brain_opt_server_addr
    )
    return EasydlClient(admin_channel, processor_channel)


def build_easydl_channel(brain_admin_server_addr, brain_opt_server_addr):
    easydl_administer_addr = os.getenv(
        "EASYDL_BRAIN_ADMINISTER_ADDR", EASYDL_BRAIN_ADMINISTER_ADDR
    )
    if brain_admin_server_addr:
        easydl_administer_addr = brain_admin_server_addr
    administer_channel = build_channel(easydl_administer_addr)

    easydl_processor_addr = os.getenv(
        "EASYDL_BRAIN_PROCESSOR_ADDR", EASYDL_BRAIN_PROCESSOR_ADDR
    )
    if brain_opt_server_addr:
        easydl_processor_addr = brain_opt_server_addr
    opt_channel = build_channel(easydl_processor_addr)
    return administer_channel, opt_channel


class GlobalEasydlClient(object):
    EASYDL_CLIENT = EasydlClient(None, None)

    @classmethod
    def update_client(cls, brain_admin_server_addr, brain_opt_server_addr):
        admin_channel, opt_channel = build_easydl_channel(
            brain_admin_server_addr, brain_opt_server_addr
        )
        cls.EASYDL_CLIENT.initialize_stub(admin_channel, opt_channel)
