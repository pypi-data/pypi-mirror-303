import unittest
import torch
from irisml.tasks.evaluate_phrase_grounding_recall import Task


class TestEvaluatePhraseGroundingRecall(unittest.TestCase):
    def test_simple(self):
        predictions = [[((0, 1), torch.tensor([[0.1, 0.1, 0.2, 0.2]]))]]
        targets = [[((0, 1), torch.tensor([[0.1, 0.1, 0.2, 0.2]]))]]
        self.assertEqual(Task(Task.Config()).execute(Task.Inputs(predictions=predictions, targets=targets)).recall, 1.0)

        predictions = [[((0, 1), torch.tensor([[0.1, 0.1, 0.2, 0.2], [0, 0, 1.0, 1.0]]))]]
        self.assertEqual(Task(Task.Config()).execute(Task.Inputs(predictions=predictions, targets=targets)).recall, 1.0)

        predictions = [[((0, 1), torch.tensor([[0.1, 0.1, 0.2, 0.2]])), ((1, 2), torch.tensor([[0.1, 0.1, 0.2, 0.2]]))]]
        self.assertEqual(Task(Task.Config()).execute(Task.Inputs(predictions=predictions, targets=targets)).recall, 1.0)

        # Tuple might be converted to a list. This happens when CUDA is used.
        predictions = [[[[0, 1], torch.tensor([[0.1, 0.1, 0.2, 0.2]])], ([1, 2], torch.tensor([[0.1, 0.1, 0.2, 0.2]]))]]
        self.assertEqual(Task(Task.Config()).execute(Task.Inputs(predictions=predictions, targets=targets)).recall, 1.0)

        predictions = [[]]
        self.assertEqual(Task(Task.Config()).execute(Task.Inputs(predictions=predictions, targets=targets)).recall, 0.0)

        predictions = [[((0, 1), torch.zeros(0, 4))]]
        self.assertEqual(Task(Task.Config()).execute(Task.Inputs(predictions=predictions, targets=targets)).recall, 0.0)
