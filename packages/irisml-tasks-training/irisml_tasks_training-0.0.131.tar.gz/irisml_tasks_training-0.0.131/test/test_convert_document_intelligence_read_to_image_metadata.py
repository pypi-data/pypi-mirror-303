import unittest
from irisml.tasks.convert_document_intelligence_read_predictions_to_image_metadata import Task


class TestConvertDocumentIntelligenceReadPredictionsToImageMetadata(unittest.TestCase):
    def test_simple(self):
        inputs = Task.Inputs(predictions=[{'content': 'A'}, {'content': 'B'}, {'content': 'C'}])
        outputs = Task(Task.Config()).execute(inputs)
        self.assertEqual(outputs.image_metadata, [{'ocr': 'A'}, {'ocr': 'B'}, {'ocr': 'C'}])

    def test_exception(self):
        inputs = Task.Inputs(predictions=['', ''])
        with self.assertRaises(ValueError):
            Task(Task.Config()).execute(inputs)
