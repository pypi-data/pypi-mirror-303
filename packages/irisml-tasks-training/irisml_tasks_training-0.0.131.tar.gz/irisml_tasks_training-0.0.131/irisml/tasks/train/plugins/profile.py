"""Pluging to profile model training and inference.

If you encounter the following error on WSL, visit https://github.com/pytorch/pytorch/issues/99615
"function cbapi->getCuptiStatus() failed with error CUPTI_ERROR_NOT_INITIALIZED"

Args:
    num_iters (int): Number of iterations to profile.
    trace_filename_prefix (str): Prefix for the trace filename. If None, the trace will not be saved.
"""

import datetime
import logging
import pathlib
import torch
from .plugin_base import PluginBase

logger = logging.getLogger(__name__)


class Plugin(PluginBase):
    def __init__(self, num_iters=10, trace_filename_prefix='trace'):
        self._num_iters = num_iters
        self._trace_filename_prefix = trace_filename_prefix
        self._profiler = None

    def on_train_start(self, trainer, model):
        self._start()

    def on_train_batch_end(self, trainer, model, loss, batch, batch_index):
        if self._profiler is not None and batch_index >= self._num_iters - 1:
            self._stop()

    def on_train_end(self, trainer, model):
        self._stop()

    def on_prediction_start(self, trainer, model):
        self._start()

    def on_prediction_batch_end(self, trainer, model, batch, batch_index):
        if self._profiler is not None and batch_index >= self._num_iters - 1:
            self._stop()

    def on_prediction_end(self, trainer, model):
        self._stop()

    def _start(self):
        logger.info(f"Starting profiling for {self._num_iters} iterations")
        assert self._profiler is None
        self._profiler = torch.profiler.profile(activities=[torch.profiler.ProfilerActivity.CPU, torch.profiler.ProfilerActivity.CUDA])
        self._profiler.__enter__()

    def _stop(self):
        if self._profiler is not None:
            self._profiler.__exit__(None, None, None)
            if self._trace_filename_prefix:
                filename = f'{self._trace_filename_prefix}_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
                pathlib.Path(filename).parent.mkdir(parents=True, exist_ok=True)
                logger.info(f"Exporting trace to {filename}")
                self._profiler.export_chrome_trace(filename)
            self._profiler = None
