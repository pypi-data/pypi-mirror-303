import unittest
import pathlib
import tempfile
import json
from irisml.tasks.extract_val_by_key_from_jsonl import Task


class TestExtractValByKeyFromJsonl(unittest.TestCase):
    def test_extract_values(self):
        data = [{"a": 1, "b": 2},
                {"a": 3, "b": 4},
                {"a": 5, "b": 6}]

        with tempfile.TemporaryDirectory() as temp_dir:
            jsonl_file = pathlib.Path(temp_dir) / "test.jsonl"
            jsonl_file.write_text("\n".join([json.dumps(d) for d in data]))

            outputs = Task(Task.Config(key='a')).execute(Task.Inputs(jsonl_file_path=jsonl_file))
            self.assertEqual(outputs.results, [1, 3, 5])
