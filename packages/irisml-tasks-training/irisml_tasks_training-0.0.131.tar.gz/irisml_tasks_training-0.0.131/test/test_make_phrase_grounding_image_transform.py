import unittest
import PIL.Image
import torch
import torchvision.transforms
from irisml.tasks.make_phrase_grounding_image_transform import Task


class TestMakePhraseGroundingImageTransform(unittest.TestCase):
    def test_simple(self):
        image_transform = torchvision.transforms.ToTensor()

        def text_transform(x):
            return x + '!'

        transform = Task(Task.Config()).execute(Task.Inputs(image_transform, text_transform)).transform

        outputs = transform(('caption', PIL.Image.new('RGB', (100, 100))), [((0, 1), torch.tensor([[0, 0, 1, 1]]))])
        self.assertEqual(outputs[0][0], 'caption!')
        self.assertIsInstance(outputs[0][1], torch.Tensor)
        self.assertEqual(outputs[1][0][0], (0, 1))
        self.assertEqual(outputs[1][0][1].tolist(), [[0, 0, 1, 1]])
