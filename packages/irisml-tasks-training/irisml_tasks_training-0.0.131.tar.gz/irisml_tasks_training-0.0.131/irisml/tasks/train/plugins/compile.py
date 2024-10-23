"""Compile the model module using torch.compile.

Args:
    backend ('inductor' or 'ipex'): The backend for torch.compile().
    dtype ('fp32' or 'bf16'): The dtype for IPEX backend.
"""
import logging
import torch
from .plugin_base import PluginBase

logger = logging.getLogger(__name__)


class Plugin(PluginBase):
    def __init__(self, backend='inductor', dtype='fp32'):
        if backend not in ['eager', 'inductor', 'ipex']:
            raise ValueError(f"Unsupported torch.compile backend '{backend}'")
        if dtype not in ['fp32', 'bf16']:
            raise ValueError(f"Unsupported dtype '{dtype}'")
        self._backend = backend
        self._dtype = dtype

    def on_train_start(self, trainer, model):
        logger.info(f"Compiling the model module using backend '{self._backend}'")
        self._original_model = model
        if self._backend == 'ipex':
            logger.debug("Loading intel_extension_for_pytorch")
            # Load intel_extension_for_pytorch to enable IPEX backend
            try:
                import intel_extension_for_pytorch  # noqa: F401
            except ImportError:
                logger.error("intel_extension_for_pytorch is not installed. Please install it by running 'pip install intel-extension-for-pytorch'")
                raise

            # weights_prepack is disabled since ops are well supported in ipex backend.
            dtype = {'fp32': torch.float32, 'bf16': torch.bfloat16}
            model = intel_extension_for_pytorch.optimize(model, weights_prepack=False, dtype=dtype)
            return torch.compile(model, backend=self._backend)
        elif self._backend == 'inductor':
            return torch.compile(model, backend=self._backend, mode='max-autotune')
        else:
            return torch.compile(model, backend=self._backend)

    def on_train_end(self, trainer, model):
        # Move the compiled model back to CPU. Otherwise, the model will stay on GPU and cause memory leak.
        model.to('cpu')

        # The OptimizedModule shares the same state_dict with the original model.
        model = self._original_model
        del self._original_model
        return model

    def on_prediction_start(self, trainer, model):
        return self.on_train_start(trainer, model)

    def on_prediction_end(self, trainer, model):
        return self.on_train_end(trainer, model)
