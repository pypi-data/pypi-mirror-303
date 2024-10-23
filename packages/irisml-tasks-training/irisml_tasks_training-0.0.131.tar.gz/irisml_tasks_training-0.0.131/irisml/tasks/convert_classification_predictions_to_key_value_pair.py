import dataclasses
import logging
import typing
import irisml.core
import torch

logger = logging.getLogger(__name__)


class Task(irisml.core.TaskBase):
    """Convert classification prediction results to Key Value Pair format.

    Inputs:
        predictions (torch.Tensor): The classification prediction results. Shape (N, num_classes).
        class_names (list[str]): The class names.

    Config:
        field_name (str): The field name to store the classification results.
        task_type (str): The task type. Either 'classification_multiclass' or 'classification_multilabel'. Default is 'classification_multiclass'.
        prob_threshold (float, optional): The probability threshold to consider a class as positive for classification_multilabel.
            If None, the class with the highest probability is considered as positive.

    Outputs:
        key_value_pairs (list[dict[str, dict]]): predictions in KVP format.
    """
    VERSION = '0.1.0'

    VALUE_KEY = 'value'  # A constant in Key Value Pair dataset, which might be changed in the future.

    @dataclasses.dataclass
    class Inputs:
        predictions: torch.Tensor
        class_names: list[str]

    @dataclasses.dataclass
    class Config:
        field_name: str
        task_type: typing.Literal['classification_multiclass', 'classification_multilabel'] = 'classification_multiclass'
        prob_threshold: float | None = None

    @dataclasses.dataclass
    class Outputs:
        key_value_pairs: list[dict[str, dict]]

    def execute(self, inputs):
        if self.config.task_type != 'classification_multilabel' and self.config.prob_threshold is not None:
            raise ValueError('prob_threshold is only used for classification_multilabel task type.')

        if self.config.task_type == 'classification_multiclass':
            positive_classes = torch.argmax(inputs.predictions, dim=-1)
            result = [{self.config.field_name: {self.VALUE_KEY: inputs.class_names[p]}} for p in positive_classes.tolist()]
        elif self.config.task_type == 'classification_multilabel':
            if self.config.prob_threshold is None:
                positive_classes = torch.argmax(inputs.predictions, dim=-1)
                result = [{self.config.field_name: {self.VALUE_KEY: [{self.VALUE_KEY: inputs.class_names[p]}]}} for p in positive_classes.tolist()]
            else:
                positive_classes = torch.where(inputs.predictions >= self.config.prob_threshold, torch.tensor(1), torch.tensor(0))
                result = [{self.config.field_name: {self.VALUE_KEY: [{self.VALUE_KEY: inputs.class_names[i]} for i, p in enumerate(p_classes.tolist()) if p == 1]}} for p_classes in positive_classes]

        return self.Outputs(key_value_pairs=result)

    def dry_run(self, inputs):
        return self.execute(inputs)
