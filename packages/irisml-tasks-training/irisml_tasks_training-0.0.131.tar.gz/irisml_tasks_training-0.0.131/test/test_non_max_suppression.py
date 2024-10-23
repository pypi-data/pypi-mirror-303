import unittest

import torch

from irisml.tasks.non_max_suppression import Task


class TestNonMaxSuppression(unittest.TestCase):
    def test_simple(self):
        predictions = [torch.Tensor([[0, 0.8, 0, 0, 1, 1],
                                     [0, 0.9, 0, 0, 0.9, 0.9],
                                     [0, 0.7, 0, 0, 0.8, 0.8]])]

        expected = [torch.tensor([[0, 0.9, 0, 0, 0.9, 0.9]])]
        result = Task(Task.Config(iou_threshold=0.5)).execute(Task.Inputs(predictions))

        self.assertTrue(torch.all(result.predictions[0] == expected[0]))

    def test_two_classes(self):
        predictions = [torch.Tensor([[0, 0.1, 0, 0, 1, 1],
                                     [0, 0.9, 0, 0, 0.9, 0.9],
                                     [0, 0.7, 0, 0, 0.8, 0.8],
                                     [1, 0.9, 0, 0, 1, 1],
                                     [1, 0.8, 0, 0, 0.9, 0.9],
                                     [1, 0.7, 0, 0, 0.8, 0.8]])]

        expected = [torch.tensor([[0, 0.9, 0, 0, 0.9, 0.9],
                                  [1, 0.9, 0, 0, 1, 1]])]

        result = Task(Task.Config(iou_threshold=0.5)).execute(Task.Inputs(predictions))
        self.assertTrue(torch.all(result.predictions[0] == expected[0]))

    def test_two_images(self):
        predictions = [torch.Tensor([[0, 0.9, 0, 0, 1, 1],
                                     [0, 0.8, 0, 0, 0.9, 0.9],
                                     [0, 0.7, 0, 0, 0.8, 0.8],
                                     [1, 0.9, 0, 0, 1, 1],
                                     [1, 0.8, 0, 0, 0.9, 0.9],
                                     [1, 0.7, 0, 0, 0.8, 0.8]]),
                       torch.Tensor([[0, 0.9, 0, 0, 1, 1],
                                     [0, 0.8, 0, 0, 0.9, 0.9],
                                     [0, 0.7, 0, 0, 0.8, 0.8]])]

        expected = [torch.tensor([[0, 0.9, 0, 0, 1, 1],
                                  [1, 0.9, 0, 0, 1, 1]]),
                    torch.tensor([[0, 0.9, 0, 0, 1, 1]])]

        result = Task(Task.Config(iou_threshold=0.5)).execute(Task.Inputs(predictions))

        for i in range(len(result.predictions)):
            self.assertTrue(torch.all(result.predictions[i] == expected[i]))

    def test_class_agnostic(self):
        predictions = [torch.Tensor([[0, 0.9, 0, 0, 1, 1],
                                     [1, 0.8, 0, 0, 0.9, 0.9]])]

        expected = [torch.tensor([[0, 0.9, 0, 0, 1, 1]])]

        result = Task(Task.Config(iou_threshold=0.5, class_agnostic=True)).execute(Task.Inputs(predictions))
        self.assertTrue(torch.all(result.predictions[0] == expected[0]))

    def test_class_agnostic_two_images(self):
        predictions = [torch.Tensor([[0, 0.9, 0, 0, 1, 1],
                                     [1, 0.8, 0, 0, 0.9, 0.9]]),
                       torch.Tensor([[1, 0.9, 0, 0, 1, 1],
                                     [0, 0.8, 0, 0, 0.9, 0.9]])]

        expected = [torch.tensor([[0, 0.9, 0, 0, 1, 1]]),
                    torch.tensor([[1, 0.9, 0, 0, 1, 1]])]

        result = Task(Task.Config(iou_threshold=0.5, class_agnostic=True)).execute(Task.Inputs(predictions))

        for i in range(len(result.predictions)):
            self.assertTrue(torch.all(result.predictions[i] == expected[i]))

    def test_empty(self):
        predictions = [torch.empty(0, 6)]
        expected = [torch.empty(0, 6)]
        result = Task(Task.Config(iou_threshold=0.5)).execute(Task.Inputs(predictions))
        self.assertTrue(torch.all(result.predictions[0] == expected[0]))


if __name__ == '__main__':
    unittest.main()
