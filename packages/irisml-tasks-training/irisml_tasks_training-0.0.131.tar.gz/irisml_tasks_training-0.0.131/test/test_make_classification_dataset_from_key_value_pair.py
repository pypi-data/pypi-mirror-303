import unittest
import PIL.Image
from irisml.tasks.make_classification_dataset_from_key_value_pair import Task


class TestMakeClassificationDatasetFromKeyValuePair(unittest.TestCase):
    def test_multiclass(self):
        kvp_dataset = [(('text', [(PIL.Image.new('RGB', (32, 32)), {})]), {'className': {'value': 'cat'}}),
                       (('text', [(PIL.Image.new('RGB', (32, 32)), {})]), {'className': {'value': 'dog'}})]

        schema = {'fieldSchema': {'className': {'type': 'string', 'classes': {'cat': {}, 'dog': {}}}}}

        outputs = Task(Task.Config(field_name='className')).execute(Task.Inputs(dataset=kvp_dataset, schema=schema))

        self.assertEqual(outputs.task_type, 'classification_multiclass')
        self.assertEqual(outputs.class_names, ['cat', 'dog'])
        self.assertEqual(outputs.num_classes, 2)
        self.assertEqual(len(outputs.dataset), 2)
        self.assertEqual(outputs.dataset[0][1].item(), 0)
        self.assertEqual(outputs.dataset[1][1].item(), 1)
        self.assertIsInstance(outputs.dataset[0][0], PIL.Image.Image)
        self.assertIsInstance(outputs.dataset[1][0], PIL.Image.Image)

    def test_multilabel(self):
        kvp_dataset = [(('text', [(PIL.Image.new('RGB', (32, 32)), {})]), {'classNames': {'value': [{'value': 'cat'}, {'value': 'dog'}]}}),
                       (('text', [(PIL.Image.new('RGB', (32, 32)), {})]), {'classNames': {'value': [{'value': 'dog'}]}})]

        schema = {'fieldSchema': {'classNames': {'type': 'array', 'items': {'type': 'string', 'classes': {'cat': {}, 'dog': {}}}}}}

        outputs = Task(Task.Config(field_name='classNames')).execute(Task.Inputs(dataset=kvp_dataset, schema=schema))

        self.assertEqual(outputs.task_type, 'classification_multilabel')
        self.assertEqual(outputs.class_names, ['cat', 'dog'])
        self.assertEqual(outputs.num_classes, 2)
        self.assertEqual(len(outputs.dataset), 2)
        self.assertEqual(outputs.dataset[0][1].tolist(), [1, 1])
        self.assertEqual(outputs.dataset[1][1].tolist(), [0, 1])
        self.assertIsInstance(outputs.dataset[0][0], PIL.Image.Image)
        self.assertIsInstance(outputs.dataset[1][0], PIL.Image.Image)
