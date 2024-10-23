import copy
import dataclasses
import logging
import typing

import torch

import irisml.core

logger = logging.getLogger(__name__)


class Task(irisml.core.TaskBase):
    """Convert object detection prediction and target coordinates from relative to absolute.
    """
    VERSION = '0.1.1'

    @dataclasses.dataclass
    class Inputs:
        dataset: torch.utils.data.Dataset
        predictions: typing.List[torch.Tensor]
        targets: typing.List[torch.Tensor]

    @dataclasses.dataclass
    class Outputs:
        predictions: torch.Tensor
        targets: torch.Tensor

    def execute(self, inputs):
        if not (len(inputs.predictions) == len(inputs.targets) == len(inputs.dataset)):
            raise ValueError('The number of predictions and targets should be the same.')

        absolute_predictions = copy.deepcopy(inputs.predictions)
        absolute_targets = copy.deepcopy(inputs.targets)

        for idx, (image, _) in enumerate(inputs.dataset):
            height, width = image.size

            # NOTE: This might break if the images were shuffled in the dataloader during prediction task
            absolute_predictions[idx][:, 2:] = self._convert_coordinates(absolute_predictions[idx][:, 2:], height, width)
            absolute_targets[idx][:, 1:] = self._convert_coordinates(absolute_targets[idx][:, 1:], height, width)

        return self.Outputs(absolute_predictions, absolute_targets)

    def dry_run(self, inputs):
        return self.execute(inputs)

    def _convert_coordinates(self, coords, height, width):
        if coords.shape[-1] != 4:
            raise ValueError('Shape of coordinates should be (N, 4)')

        coords[:, 0] = coords[:, 0] * width
        coords[:, 1] = coords[:, 1] * height
        coords[:, 2] = coords[:, 2] * width
        coords[:, 3] = coords[:, 3] * height
        return coords
