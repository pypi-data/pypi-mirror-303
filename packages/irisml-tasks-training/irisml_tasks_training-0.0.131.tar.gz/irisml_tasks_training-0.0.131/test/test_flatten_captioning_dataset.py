import unittest
import PIL.Image
import torch.utils.data
from irisml.tasks.flatten_captioning_dataset import Task


class FakeDataset(torch.utils.data.Dataset):
    def __init__(self, data):
        self._data = data

    def __getitem__(self, index):
        return self._data[index]

    def __len__(self):
        return len(self._data)


class TestFlattenCaptioningDataset(unittest.TestCase):
    def test_simple(self):
        dataset = FakeDataset([(PIL.Image.new('RGB', (8, 8)), ['caption A', 'caption B', 'caption C']), (PIL.Image.new('RGB', (16, 16)), []), (PIL.Image.new('RGB', (32, 32)), ['caption D'])])
        new_dataset = Task(Task.Config()).execute(Task.Inputs(dataset)).dataset
        self.assertEqual(len(new_dataset), 4)

        self.assertIsInstance(new_dataset[0][0], PIL.Image.Image)
        self.assertEqual(new_dataset[0][0].size, (8, 8))
        self.assertEqual(new_dataset[1][0].size, (8, 8))
        self.assertEqual(new_dataset[2][0].size, (8, 8))
        self.assertEqual(new_dataset[3][0].size, (32, 32))

        self.assertEqual(new_dataset[0][1], ['caption A'])
        self.assertEqual(new_dataset[1][1], ['caption B'])
        self.assertEqual(new_dataset[2][1], ['caption C'])
        self.assertEqual(new_dataset[3][1], ['caption D'])
