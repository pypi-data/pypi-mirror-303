"""Plugin to record CUDA memory snapshots.

See https://pytorch.org/docs/stable/torch_cuda_memory.html for the details.
"""
import logging
import pathlib
import torch.cuda.memory
from .plugin_base import PluginBase

logger = logging.getLogger(__name__)


class Plugin(PluginBase):
    def __init__(self, iter_count=5, path='outputs/memory_snapshot.pkl'):
        self._path = pathlib.Path(path)
        self._iter_count = iter_count
        self._done = False
        self._recording = False

    def on_train_start(self, trainer, model):
        if torch.distributed.is_initialized() and torch.distributed.get_rank() != 0:
            logger.debug(f"Skipping memory recording on rank {torch.distributed.get_rank()}")
            return

        torch.cuda.memory._record_memory_history()
        logger.info("Recording CUDA memory history")
        self._recording = True

    def on_train_end(self, trainer, model):
        torch.cuda.memory._record_memory_history(enabled=None)

    def on_train_batch_end(self, trainer, model, loss, batch, batch_index):
        if self._recording and batch_index == self._iter_count:
            torch.cuda.memory._dump_snapshot(self._path)
            logger.info(f"Memory snapshot saved to {self._path}")
            # Disable memory recording since it consumes significant amount of CPU memory
            torch.cuda.memory._record_memory_history(enabled=None)
            self._recording = False
