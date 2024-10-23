"""Save state_dict of the training model during training.

Parameters:
    filename_prefix (str): Prefix of the filename to save the state_dict of the model.
    epoch_interval (int): Interval of epochs to save the state_dict of the model.
"""

import logging
import os
import torch
from .plugin_base import PluginBase

logger = logging.getLogger(__name__)


class Plugin(PluginBase):
    def __init__(self, filename_prefix='model_snapshot_', epoch_interval=1):
        self._filename_prefix = filename_prefix
        self._epoch_interval = epoch_interval

    def on_train_epoch_end(self, trainer, model, epoch_index):
        if (epoch_index + 1) % self._epoch_interval == 0:
            filename = f'{self._filename_prefix}{epoch_index}.pth'
            logger.info(f"Saving state_dict of the model to {filename}")
            torch.save(model.state_dict(), filename)
            file_size = os.stat(filename).st_size
            logger.info(f"Saved state_dict of the model to {filename}. File size: {file_size} bytes.")
