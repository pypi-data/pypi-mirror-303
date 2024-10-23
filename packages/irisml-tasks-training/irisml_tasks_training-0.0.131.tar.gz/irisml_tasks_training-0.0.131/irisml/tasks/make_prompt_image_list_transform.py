import dataclasses
import typing
import PIL.Image
import torch
import irisml.core


class Task(irisml.core.TaskBase):
    """Make a transform function for images and return the original prompt.
    Given an image transform T, ([im1,im2,im3], text) is transformed to ([T(im1), T(im2), T(im3)], text)

    The interface of the transform function is:
    - Input: Tuple[List[PIL.Image.Image], str]
    - Output: Tuple[List[torch.Tensor], str]
    """

    VERSION = '0.1.0'

    @dataclasses.dataclass
    class Inputs:
        image_transform: typing.Callable[[PIL.Image.Image], torch.Tensor]

    @dataclasses.dataclass
    class Outputs:
        transform: typing.Callable

    def execute(self, inputs):
        transform = ImagesTransform(inputs.image_transform)
        return self.Outputs(transform=transform)

    def dry_run(self, inputs):
        return self.execute(inputs)


class ImagesTransform:
    def __init__(self, image_transform):
        self._image_transform = image_transform

    def __call__(self, inputs, targets):
        images, text = inputs
        tensors = [self._image_transform(image) for image in images]
        return (text, tensors), targets
