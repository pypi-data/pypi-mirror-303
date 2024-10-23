import dataclasses
import json
import logging
import pathlib
import typing
import PIL.Image
import torch
import torch.utils.data
import irisml.core

logger = logging.getLogger(__name__)


class Task(irisml.core.TaskBase):
    """Create a dataset with a single image.

    Inputs:
        image_metadata (str): A string of ocr metadata (key_value_pair datasets only). If it is valid JSON, it is used as-is.
                              Otherwise, it is converted into a dictionary with default_metadata_key as the key and image_metadata as the value.
    Config:
        path (Path): Path to the image file.
        task_type: Type of the task. Supported values are 'classification_multiclass', 'object_detection', and 'key_value_pair'.
        default_metadata_key (str): The default metadata key to be used for the metadata dictionary when the image_metadata passed in is not None and is not a valid dict.
    """
    VERSION = '0.3.1'
    CACHE_ENABLED = False

    @dataclasses.dataclass
    class Inputs:
        image_metadata: str | None = None

    @dataclasses.dataclass
    class Config:
        path: pathlib.Path
        task_type: typing.Literal['classification_multiclass', 'object_detection', 'key_value_pair']
        default_metadata_key: str = 'metadata'

    @dataclasses.dataclass
    class Outputs:
        dataset: torch.utils.data.Dataset

    def execute(self, inputs):
        return self.Outputs(SingleImageDataset(self.config.path, self.config.task_type, inputs.image_metadata, self.config.default_metadata_key))


class SingleImageDataset(torch.utils.data.Dataset):
    def __init__(self, path: pathlib.Path, task_type: str, image_metadata: str, default_metadata_key: str):
        self._path = path
        self._task_type = task_type
        if task_type != 'key_value_pair' and image_metadata is not None:
            raise ValueError(f"task_type must be 'key_value_pair' if image_metadata is supplied, but got task_type='{task_type}'")
        self._image_metadata = image_metadata
        self._default_metadata_key = default_metadata_key

    def __len__(self):
        return 1

    def __getitem__(self, index):
        if index != 0:
            raise IndexError('Index out of range')

        if self._path.exists():
            logger.info(f"Loading image: {self._path}")
            with PIL.Image.open(self._path) as image:
                # If image is truncated, return UnidentifiedImageError instead of a generic OS Error
                # so that the caller can correctly identify the cause.
                try:
                    image.load()
                except OSError as e:
                    raise PIL.UnidentifiedImageError(str(e))

                image = image.convert('RGB')
        else:
            logger.error(f"File not found: {self._path}. Using a dummy image.")
            image = PIL.Image.new('RGB', (224, 224))

        if self._task_type == 'classification_multiclass':
            return image, torch.tensor(0, dtype=torch.long)
        elif self._task_type == 'object_detection':
            return image, torch.zeros((0, 5), dtype=torch.float32)
        elif self._task_type == 'key_value_pair':
            formatted_metadata = None
            if self._image_metadata:
                try:
                    image_metadata = json.loads(self._image_metadata)
                    if isinstance(image_metadata, dict):
                        formatted_metadata = image_metadata
                except json.JSONDecodeError:
                    formatted_metadata = {self._default_metadata_key: self._image_metadata}
            return (None, [(image, formatted_metadata)]), None
        else:
            raise ValueError(f'Unsupported task type: {self._task_type}')
