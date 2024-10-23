"""Enable deterministic training for PyTorch models.

Note that there will be a performance penalty for enabling this feature.
"""
import os
import torch
from .plugin_base import PluginBase


class Plugin(PluginBase):
    def __init__(self):
        self._original_cudnn_benchmark = torch.backends.cudnn.benchmark
        self._original_cudnn_deterministic = torch.backends.cudnn.deterministic
        self._original_cublas_workspace_config = os.getenv('CUBLAS_WORKSPACE_CONFIG')

    def on_train_start(self, trainer, model):
        self._enable_deterministic()

    def on_train_end(self, trainer, model):
        self._disable_deterministic()

    def on_prediction_start(self, trainer, model):
        self._enable_deterministic()

    def on_prediction_end(self, trainer, model):
        self._disable_deterministic()

    def _enable_deterministic(self):
        torch.backends.cudnn.benchmark = False
        torch.backends.cudnn.deterministic = True
        torch.use_deterministic_algorithms(True, warn_only=True)
        os.environ['CUBLAS_WORKSPACE_CONFIG'] = ':4096:8'

    def _disable_deterministic(self):
        torch.backends.cudnn.benchmark = self._original_cudnn_benchmark
        torch.backends.cudnn.deterministic = self._original_cudnn_deterministic
        torch.use_deterministic_algorithms(False)
        if self._original_cublas_workspace_config is not None:
            os.environ['CUBLAS_WORKSPACE_CONFIG'] = self._original_cublas_workspace_config
        else:
            del os.environ['CUBLAS_WORKSPACE_CONFIG']
