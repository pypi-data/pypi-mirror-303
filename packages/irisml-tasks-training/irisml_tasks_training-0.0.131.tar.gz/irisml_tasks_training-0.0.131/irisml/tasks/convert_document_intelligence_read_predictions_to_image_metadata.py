"""
Task to convert Document Intelligence Read predictions to image metadata.
"""
import dataclasses
import logging
import typing

import irisml.core

logger = logging.getLogger(__name__)


class Task(irisml.core.TaskBase):
    """
    Convert Document Intelligence Read predictions to image metadata.
    """

    VERSION = '0.1.0'

    @dataclasses.dataclass
    class Inputs:
        predictions: typing.List[typing.Dict[str, typing.Any]]

    @dataclasses.dataclass
    class Outputs:
        image_metadata: typing.List[typing.Dict[str, str]]

    def execute(self, inputs):
        metadata = []
        for prediction in inputs.predictions:
            if "content" not in prediction:
                raise ValueError(f"Missing 'content' in prediction: {prediction}")
            metadata.append({'ocr': prediction['content']})
        return self.Outputs(image_metadata=metadata)
