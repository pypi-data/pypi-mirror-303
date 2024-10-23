import dataclasses
import typing

import PIL.Image
import PIL.ImageOps
import torch
import torch.utils.data

import irisml.core


class Task(irisml.core.TaskBase):
    """Apply 2x2 mosaic augmentation to a dataset.

    Note that new random images are sampled each time the dataset is accessed.

    The returned dataset object has `set_epoch` method to set the current epoch. This method must be called when stop_epoch is set.

    Config:
        image_size (int): The size of the output images.
        task_type (str): The type of the task. Either 'classification_multilabel' or 'object_detection'.
        stop_epoch (int): If set, the mosaic augmentation is disabled after the specified epoch.
    """
    VERSION = '0.2.0'

    @dataclasses.dataclass
    class Inputs:
        dataset: torch.utils.data.Dataset

    @dataclasses.dataclass
    class Config:
        image_size: int
        task_type: typing.Literal['classification_multilabel', 'object_detection'] = 'object_detection'
        stop_epoch: typing.Optional[int] = None

    @dataclasses.dataclass
    class Outputs:
        dataset: torch.utils.data.Dataset

    def execute(self, inputs):
        dataset = MosaicDataset(inputs.dataset, self.config.image_size, self.config.task_type, self.config.stop_epoch)
        return self.Outputs(dataset)

    def dry_run(self, inputs):
        return self.execute(inputs)


class MosaicDataset(torch.utils.data.Dataset):
    def __init__(self, dataset, image_size, task_type, stop_epoch):
        self._dataset = dataset
        self._image_size = image_size
        self._task_type = task_type
        self._stop_epoch = stop_epoch
        self._epoch = 0

    def __len__(self):
        return len(self._dataset)

    def __getitem__(self, index):
        if self._stop_epoch and self._epoch >= self._stop_epoch:
            return self._dataset[index]

        random_tensor3 = torch.randint(0, len(self._dataset), (3,))
        indices = [index] + [int(i) for i in random_tensor3]
        assert len(indices) == 4

        data = [self._dataset[i] for i in indices]
        images = [d[0] for d in data]
        targets = [d[1] for d in data]

        data[0] = self._pad(images[0], targets[0], (1, 1))
        data[1] = self._pad(images[1], targets[1], (0, 1))
        data[2] = self._pad(images[2], targets[2], (1, 0))
        data[3] = self._pad(images[3], targets[3], (0, 0))
        s = self._image_size
        image, targets = self._tile(data)

        random_tensor2 = torch.randint(0, s, (2,))
        image, targets = self._crop(image, targets, ((int(random_tensor2[0]), int(random_tensor2[1]), s + int(random_tensor2[0]), s + int(random_tensor2[1]))))

        return image, targets

    def set_epoch(self, epoch: int):
        self._epoch = epoch

    def _pad(self, image, targets, centering):
        scale = self._image_size / max(image.size)
        new_size = (int(image.size[0] * scale), int(image.size[1] * scale))
        image = image.resize(new_size, PIL.Image.BICUBIC)
        new_image = PIL.Image.new('RGB', (self._image_size, self._image_size))
        targets = self._scale_targets(targets, (image.size[0] / self._image_size, image.size[1] / self._image_size))
        if centering == (0, 0):
            new_image.paste(image, (0, 0))
        elif centering == (1, 0):
            new_image.paste(image, (self._image_size - new_size[0], 0))
            targets = self._shift_targets(targets, ((self._image_size - new_size[0]) / self._image_size, 0))
        elif centering == (0, 1):
            new_image.paste(image, (0, self._image_size - new_size[1]))
            targets = self._shift_targets(targets, (0, (self._image_size - new_size[1]) / self._image_size))
        elif centering == (1, 1):
            new_image.paste(image, (self._image_size - new_size[0], self._image_size - new_size[1]))
            targets = self._shift_targets(targets, ((self._image_size - new_size[0]) / self._image_size, (self._image_size - new_size[1]) / self._image_size))
        else:
            raise ValueError(f"Invalid centering: {centering}")

        return new_image, targets

    def _tile(self, data):
        assert len(data) == 4
        image = PIL.Image.new('RGB', (self._image_size * 2, self._image_size * 2))
        image.paste(data[0][0], (0, 0))
        image.paste(data[1][0], (self._image_size, 0))
        image.paste(data[2][0], (0, self._image_size))
        image.paste(data[3][0], (self._image_size, self._image_size))

        if self._task_type == 'object_detection':
            for i in range(4):
                data[i][1][:, 1:] /= 2.0

            data[1][1][:, (1, 3)] += 0.5
            data[2][1][:, (2, 4)] += 0.5
            data[3][1][:, 1:] += 0.5

            targets = torch.cat([data[i][1] for i in range(4)], dim=0)
        elif self._task_type == 'classification_multilabel':
            targets = torch.clamp(torch.sum(torch.stack([data[i][1] for i in range(4)]), dim=0), max=1.0)
        else:
            raise ValueError(f"Invalid task type: {self._task_type}")

        return image, targets

    def _crop(self, image, targets, box):
        assert image.size == (self._image_size * 2, self._image_size * 2)
        assert box[2] - box[0] == self._image_size and box[3] - box[1] == self._image_size
        image = image.crop(box)
        targets = self._scale_targets(targets, (2.0, 2.0))
        targets = self._shift_targets(targets, (-box[0] / self._image_size, -box[1] / self._image_size))
        return image, targets

    def _scale_targets(self, targets, scale: typing.Tuple[float, float]):
        if self._task_type == 'object_detection':
            targets[:, (1, 3)] *= scale[0]
            targets[:, (2, 4)] *= scale[1]
        return targets

    def _shift_targets(self, targets, shift: typing.Tuple[float, float]):
        if self._task_type == 'object_detection':
            targets[:, (1, 3)] += shift[0]
            targets[:, (2, 4)] += shift[1]

            targets[:, 1:] = torch.clamp(targets[:, 1:], min=0, max=1)

            # Remove boxes with zero area.
            valid_boxes = ((targets[:, 3] - targets[:, 1]) * (targets[:, 4] - targets[:, 2])) > 0
            targets = targets[valid_boxes]

        return targets
