"""
Injects image metadata to the key-value pair dataset.
"""
import dataclasses
import logging
import typing

import torch

import irisml.core

logger = logging.getLogger(__name__)


class Task(irisml.core.TaskBase):
    """
    Injects image metadata to the key-value pair dataset.
    """

    VERSION = '0.1.0'

    @dataclasses.dataclass
    class Inputs:
        dataset: torch.utils.data.Dataset
        image_metadata: typing.List[typing.Dict[str, str]]

    @dataclasses.dataclass
    class Outputs:
        dataset: torch.utils.data.Dataset

    def execute(self, inputs):
        return self.Outputs(dataset=Dataset(inputs.dataset, inputs.image_metadata))


class Dataset(torch.utils.data.Dataset):
    def __init__(self, dataset, image_metadata):
        # check if same length
        if len(dataset) != len(image_metadata):
            raise ValueError(f"Expected dataset and image_metadata to have the same length, but got {len(dataset)} and {len(image_metadata)}")
        self._image_metadata = image_metadata
        self._dataset = dataset

    def __len__(self):
        return len(self._dataset)

    def __getitem__(self, index):
        inputs, targets = self._dataset[index]

        if not isinstance(inputs, tuple):
            raise ValueError(f"Expected tuple of inputs, but got {type(inputs)}")
        if len(inputs) != 2:
            raise ValueError(f"Expected 2 inputs, but got {len(inputs)}")

        imgs_with_metadata = inputs[1]

        if not isinstance(imgs_with_metadata, list):
            raise ValueError(f"Expected list of images, but got {type(imgs_with_metadata)}")
        if len(imgs_with_metadata) != 1:
            raise ValueError(f"Expected 1 image, but got {len(imgs_with_metadata)}")
        if not isinstance(imgs_with_metadata[0], tuple):
            raise ValueError(f"Expected tuple of image and metadata, but got {type(imgs_with_metadata[0])}")

        new_image_metadata = self._image_metadata[index]
        image_metadata = imgs_with_metadata[0][1]
        if image_metadata is None:
            image_metadata = {}
        image_metadata = {**image_metadata, **new_image_metadata}
        inputs = (inputs[0], [(imgs_with_metadata[0][0], image_metadata)])
        return inputs, targets

    def get_targets(self, index):
        return self._dataset.get_targets(index)
