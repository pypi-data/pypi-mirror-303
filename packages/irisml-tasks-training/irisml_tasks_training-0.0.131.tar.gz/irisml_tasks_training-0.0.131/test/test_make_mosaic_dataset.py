import unittest
import PIL.Image
import torch
from irisml.tasks.make_mosaic_dataset import Task


class FakeDataset(torch.utils.data.Dataset):
    def __init__(self, data):
        self._data = data

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]


class TestMakeMosaicDataset(unittest.TestCase):
    def test_object_detection(self):
        dataset = FakeDataset([(PIL.Image.new('RGB', (32, 32), color='red'), torch.zeros(0, 5)),
                               (PIL.Image.new('RGB', (16, 16), color='green'), torch.tensor([[0, 0.1, 0.1, 0.9, 0.9]])),
                               (PIL.Image.new('RGB', (64, 63), color='blue'), torch.tensor([[1, 0.1, 0.1, 0.9, 0.9]])),
                               (PIL.Image.new('RGB', (128, 32), color='yellow'), torch.tensor([[2, 0.1, 0.1, 0.9, 0.9]]))])

        new_dataset = Task(Task.Config(image_size=64, task_type='object_detection')).execute(Task.Inputs(dataset)).dataset
        self.assertIsInstance(new_dataset, torch.utils.data.Dataset)

        self.assertEqual(len(new_dataset), len(dataset))
        image0, targets0 = new_dataset[0]
        self.assertEqual(image0.size, (64, 64))
        self.assertIsInstance(targets0, torch.Tensor)
        self.assertEqual(targets0.shape[1], 5)

        all_targets = torch.cat([new_dataset[i][1] for i in range(len(new_dataset))])
        self.assertGreaterEqual(all_targets[:, 1:].min().item(), 0)
        self.assertLessEqual(all_targets[:, 1:].max().item(), 1)
        areas = (all_targets[:, 3] - all_targets[:, 1]) * (all_targets[:, 4] - all_targets[:, 2])
        self.assertGreater(areas.min().item(), 0)

    def test_classification_multilabel(self):
        dataset = FakeDataset([(PIL.Image.new('RGB', (32, 32), color='red'), torch.tensor([0, 0, 1])),
                               (PIL.Image.new('RGB', (16, 16), color='green'), torch.tensor([1, 0, 1])),
                               (PIL.Image.new('RGB', (64, 63), color='blue'), torch.tensor([0, 1, 0])),
                               (PIL.Image.new('RGB', (128, 32), color='yellow'), torch.tensor([1, 1, 1]))])

        new_dataset = Task(Task.Config(image_size=64, task_type='classification_multilabel')).execute(Task.Inputs(dataset)).dataset
        self.assertIsInstance(new_dataset, torch.utils.data.Dataset)

        self.assertEqual(len(new_dataset), len(dataset))
        image0, targets0 = new_dataset[0]
        self.assertEqual(image0.size, (64, 64))
        self.assertIsInstance(targets0, torch.Tensor)
        self.assertEqual(targets0.shape, (3, ))

        all_targets = torch.cat([new_dataset[i][1] for i in range(len(new_dataset))])
        self.assertGreaterEqual(all_targets.min().item(), 0)
        self.assertEqual(all_targets.max().item(), 1)

    def test_stop_epoch(self):
        dataset = FakeDataset([(PIL.Image.new('RGB', (32, 32), color='red'), torch.zeros(0, 5)),
                               (PIL.Image.new('RGB', (16, 16), color='green'), torch.tensor([[0, 0.1, 0.1, 0.9, 0.9]])),
                               (PIL.Image.new('RGB', (64, 63), color='blue'), torch.tensor([[1, 0.1, 0.1, 0.9, 0.9]])),
                               (PIL.Image.new('RGB', (128, 32), color='yellow'), torch.tensor([[2, 0.1, 0.1, 0.9, 0.9]]))])

        new_dataset = Task(Task.Config(image_size=64, task_type='object_detection', stop_epoch=2)).execute(Task.Inputs(dataset)).dataset

        self.assertTrue(hasattr(new_dataset, 'set_epoch'))
        self.assertFalse(torch.equal(new_dataset[1][1], dataset[1][1]))
        new_dataset.set_epoch(0)
        self.assertFalse(torch.equal(new_dataset[1][1], dataset[1][1]))
        new_dataset.set_epoch(2)
        self.assertTrue(torch.equal(new_dataset[1][1], dataset[1][1]))

        new_dataset.set_epoch(0)
        self.assertFalse(torch.equal(new_dataset[1][1], dataset[1][1]))
