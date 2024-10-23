import unittest
import torch
from irisml.tasks.evaluate_phrase_grounding import Task


class TestEvaluatePhraseGrounding(unittest.TestCase):
    def test_simple(self):
        predictions = [[((0, 1), torch.tensor([[0.1, 0.1, 0.2, 0.2]]))]]
        targets = [[((0, 1), torch.tensor([[0.1, 0.1, 0.2, 0.2]]))]]
        outputs = Task(Task.Config()).execute(Task.Inputs(predictions=predictions, targets=targets))
        self.assertEqual(outputs.precision, 1.0)
        self.assertEqual(outputs.recall, 1.0)

        predictions = [[((0, 1), torch.tensor([[0.1, 0.1, 0.2, 0.2], [0, 0, 1.0, 1.0]]))]]
        outputs = Task(Task.Config()).execute(Task.Inputs(predictions=predictions, targets=targets))
        self.assertEqual(outputs.precision, 1.0)
        self.assertEqual(outputs.recall, 1.0)

        predictions = [[((0, 1), torch.tensor([[0.8, 0.8, 0.9, 0.9], [0, 0, 1.0, 1.0]]))]]
        outputs = Task(Task.Config()).execute(Task.Inputs(predictions=predictions, targets=targets))
        self.assertEqual(outputs.precision, 0.0)
        self.assertEqual(outputs.recall, 0.0)

        predictions = [[((0, 1), torch.tensor([[0.1, 0.1, 0.2, 0.2]])), ((1, 2), torch.tensor([[0.1, 0.1, 0.2, 0.2]]))]]
        outputs = Task(Task.Config()).execute(Task.Inputs(predictions=predictions, targets=targets))
        self.assertEqual(outputs.precision, 1.0)  # Predictions with wrong text span are ignored.
        self.assertEqual(outputs.recall, 1.0)

        # Tuple might be converted to a list. This happens when CUDA is used.
        predictions = [[[[0, 1], torch.tensor([[0.1, 0.1, 0.2, 0.2]])], ([1, 2], torch.tensor([[0.1, 0.1, 0.2, 0.2]]))]]
        outputs = Task(Task.Config()).execute(Task.Inputs(predictions=predictions, targets=targets))
        self.assertEqual(outputs.precision, 1.0)  # Predictions with wrong text span are ignored.
        self.assertEqual(outputs.recall, 1.0)

        predictions = [[]]
        outputs = Task(Task.Config()).execute(Task.Inputs(predictions=predictions, targets=targets))
        self.assertEqual(outputs.precision, 0.0)  # No predictions, return zero.
        self.assertEqual(outputs.recall, 0.0)

        predictions = [[((0, 1), torch.zeros(0, 4))]]
        outputs = Task(Task.Config()).execute(Task.Inputs(predictions=predictions, targets=targets))
        self.assertEqual(outputs.precision, 0.0)
        self.assertEqual(outputs.recall, 0.0)
