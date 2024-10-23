import dataclasses
import typing
import torch
import irisml.core


class Task(irisml.core.TaskBase):
    """Creates a collate_function to stach images only.

        [(image: Tensor, target: T), (image: Rensor, target: T), ...] => (images: Tensor, targets: list[T])
    """
    VERSION = '0.1.0'

    @dataclasses.dataclass
    class Outputs:
        collate_function: typing.Callable

    def execute(self, inputs):
        return self.Outputs(collate_function)

    def dry_run(self, inputs):
        return self.execute(inputs)


def collate_function(batch):
    images = [b[0] for b in batch]
    targets = [b[1] for b in batch]
    images = torch.stack(images, 0)
    return images, targets
