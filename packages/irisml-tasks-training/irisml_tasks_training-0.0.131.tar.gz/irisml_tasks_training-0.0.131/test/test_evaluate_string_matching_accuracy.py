import unittest
from irisml.tasks.evaluate_string_matching_accuracy import Task


class TestEvaluateStringMatchingAccuracy(unittest.TestCase):
    def test_simple(self):
        outputs = Task(Task.Config()).execute(Task.Inputs(['A', 'b', 'c'], ['a', 'B', 'C']))
        self.assertEqual(outputs.accuracy, 1.0)

        outputs = Task(Task.Config()).execute(Task.Inputs(['aa', 'bb', 'cc'], ['a', 'b', 'c']))
        self.assertEqual(outputs.accuracy, 0.0)

        outputs = Task(Task.Config()).execute(Task.Inputs(['aa', 'bb'], ['aa', 'bc']))
        self.assertEqual(outputs.accuracy, 0.5)
