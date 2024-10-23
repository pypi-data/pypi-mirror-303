import unittest
import PIL.Image
import torch
from irisml.tasks.convert_vqa_dataset_to_image_text_classification_dataset import Task


class TestConvertVqaDatasetToImageTextClassificationDataset(unittest.TestCase):
    def test_simple(self):
        dataset = [(('question1', PIL.Image.new('RGB', (10, 10))), 'answer1'), (('question2', PIL.Image.new('RGB', (10, 10))), 'answer2'), (('question3', PIL.Image.new('RGB', (10, 10))), 'answer1')]

        outputs = Task(Task.Config()).execute(Task.Inputs(dataset))
        self.assertEqual(len(outputs.dataset), 3)
        self.assertEqual(outputs.num_classes, 2)
        self.assertEqual(outputs.class_names, ['answer1', 'answer2'])
        self.assertIsInstance(outputs.dataset[0][0][0], PIL.Image.Image)
        self.assertEqual(outputs.dataset[0][0][1], 'question1')
        self.assertIsInstance(outputs.dataset[0][1], torch.Tensor)

        self.assertEqual(outputs.dataset[0][1], torch.tensor(0, dtype=torch.long))
        self.assertEqual(outputs.dataset[1][1], torch.tensor(1, dtype=torch.long))
        self.assertEqual(outputs.dataset[2][1], torch.tensor(0, dtype=torch.long))

    def test_invalid_dataset(self):
        dataset = [(PIL.Image.new('RGB', (8, 8)), 'answer1')]
        with self.assertRaises(ValueError):
            Task(Task.Config()).execute(Task.Inputs(dataset))

        dataset = [('question1', PIL.Image.new('RGB', (8, 8)), torch.tensor(0))]
        with self.assertRaises(ValueError):
            Task(Task.Config()).execute(Task.Inputs(dataset))

        dataset = []
        Task(Task.Config()).execute(Task.Inputs(dataset))  # Should not raise

    def test_class_names_input(self):
        dataset = [(('question1', PIL.Image.new('RGB', (10, 10))), 'answer1'), (('question2', PIL.Image.new('RGB', (10, 10))), 'answer2'), (('question3', PIL.Image.new('RGB', (10, 10))), 'answer1')]

        outputs = Task(Task.Config()).execute(Task.Inputs(dataset, class_names=['answer2', 'answer1', 'answer3']))
        self.assertEqual(len(outputs.dataset), 3)
        self.assertEqual(outputs.num_classes, 3)
        self.assertEqual(outputs.class_names, ['answer2', 'answer1', 'answer3'])

        self.assertEqual(outputs.dataset[0][1], torch.tensor(1, dtype=torch.long))
        self.assertEqual(outputs.dataset[1][1], torch.tensor(0, dtype=torch.long))
        self.assertEqual(outputs.dataset[2][1], torch.tensor(1, dtype=torch.long))

        # Should raise if class_names is not a subset of the dataset
        with self.assertRaises(ValueError):
            Task(Task.Config()).execute(Task.Inputs(dataset, class_names=['answer1']))  # missing 'answer2'
