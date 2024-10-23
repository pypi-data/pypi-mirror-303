"""Plugin to debug training process.

Args:
    level (int): Log level. 0=info, 1=debug, 2=verbose. Default: 0.
"""
import logging
from .plugin_base import PluginBase

logger = logging.getLogger(__name__)


class Plugin(PluginBase):
    def __init__(self, level=0):
        self._level = level
        self._batch_loss = 0

    def on_train_backward_start(self, trainer, model, loss):
        # Get a loss in this method, because other plugins may change it.
        self._batch_loss = float(loss.item())
        return loss

    def on_train_batch_end(self, trainer, model, loss, batch, batch_index):
        lrs = [g['lr'] for g in trainer.optimizer.param_groups]
        if batch_index % 100 == 0:
            self._log0(f"Batch {batch_index} loss: {self._batch_loss}, lr: {lrs}")
        else:
            self._log2(f"Batch {batch_index} loss: {self._batch_loss}, lr: {lrs}")

    def _log0(self, msg):
        if self._level >= 0:
            logger.info(msg)

    def _log1(self, msg):
        if self._level >= 1:
            logger.info(msg)

    def _log2(self, msg):
        if self._level >= 2:
            logger.info(msg)
