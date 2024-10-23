import dataclasses
import logging
import typing
import torch
import irisml.core

logger = logging.getLogger(__name__)


class Task(irisml.core.TaskBase):
    """Convert VQA dataset to image text classification dataset.

    This task consideres VQA question as text input and answer as class label.

    The expected VQA dataset format is (question, image), answer, where question is a string, image is a PIL image, and answer is a string.

    If class_names is given, it is used as class names. Otherwise, class names are extracted from the dataset.
    """
    VERSION = '0.2.0'

    @dataclasses.dataclass
    class Inputs:
        dataset: torch.utils.data.Dataset
        class_names: typing.Optional[typing.List[str]] = None

    @dataclasses.dataclass
    class Outputs:
        dataset: torch.utils.data.Dataset
        num_classes: int
        class_names: typing.List[str]

    def execute(self, inputs):
        # Verify the dataset is VQA dataset by checking the first data.
        if inputs.dataset:
            first_data = inputs.dataset[0]
            if not isinstance(first_data, (tuple, list)):
                raise ValueError(f"Unexpected dataset type: {type(first_data)}")
            if len(first_data) != 2:
                raise ValueError(f"Unexpected dataset length: {len(first_data)}")
            if not isinstance(first_data[0], (tuple, list)):
                raise ValueError(f"This task expects (text, image) tuple as dataset input, but got {type(first_data[0])}")
            if not isinstance(first_data[1], str):
                raise ValueError(f"This task expects string as target, but got {type(first_data[1])}")
        else:
            logger.warning("Empty dataset is given.")

        class_names = self._get_class_names(inputs.dataset)
        logger.debug(f"Extracted class_names from dataset. num_classes={len(class_names)} class_names={class_names}")

        if inputs.class_names:
            missing_class_names = set(class_names) - set(inputs.class_names)
            if missing_class_names:
                raise ValueError(f"Given class_names is missing some class names: {missing_class_names}")
            class_names = inputs.class_names
            logger.info(f"Using given class_names. num_classes={len(class_names)} class_names={class_names}")

        dataset = Dataset(inputs.dataset, class_names)
        logger.info(f"Converted dataset. num_classes={len(class_names)} num_samples={len(dataset)}")
        return self.Outputs(dataset=dataset, num_classes=len(class_names), class_names=class_names)

    def dry_run(self, inputs):
        return self.execute(inputs)

    def _get_class_names(self, dataset):
        answer_set = set()
        if hasattr(dataset, 'get_targets'):
            for i in range(len(dataset)):
                answer_set.add(dataset.get_targets(i))
        else:
            for _, answer in dataset:
                answer_set.add(answer)

        return sorted(list(answer_set))


class Dataset(torch.utils.data.Dataset):
    def __init__(self, dataset, class_names):
        self._class_names = class_names
        self._class_name_to_index = {class_name: i for i, class_name in enumerate(class_names)}
        self._dataset = dataset

    def __len__(self):
        return len(self._dataset)

    def __getitem__(self, index):
        (question, image), targets = self._dataset[index]
        assert isinstance(targets, str)
        assert targets in self._class_name_to_index
        class_id = torch.tensor(self._class_name_to_index[targets], dtype=torch.long)
        return (image, question), class_id

    def get_targets(self, index):
        if hasattr(self._dataset, 'get_targets'):
            targets = self._dataset.get_targets(index)
        else:
            _, targets = self._dataset[index]

        class_id = torch.tensor(self._class_name_to_index[targets], dtype=torch.long)
        return class_id
