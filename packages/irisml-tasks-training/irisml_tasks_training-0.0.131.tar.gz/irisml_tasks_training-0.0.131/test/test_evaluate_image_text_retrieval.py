import unittest
import torch
from irisml.tasks.evaluate_image_text_retrieval import Task


class TestEvaluateImageTextRetrieval(unittest.TestCase):
    def test_zero_recall(self):
        image_features = torch.ones((100, 2))
        text_features = torch.ones((300, 2))
        targets = torch.zeros((300,), dtype=torch.long)

        outputs = Task(Task.Config()).execute(Task.Inputs(image_features, text_features, targets))
        self.assertEqual(outputs.text_retrieval_recall_1, 0.01)
        self.assertEqual(outputs.text_retrieval_recall_5, 0.01)
        self.assertEqual(outputs.text_retrieval_recall_10, 0.01)
        self.assertEqual(outputs.image_retrieval_recall_1, 0)
        self.assertEqual(outputs.image_retrieval_recall_5, 0)
        self.assertEqual(outputs.image_retrieval_recall_10, 0)

    def test_perfect_recall(self):
        image_features = torch.ones((10, 2))
        text_features = torch.ones((10, 2))
        targets = torch.arange(10, dtype=torch.long)
        for i in range(10):
            image_features[i][0] = i + 1
            text_features[i][0] = i + 1

        outputs = Task(Task.Config()).execute(Task.Inputs(image_features, text_features, targets))
        self.assertEqual(outputs.text_retrieval_recall_1, 1)
        self.assertEqual(outputs.text_retrieval_recall_5, 1)
        self.assertEqual(outputs.text_retrieval_recall_10, 1)
        self.assertEqual(outputs.image_retrieval_recall_1, 1)
        self.assertEqual(outputs.image_retrieval_recall_5, 1)
        self.assertEqual(outputs.image_retrieval_recall_10, 1)
