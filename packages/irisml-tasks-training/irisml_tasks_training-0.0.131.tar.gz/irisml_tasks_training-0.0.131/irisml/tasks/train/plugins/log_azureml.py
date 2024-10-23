"""Log metrics on Azure ML.

This plugin requires mlflow and azureml-mlflow packages. Use "azureml" extra dependency to install them.
```
pip install irisml-tasks-training[azureml]
```

"""
import logging
import mlflow
from .plugin_base import PluginBase

logger = logging.getLogger(__name__)


class Plugin(PluginBase):
    def on_train_start(self, trainer, model):
        logger.info("Enabling MLflow autologging")
        mlflow.autolog(log_models=False, exclusive=True)

    def on_train_end(self, trainer, model):
        logger.info("Disabling MLflow autologging")
        mlflow.autolog(disable=True)

    def on_train_backward_start(self, trainer, model, loss):
        # Get a loss in this method, because other plugins may change it.
        mlflow.log_metric("train_loss", float(loss.item()))
        return loss

    def on_train_batch_end(self, trainer, model, loss, batch, batch_index):
        for i, lr in enumerate(g['lr'] for g in trainer.optimizer.param_groups):
            mlflow.log_metric(f"lr{i}", float(lr))

    def on_validation_batch_end(self, trainer, model, loss, batch, batch_index):
        mlflow.log_metric("val_loss", float(loss.item()))
