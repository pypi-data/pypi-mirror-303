import unittest
import torch
from irisml.tasks.convert_classification_predictions_to_key_value_pair import Task


class TestConvertClassificationPredictionsToKeyValuePair(unittest.TestCase):
    def test_classification_multiclass(self):
        class_names = ['A', 'B', 'C']
        predictions = torch.tensor([[0.1, 0.2, 0.7], [0.3, 0.4, 0.3]])
        outputs = Task(Task.Config(task_type='classification_multiclass', field_name='field1')).execute(Task.Inputs(predictions=predictions, class_names=class_names))
        self.assertEqual(outputs.key_value_pairs, [{'field1': {'value': 'C'}}, {'field1': {'value': 'B'}}])

    def test_empty(self):
        class_names = ['A', 'B', 'C']
        predictions = torch.empty(0, 3)
        outputs = Task(Task.Config(task_type='classification_multiclass', field_name='field1')).execute(Task.Inputs(predictions=predictions, class_names=class_names))
        self.assertEqual(outputs.key_value_pairs, [])

    def test_classification_multilabel(self):
        class_names = ['A', 'B', 'C']
        predictions = torch.tensor([[0.8, 0.2, 0.7], [0.3, 0.4, 0.3]])
        outputs = Task(Task.Config(task_type='classification_multilabel', field_name='field1', prob_threshold=0.5)).execute(Task.Inputs(predictions=predictions, class_names=class_names))

        self.assertEqual(outputs.key_value_pairs, [{'field1': {'value': [{'value': 'A'}, {'value': 'C'}]}}, {'field1': {'value': []}}])

        outputs = Task(Task.Config(task_type='classification_multilabel', field_name='field1')).execute(Task.Inputs(predictions=predictions, class_names=class_names))
        self.assertEqual(outputs.key_value_pairs, [{'field1': {'value': [{'value': 'A'}]}}, {'field1': {'value': [{'value': 'B'}]}}])
