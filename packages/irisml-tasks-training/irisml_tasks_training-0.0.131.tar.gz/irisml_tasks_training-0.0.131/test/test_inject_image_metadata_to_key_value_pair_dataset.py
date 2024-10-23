import unittest

import PIL.Image
import torch.utils.data

from irisml.tasks.inject_image_metadata_to_key_value_pair_dataset import Task, Dataset


class MockDataset(torch.utils.data.Dataset):
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]


class TestInjectImageMetadataToKeyValuePairDataset(unittest.TestCase):
    def setUp(self):
        im1 = PIL.Image.new('RGB', (1, 1))
        im2 = PIL.Image.new('RGB', (2, 2))

        # A sample of key-value pair dataset
        inputs = [
            ("what is in this image?", [(im1, None)]),
            ("what is in that image?", [(im2, {"color": "black"})])
        ]
        targets = [
            {"answer": {"value": {"content": "cat food"}}},
            {"answer": {"value": {"content": "dog food"}}}
        ]

        # Create a dataset from these inputs and targets
        self.dataset = MockDataset(list(zip(inputs, targets)))

        self.image_metadata = [
            {"label": "cat"},
            {"label": "dog"}
        ]

    def test_execute_success(self):
        task = Task(Task.Config())
        inputs = Task.Inputs(dataset=self.dataset, image_metadata=self.image_metadata)

        outputs = task.execute(inputs)
        self.assertIsInstance(outputs, Task.Outputs)
        self.assertEqual(len(outputs.dataset), len(self.dataset))

    def test_dataset_length_mismatch(self):
        with self.assertRaises(ValueError):
            inputs = Task.Inputs(dataset=self.dataset, image_metadata=[self.image_metadata[0]])
            task = Task(Task.Config())
            task.execute(inputs)

    def test_getitem_with_correct_metadata(self):
        dataset = Dataset(self.dataset, self.image_metadata)

        inputs, targets = dataset[0]
        self.assertEqual(inputs[0], "what is in this image?")  # Check the text input
        self.assertEqual(inputs[1][0][0], PIL.Image.new('RGB', (1, 1)))  # Check the image input
        self.assertEqual(inputs[1][0][1], {"label": "cat"})  # Check the metadata
        self.assertEqual(targets["answer"]["value"]["content"], "cat food")  # Check the target value

        inputs, targets = dataset[1]
        self.assertEqual(inputs[1][0][1], {"color": "black", "label": "dog"})  # Check the metadata
