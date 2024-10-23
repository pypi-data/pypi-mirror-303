import dataclasses
import math
import typing
import numpy
import PIL.Image
import torch
import irisml.core


class Task(irisml.core.TaskBase):
    """Create a transform that resizes an image to a resolution and rounds it to the nearest multiple of the resolution.

    Example:
        - Input: 1000x1000 image, resolution=32, max_input_size=640 -> 640x640 image
        - Input: 500x100 image, resolution=32, max_input_size=640 -> 640x128 image

    Config:
        max_input_size (int): The maximum size of the input image.
        resolution (int): The resolution to round the image to.
        padding (bool): Whether to pad the image to the resolution if it is not a multiple of the resolution.
    """
    VERSION = '1.0.0'

    @dataclasses.dataclass
    class Config:
        max_input_size: int
        resolution: int
        padding: bool = False
        task_type: typing.Literal['classification_multiclass', 'object_detection'] = 'object_detection'

    @dataclasses.dataclass
    class Outputs:
        transform: typing.Callable

    def execute(self, inputs):
        return self.Outputs(Transform(self.config.max_input_size, self.config.resolution, self.config.padding, self.config.task_type))

    def dry_run(self, inputs):
        return self.execute(inputs)


class Transform:
    def __init__(self, max_input_size, resolution, padding, task_type):
        self._max_input_size = max_input_size
        self._resolution = resolution
        self._padding = padding
        self._task_type = task_type

    def __call__(self, inputs: PIL.Image.Image, targets):
        assert isinstance(inputs, PIL.Image.Image)

        ratio = self._max_input_size / max(inputs.size)
        new_size = (int(inputs.size[0] * ratio), int(inputs.size[1] * ratio))

        rounded_new_size = (math.ceil(new_size[0] / self._resolution) * self._resolution,
                            math.ceil(new_size[1] / self._resolution) * self._resolution)

        if self._padding:
            resized = inputs.resize(new_size, PIL.Image.BILINEAR)
            image = torch.from_numpy(numpy.array(resized)).to(torch.float32).permute(2, 0, 1) / 255.0
            image_with_padding = torch.zeros((3, rounded_new_size[1], rounded_new_size[0]), dtype=torch.float32) + 0.5

            pad_left = (rounded_new_size[0] - new_size[0]) // 2
            pad_top = (rounded_new_size[1] - new_size[1]) // 2

            image_with_padding[:, pad_top:pad_top + new_size[1], pad_left:pad_left + new_size[0]] = image
            if self._task_type == 'object_detection':
                assert targets.shape[1] == 5, f"Expected targets to have 5 columns, got {targets.shape[1]}"
                scale_x = new_size[0] / rounded_new_size[0]
                scale_y = new_size[1] / rounded_new_size[1]
                normalized_pad_left = pad_left / rounded_new_size[0]
                normalized_pad_top = pad_top / rounded_new_size[1]

                targets[:, (1, 3)] = targets[:, (1, 3)] * scale_x + normalized_pad_left
                targets[:, (2, 4)] = targets[:, (2, 4)] * scale_y + normalized_pad_top

            return image_with_padding, targets
        else:
            resized = inputs.resize(rounded_new_size, PIL.Image.BICUBIC)
            return torch.from_numpy(numpy.array(resized)).to(torch.float32).permute(2, 0, 1) / 255.0, targets
