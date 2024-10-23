import copy
import unittest
from irisml.tasks.convert_key_value_pairs_to_key_value_pair_labels import Task


class TestConvertKeyValuePairsToKeyValuePairLabels(unittest.TestCase):
    def test_simple(self):
        key_value_pairs = [
            {
                "image_description": "Description",
                "number_of_chinchillas": 3,
                "activity": "sleeping"
            }
        ]
        expected_output = [
            {
                "image_description": {"value": "Description"},
                "number_of_chinchillas": {"value": 3},
                "activity": {"value": "sleeping"}
            }
        ]
        kvp_before_execution = copy.deepcopy(key_value_pairs)
        outputs = Task(Task.Config()).execute(Task.Inputs(key_value_pairs=key_value_pairs))
        self.assertEqual(outputs.key_value_pair_labels, expected_output)
        self.assertEqual(key_value_pairs, kvp_before_execution)

    def test_simple_two_dicts(self):
        key_value_pairs = [
            {
                "image_description": "Description",
                "number_of_chinchillas": 3,
                "activity": "sleeping"
            },
            {
                "image_description": "Description 2",
                "number_of_chinchillas": 1,
                "activity": "eating"
            }
        ]
        expected_output = [
            {
                "image_description": {"value": "Description"},
                "number_of_chinchillas": {"value": 3},
                "activity": {"value": "sleeping"}
            },
            {
                "image_description": {"value": "Description 2"},
                "number_of_chinchillas": {"value": 1},
                "activity": {"value": "eating"}
            }
        ]
        kvp_before_execution = copy.deepcopy(key_value_pairs)
        outputs = Task(Task.Config()).execute(Task.Inputs(key_value_pairs=key_value_pairs))
        self.assertEqual(outputs.key_value_pair_labels, expected_output)
        self.assertEqual(key_value_pairs, kvp_before_execution)

    def test_list(self):
        key_value_pairs = [
            {
                "defects": [
                    {
                        "defect_type": "scratch",
                        "explanation": "Long, thin mark"
                    },
                    {
                        "defect_type": "dent",
                        "explanation": "Indented area in upper left"
                    }
                ]
            }
        ]
        expected_output = [
            {
                "defects": {
                    "value": [
                        {
                            "defect_type": {"value": "scratch"},
                            "explanation": {"value": "Long, thin mark"}
                        },
                        {
                            "defect_type": {"value": "dent"},
                            "explanation": {"value": "Indented area in upper left"}
                        }
                    ]
                }
            }
        ]
        kvp_before_execution = copy.deepcopy(key_value_pairs)
        outputs = Task(Task.Config()).execute(Task.Inputs(key_value_pairs=key_value_pairs))
        self.assertEqual(outputs.key_value_pair_labels, expected_output)
        self.assertEqual(key_value_pairs, kvp_before_execution)

    def test_nested_object(self):
        key_value_pairs = [
            {
                "brand_sentiment": {
                    "has_non_contoso_brands": False,
                    "contoso_specific": {
                        "sentiment": "very positive",
                        "logos": [
                            "text", "rgb"
                        ]
                    }
                }
            }
        ]
        expected_output = [
            {
                "brand_sentiment": {
                    "value": {
                        "has_non_contoso_brands": {"value": False},
                        "contoso_specific": {
                            "value": {
                                "sentiment": {"value": "very positive"},
                                "logos": {
                                    "value": [
                                        {"value": "text"},
                                        {"value": "rgb"}
                                    ]
                                }
                            }
                        }
                    }
                }
            }
        ]
        kvp_before_execution = copy.deepcopy(key_value_pairs)
        outputs = Task(Task.Config()).execute(Task.Inputs(key_value_pairs=key_value_pairs))
        self.assertEqual(outputs.key_value_pair_labels, expected_output)
        self.assertEqual(key_value_pairs, kvp_before_execution)
