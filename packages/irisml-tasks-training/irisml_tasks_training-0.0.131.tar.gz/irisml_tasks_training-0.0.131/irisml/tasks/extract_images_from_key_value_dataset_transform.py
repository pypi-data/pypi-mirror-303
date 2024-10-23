"""
Extracts images from a key-value dataset and applies a transformation to them.
"""
import dataclasses
import logging
import typing

import PIL.Image
import torch

import irisml.core

logger = logging.getLogger(__name__)


class Task(irisml.core.TaskBase):
    """
    Extracts images from a key-value dataset and applies a transformation to them.
    """

    VERSION = '0.1.0'

    @dataclasses.dataclass
    class Inputs:
        image_transform: typing.Callable[[PIL.Image.Image], torch.Tensor]

    @dataclasses.dataclass
    class Outputs:
        transform: typing.Callable

    def execute(self, inputs):
        transform = ExtractImageFromKeyValueDatasetTransform(inputs.image_transform)
        return self.Outputs(transform=transform)

    def dry_run(self, inputs):
        return self.execute(inputs)


class ExtractImageFromKeyValueDatasetTransform:
    """Transform class for key-value-pair dataset training/inference.
    The transform accepts inputs, targets and returns transformed transformed_imgs, where inputs is tuple of text dict and list of (image, optional metadata dict) tuples

    Args:
        img_transform (callable): Image transform function
    """
    def __init__(self, img_transform):
        self._img_transform = img_transform

    def __call__(self, inputs, targets):
        assert len(inputs[1]) == 1, 'Only single image is supported'
        img = inputs[1][0][0]
        tensor = self._img_transform(img)
        return tensor, None
