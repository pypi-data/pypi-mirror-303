import dataclasses
from typing import Callable, Optional
import PIL.Image
import torch
import irisml.core


class Task(irisml.core.TaskBase):
    """Make phrase grounding image transform.

    The input of the tramsform function is:
        ((caption, image), [[((span_start, span_end), bboxes)]]

    image_transform is applied to the image, and text_transform is applied to the caption.
    """
    VERSION = '0.1.0'

    @dataclasses.dataclass
    class Inputs:
        image_transform: Optional[Callable[[PIL.Image.Image], torch.Tensor]] = None
        text_transform: Optional[Callable[[str], str]] = None

    @dataclasses.dataclass
    class Outputs:
        transform: Callable

    def execute(self, inputs):
        transform = Transform(inputs.image_transform, inputs.text_transform)
        return self.Outputs(transform=transform)


class Transform:
    def __init__(self, image_transform, text_transform):
        self._image_transform = image_transform
        self._text_transform = text_transform

    def __call__(self, inputs, targets):
        caption, image = inputs
        if self._image_transform is not None:
            image = self._image_transform(image)

        if self._text_transform is not None:
            caption = self._text_transform(caption)

        return (caption, image), targets
