import dataclasses
import logging
import typing
import irisml.core

logger = logging.getLogger(__name__)


class Task(irisml.core.TaskBase):
    """Calculate accuracy of string matching.

    Case insensitive.
    """
    VERSION = '0.1.0'

    @dataclasses.dataclass
    class Inputs:
        predictions: typing.List[str]
        targets: typing.List[str]

    @dataclasses.dataclass
    class Outputs:
        accuracy: float

    def execute(self, inputs):
        if len(inputs.predictions) != len(inputs.targets):
            raise ValueError('predictions and targets must have same length')

        num_correct = 0
        for prediction, target in zip(inputs.predictions, inputs.targets):
            # Ignore cases
            if prediction.lower() == target.lower():
                num_correct += 1

        accuracy = num_correct / len(inputs.predictions)
        logger.info(f"Accuracy: {accuracy}, num_correct: {num_correct}, num_samples: {len(inputs.predictions)}")
        return self.Outputs(accuracy=accuracy)

    def dry_run(self, inputs):
        return self.execute(inputs)
