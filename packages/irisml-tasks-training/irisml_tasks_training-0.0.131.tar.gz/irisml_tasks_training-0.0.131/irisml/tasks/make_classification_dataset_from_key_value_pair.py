import dataclasses
import logging
import typing
import irisml.core
import torch.utils.data

logger = logging.getLogger(__name__)


class Task(irisml.core.TaskBase):
    """Convert Key Value Pair dataset to Classification dataset

    This task extracts a single classification from a Key Value Pair dataset and converts it to a Classification dataset.

    Config:
        field_name (str): The schema field name to convert to Classification dataset.

    Inputs:
        dataset (Dataset): Key Value Pair dataset. It must contain `field_name` field.
        schema: (dict): Key Value Pair dataset schema.

    Outputs:
        dataset (Dataset): classification dataset
        task_type (Literal): 'classification_multiclass' or 'classifictaion_multilabel'
        class_names (list[str]): A list of class names.
        num_classes (int): The number of classes.
    """
    VERSION = '0.1.0'

    @dataclasses.dataclass
    class Inputs:
        dataset: torch.utils.data.Dataset
        schema: dict

    @dataclasses.dataclass
    class Config:
        field_name: str

    @dataclasses.dataclass
    class Outputs:
        dataset: torch.utils.data.Dataset
        task_type: typing.Literal['classification_multiclass', 'classification_multilabel']
        class_names: list[str]
        num_classes: int

    def execute(self, inputs):
        field_schema = inputs.schema['fieldSchema'][self.config.field_name]
        if field_schema['type'] == 'string':
            task_type = 'classification_multiclass'
            class_names = list(field_schema['classes'].keys())
        elif field_schema['type'] == 'array':
            task_type = 'classification_multilabel'
            class_names = list(field_schema['items']['classes'].keys())
        else:
            raise ValueError('Invalid field type.')

        logger.info(f"Converting Key Value Pair dataset to Classification dataset for field '{self.config.field_name}'.")

        dataset = ClassificationFromKeyValuePairDataset(inputs.dataset, self.config.field_name, task_type, class_names)
        return self.Outputs(dataset=dataset, task_type=task_type, class_names=class_names, num_classes=len(class_names))

    def dry_run(self, inputs):
        return self.execute(inputs)


class ClassificationFromKeyValuePairDataset(torch.utils.data.Dataset):
    VALUE_KEY = 'value'  # Might be changed in the future.

    def __init__(self, dataset: torch.utils.data.Dataset, field_name: str, task_type: str, class_names: list[str]):
        assert task_type in ('classification_multiclass', 'classification_multilabel')
        self._dataset = dataset
        self._field_name = field_name
        self._task_type = task_type
        self._class_names = class_names

    def __len__(self):
        return len(self._dataset)

    def __getitem__(self, idx):
        inputs, targets = self._dataset[idx]
        _, images = inputs
        if len(images) != 1:
            logger.warning(f"Dataset[{idx}] has {len(images)} images. Only the first image is used.")
        image = images[0][0]

        field = targets[self._field_name]
        targets_tensor = None
        if self._task_type == 'classification_multiclass':
            targets_tensor = torch.tensor(self._class_names.index(field[self.VALUE_KEY]), dtype=torch.long)
        elif self._task_type == 'classification_multilabel':
            targets_tensor = torch.zeros(len(self._class_names), dtype=torch.float)
            for c in field[self.VALUE_KEY]:
                targets_tensor[self._class_names.index(c[self.VALUE_KEY])] = 1
        else:
            raise ValueError('Invalid task type.')
        return image, targets_tensor
