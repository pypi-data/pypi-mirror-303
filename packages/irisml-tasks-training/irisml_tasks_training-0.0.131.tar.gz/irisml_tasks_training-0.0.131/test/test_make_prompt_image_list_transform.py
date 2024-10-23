import unittest
import PIL.Image
import torch
import torchvision
from irisml.tasks.make_prompt_image_list_transform import Task


class TestMakePromptImageListTransform(unittest.TestCase):
    def test_simple(self):
        image_transform = torchvision.transforms.ToTensor()
        prompt = 'prompt'
        outputs = Task(Task.Config()).execute(Task.Inputs(image_transform))
        transform = outputs.transform

        images = [PIL.Image.new('RGB', (1, 1)), PIL.Image.new('RGB', (2, 2))]
        sample = (images, prompt)
        target = torch.tensor(0)
        self.assertEqual(transform(sample, target)[1], target)
        self.assertEqual(transform(sample, target)[0][0], prompt)
        self.assertEqual(len(transform(sample, target)[0][1]), len(images))

        self.assertTrue(torch.equal(transform(sample, target)[0][1][0], torch.zeros(3, 1, 1)))
        self.assertTrue(torch.equal(transform(sample, target)[0][1][1], torch.zeros(3, 2, 2)))
