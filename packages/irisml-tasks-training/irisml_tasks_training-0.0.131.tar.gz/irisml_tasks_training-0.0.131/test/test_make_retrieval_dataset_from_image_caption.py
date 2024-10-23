import unittest
import PIL.Image
import torch
import torch.utils.data
from irisml.tasks.make_retrieval_dataset_from_image_caption import Task


class FakeDataset(torch.utils.data.Dataset):
    def __init__(self, data):
        self._data = data

    def __getitem__(self, index):
        return self._data[index]

    def __len__(self):
        return len(self._data)


class TestMakeRetrievalDatasetFromImageCaption(unittest.TestCase):
    def test_simple(self):
        dataset = FakeDataset([(PIL.Image.new('RGB', (224, 224)), ['a', 'b']), (PIL.Image.new('RGB', (224, 224)), ['c'])])
        outputs = Task(Task.Config()).execute(Task.Inputs(dataset))

        self.assertIsInstance(outputs.image_retrieval_dataset, torch.utils.data.Dataset)
        self.assertIsInstance(outputs.text_retrieval_dataset, torch.utils.data.Dataset)

        self.assertEqual(len(outputs.image_retrieval_dataset), 2)
        self.assertIsInstance(outputs.image_retrieval_dataset[0][0], PIL.Image.Image)
        self.assertIsInstance(outputs.image_retrieval_dataset[0][1], torch.Tensor)
        self.assertEqual(outputs.image_retrieval_dataset[0][1].tolist(), [0, 1])
        self.assertEqual(outputs.image_retrieval_dataset[1][1].tolist(), [2])

        self.assertEqual(len(outputs.text_retrieval_dataset), 3)
        self.assertIsInstance(outputs.text_retrieval_dataset[0][0], str)
        self.assertIsInstance(outputs.text_retrieval_dataset[0][1], torch.Tensor)
        self.assertEqual(outputs.text_retrieval_dataset[0][0], 'a')
        self.assertEqual(outputs.text_retrieval_dataset[1][0], 'b')
        self.assertEqual(outputs.text_retrieval_dataset[2][0], 'c')
        self.assertEqual(outputs.text_retrieval_dataset[0][1].item(), 0)
        self.assertEqual(outputs.text_retrieval_dataset[1][1].item(), 0)
        self.assertEqual(outputs.text_retrieval_dataset[2][1].item(), 1)
