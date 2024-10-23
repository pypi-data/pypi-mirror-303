import pickle
import unittest
import PIL.Image
import torch
import torchvision.transforms
from irisml.tasks.make_vqa_image_transform import Task


class TestMakeVqaImageTransform(unittest.TestCase):
    def test_simple_without_tokenizer(self):
        image_transform = torchvision.transforms.ToTensor()

        def text_transform(text):
            return f'question: {text} answer:'

        outputs = Task(Task.Config()).execute(Task.Inputs(image_transform, text_transform))
        transform = outputs.transform

        transform_outputs = transform(('What is this?', PIL.Image.new('RGB', (32, 32))), 'R2D2')
        self.assertEqual(transform_outputs[0][0], 'question: What is this? answer:')
        self.assertIsInstance(transform_outputs[0][1], torch.Tensor)
        self.assertEqual(transform_outputs[1], 'R2D2')

    def test_simple_with_tokenizer(self):
        def tokenizer(text):
            return torch.tensor([1, 2, 3]), torch.tensor([1, 1, 0])

        image_transform = torchvision.transforms.ToTensor()
        outputs = Task(Task.Config()).execute(Task.Inputs(image_transform, tokenizer=tokenizer))
        transform = outputs.transform

        transform_outputs = transform(('What is this?', PIL.Image.new('RGB', (32, 32))), 'R2D2')
        self.assertIsInstance(transform_outputs[0][0], tuple)
        self.assertEqual(len(transform_outputs[0][0]), 2)
        self.assertIsInstance(transform_outputs[0][0][0], torch.Tensor)
        self.assertIsInstance(transform_outputs[0][0][1], torch.Tensor)
        self.assertIsInstance(transform_outputs[0][1], torch.Tensor)

        self.assertIsInstance(transform_outputs[1], tuple)
        self.assertEqual(len(transform_outputs[1]), 2)
        self.assertIsInstance(transform_outputs[1][0], torch.Tensor)
        self.assertIsInstance(transform_outputs[1][1], torch.Tensor)

    def test_collate_function(self):
        image_transform = torchvision.transforms.ToTensor()
        outputs = Task(Task.Config()).execute(Task.Inputs(image_transform))
        collate_function = outputs.collate_function

        pickle.dumps(collate_function)  # Make sure it's pickleable

        question = (torch.Tensor([1, 2, 3]), torch.Tensor([1, 1, 0]))
        answer = (torch.Tensor([4, 5, 6]), torch.Tensor([1, 1, 0]))
        image = torch.rand(3, 32, 32)

        collate_outputs = collate_function([((question, image), answer) for _ in range(4)])
        self.assertIsInstance(collate_outputs, tuple)
        self.assertEqual(len(collate_outputs), 2)

        # inputs
        self.assertIsInstance(collate_outputs[0], tuple)
        self.assertEqual(len(collate_outputs[0]), 2)
        self.assertIsInstance(collate_outputs[0][0], tuple)
        self.assertEqual(len(collate_outputs[0][0]), 2)
        self.assertIsInstance(collate_outputs[0][0][0], torch.Tensor)
        self.assertIsInstance(collate_outputs[0][0][1], torch.Tensor)
        self.assertIsInstance(collate_outputs[0][1], torch.Tensor)
        self.assertEqual(collate_outputs[0][0][0].shape, (4, 3))
        self.assertEqual(collate_outputs[0][0][1].shape, (4, 3))
        self.assertEqual(collate_outputs[0][1].shape, (4, 3, 32, 32))

        # targets
        self.assertIsInstance(collate_outputs[1], tuple)
        self.assertEqual(len(collate_outputs[1]), 2)
        self.assertIsInstance(collate_outputs[1][0], torch.Tensor)
        self.assertIsInstance(collate_outputs[1][1], torch.Tensor)
        self.assertEqual(collate_outputs[1][0].shape, (4, 3))
        self.assertEqual(collate_outputs[1][1].shape, (4, 3))

        # When targets are strings
        collate_outputs = collate_function([((question, image), 'answer') for _ in range(4)])
        self.assertIsInstance(collate_outputs[1], list)
        self.assertEqual(len(collate_outputs[1]), 4)
        self.assertIsInstance(collate_outputs[1][0], str)
        self.assertEqual(collate_outputs[1], ['answer' for _ in range(4)])

    def test_collate_function_padding(self):
        image_transform = torchvision.transforms.ToTensor()
        outputs = Task(Task.Config(pad_token_id=100)).execute(Task.Inputs(image_transform))
        collate_function = outputs.collate_function

        collate_outputs = collate_function([(((torch.Tensor([i] * i), torch.Tensor([1] * i)), torch.rand(3, 32, 32)), 'answer') for i in range(1, 5)])

        self.assertEqual(collate_outputs[0][0][0].tolist(), [[1, 100, 100, 100], [2, 2, 100, 100], [3, 3, 3, 100], [4, 4, 4, 4]])
        self.assertEqual(collate_outputs[0][0][1].tolist(), [[1, 0, 0, 0], [1, 1, 0, 0], [1, 1, 1, 0], [1, 1, 1, 1]])
        self.assertEqual(collate_outputs[1], ['answer' for _ in range(4)])
