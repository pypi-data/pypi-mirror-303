import dataclasses
import logging
import typing
import torch.utils.data
import irisml.core

logger = logging.getLogger(__name__)


def _identity_prompt_generator(label: str) -> list[str]:
    return [label]


class Task(irisml.core.TaskBase):
    """Create a classification prompt dataset.

    This task creates a dataset for classification prompts. Each example in the dataset consists of a text and a label. The text is generated from a prompt generator function,
    and the label is an integer index of the class name.

    Inputs:
        class_names (list[str]): A list of class names.
        prompt_generator (Callable[[str], list[str]], optional): A function that generates prompts for each class. If not provided, the default prompt generator is used.
    """
    VERSION = '0.2.0'

    @dataclasses.dataclass
    class Inputs:
        class_names: list[str]
        prompt_generator: typing.Callable[[str], list[str]] | None = None

    @dataclasses.dataclass
    class Outputs:
        dataset: torch.utils.data.Dataset

    def execute(self, inputs):
        prompt_generator = inputs.prompt_generator or _identity_prompt_generator
        text_lists = [(t, i) for i, label in enumerate(inputs.class_names) for t in prompt_generator(label)]
        logger.debug(f"Created a text dataset. The number of examples: {len(text_lists)}. The number of classes: {len(inputs.class_names)}")
        return self.Outputs(TextListDataset(text_lists))

    def dry_run(self, inputs):
        return self.execute(inputs)


class TextListDataset(torch.utils.data.Dataset):
    def __init__(self, text_list: list[tuple[str, int]]):
        self._data = text_list

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]
