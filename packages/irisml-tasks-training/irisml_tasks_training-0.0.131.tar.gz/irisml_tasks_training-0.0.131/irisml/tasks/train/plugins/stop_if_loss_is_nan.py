"""Stop the training if the loss is NaN."""
import logging
import math
import torch
import torch.distributed
from .plugin_base import PluginBase

logger = logging.getLogger(__name__)


class Plugin(PluginBase):
    def __init__(self, patience=5):
        if patience < 1:
            raise ValueError("patience must be a positive integer.")
        self._patience = patience

    def on_train_start(self, trainer, model):
        self._counter = 0

    def on_train_batch_end(self, trainer, model, loss, batch, batch_index):
        if math.isnan(loss):
            self._counter += 1
        else:
            self._counter = 0

        if 0 < self._counter <= self._patience:
            logger.debug(f"Loss is NaN for {self._counter} consecutive batches.")

    def on_train_epoch_start(self, trainer, model, epoch_index):
        if torch.distributed.is_initialized():
            shared_counter = torch.tensor(self._counter).to(trainer.device)
            torch.distributed.broadcast(shared_counter, 0)
            self._counter = shared_counter.item()

        if self._counter > self._patience:
            logger.warning(f"Loss is NaN for {self._counter} consecutive batches. Stopping the training.")
            return False

        return True
