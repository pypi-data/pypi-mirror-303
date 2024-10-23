"""Call set_epoch method of dataset before each epoch.

This plugin is useful when you want to change the behavior of the dataset based on the epoch index.
"""
import logging
from .plugin_base import PluginBase

logger = logging.getLogger(__name__)


class Plugin(PluginBase):
    def on_train_start(self, trainer, model):
        if hasattr(trainer.train_dataloader.dataset, "set_epoch"):
            logger.info("Dataset has set_epoch method. This plugin will call it before each epoch.")
        else:
            logger.warning("Dataset does not have set_epoch method. This plugin will not work.")

    def on_train_epoch_start(self, trainer, model, epoch_index):
        if hasattr(trainer.train_dataloader.dataset, "set_epoch"):
            trainer.train_dataloader.dataset.set_epoch(epoch_index)
        return True
