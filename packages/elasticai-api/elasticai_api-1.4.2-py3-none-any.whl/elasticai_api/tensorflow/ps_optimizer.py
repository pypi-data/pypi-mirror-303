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

import tensorflow as tf
from tensorflow.python.framework import ops
from tensorflow.python.training.optimizer import Optimizer


def transfer_grad_with_bf16_if_needed(grad, var):
    """If grad and var are in different devices, use bfloat16
    for grad transfer between devices.
    """
    if grad is None:
        return grad
    if isinstance(grad, tf.IndexedSlices):
        if grad.values.device == var.device:
            return grad
        with ops.colocate_with(grad.values):
            g16 = tf.cast(grad.values, tf.bfloat16)
        with ops.colocate_with(var):
            g32 = tf.cast(g16, tf.float32)
            new_g = tf.IndexedSlices(values=g32, indices=grad.indices)
        return new_g
    if grad.device == var.device:
        return grad
    with ops.colocate_with(grad):
        g16 = tf.cast(grad, tf.bfloat16)
    with ops.colocate_with(var):
        g32 = tf.cast(g16, tf.float32)
    return g32


def encode_grad_use_bf16(grads_and_vars):
    """Use bfloat16 for gradients transfer from worker to PS"""
    grads_and_vars = tuple(grads_and_vars)
    grad_list = []
    var_list = []
    for g, v in grads_and_vars:
        g = transfer_grad_with_bf16_if_needed(g, v)
        var_list.append(v)
        grad_list.append(g)
    grads_and_vars = zip(tuple(grad_list), tuple(var_list))
    return grads_and_vars


class PSOptimizer(Optimizer):
    """Construct a new optimizer to support different training optimization
    methods in PS-based distributed training. This optimizer uses another
    optimizer under the hood for computing gradient values on workers and
    applying gradient updates on PS.
    Supported training optimization methods:
      - use bfloat16 for gradients transfer from worker to PS to reduce data
        communication.
    """

    def __init__(
        self,
        optimizer,
        use_bf16_for_grad=True,
    ):
        """
        Args
        optimizer: a TensorFlow optimizer used to computing gradients and
            applying gradients updates.
        use_bf16_for_grad: if True, encode gradients with bfloat16 for data
            transfer between worker and PS to reduce data communication.
        """
        self._optimizer = optimizer
        self._use_bf16_for_grad = use_bf16_for_grad

    def compute_gradients(self, *args, **kwargs):
        return self._optimizer.compute_gradients(*args, **kwargs)

    def apply_gradients(self, grads_and_vars, global_step=None, name=None):
        if self._use_bf16_for_grad:
            grads_and_vars = encode_grad_use_bf16(grads_and_vars)
        return self._optimizer.apply_gradients(
            grads_and_vars, global_step=global_step, name=name
        )

    def get_slot(self, *args, **kwargs):
        """Calls this same method on the underlying optimizer."""
        return self._optimizer.get_slot(*args, **kwargs)

    def get_slot_names(self, *args, **kwargs):
        """Calls this same method on the underlying optimizer."""
        return self._optimizer.get_slot_names(*args, **kwargs)

    def variables(self, *args, **kwargs):
        """Calls this same method on the underlying optimizer."""
        return self._optimizer.variables(*args, **kwargs)
