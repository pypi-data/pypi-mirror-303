import unittest

import torch
from torchvision import transforms

from irisml.tasks.convert_relative_to_absolute_coordinates import Task


class FakeDataset(torch.utils.data.Dataset):
    def __init__(self, data):
        self._data = data

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]


class TestConvertRelativetoAbsoluteCoordinates(unittest.TestCase):
    def test_convert_relative_to_absolute_coordinates(self):
        dataset = FakeDataset([(transforms.ToPILImage()(torch.zeros((3, 100, 100))), torch.tensor([0, 0, 0, 1, 1]))])

        predictions = [torch.tensor([[0, 0, 0, 0, 1, 1],
                                     [0, 0, 0, 0, 0.5, 0.5]])]

        targets = [torch.tensor([[0, 0, 0, 1, 1]])]

        task = Task(Task.Config())
        outputs = task.execute(Task.Inputs(dataset, predictions, targets))

        self.assertEqual(outputs.predictions[0][0].tolist(), [0, 0, 0, 0, 100, 100])
        self.assertEqual(outputs.predictions[0][1].tolist(), [0, 0, 0, 0, 50, 50])
        self.assertEqual(outputs.targets[0][0].tolist(), [0, 0, 0, 100, 100])


if __name__ == '__main__':
    unittest.main()
