import unittest
import torch
from irisml.tasks.make_image_collate_function import Task


class TestMakeImageCollateFunction(unittest.TestCase):
    def test_simple(self):
        collate_function = Task(Task.Config()).execute(Task.Inputs()).collate_function
        batch = [(torch.rand(3, 224, 224), 'a'), (torch.rand(3, 224, 224), 3)]
        images, targets = collate_function(batch)
        self.assertEqual(images.shape, torch.Size([2, 3, 224, 224]))
        self.assertEqual(targets, ['a', 3])
