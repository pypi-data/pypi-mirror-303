import dataclasses
import logging

import irisml.core

logger = logging.getLogger(__name__)


class Task(irisml.core.TaskBase):
    """Converts an output as defined in the OpenAI structured outputs API https://platform.openai.com/docs/guides/structured-outputs/example-response to the key-value pair label format
    as defined in the "fields" field of the vision-datasets format: https://github.com/microsoft/vision-datasets/blob/main/COCO_DATA_FORMAT.md#keyvaluepair-dataset.

    Inputs:
        key_value_pairs (list[dict]): A list of output dicts as defined by the OpenAI structured outputs API. An example for a VQA task is
        {
            "answer": "A",
            "rationale": "The dog appears to be running."
        }
    Outputs:
        key_value_pair_labels (list[dict]): A dictionary compatible with the vision-datasets key-value pair annotation definition. An example for the same VQA task is
        {
            "answer": {"value": "A"},
            "rationale": {"value": "The dog appears to be running."}
        }

    """
    VERSION = "0.1.0"

    @dataclasses.dataclass
    class Inputs:
        key_value_pairs: list[dict]

    @dataclasses.dataclass
    class Outputs:
        key_value_pair_labels: list[dict]

    def _convert_output_to_prediction_format(self, key_value_pairs: dict):
        """
        Changes are:
        - Change the value of each field from the value itself to a dictionary of {"value": <value>}, with the exception of the outermost result object and objects in lists.
        """
        def convert_output_recursively(pairs, wrap_value):
            if isinstance(pairs, dict):
                pairs = {k: convert_output_recursively(v, wrap_value=True) for k, v in pairs.items()}
                return {"value": pairs} if wrap_value else pairs
            elif isinstance(pairs, list):
                pairs = [convert_output_recursively(p, wrap_value=not isinstance(p, dict)) for p in pairs]
                return {"value": pairs} if wrap_value else pairs
            else:
                return {"value": pairs}

        converted = convert_output_recursively(key_value_pairs, wrap_value=False)
        logger.info(f'Converted key-value pair to key-value pair label format: \n{converted}')

        return converted

    def execute(self, inputs):
        key_value_pair_labels = [self._convert_output_to_prediction_format(kvp) for kvp in inputs.key_value_pairs]
        return self.Outputs(key_value_pair_labels)

    def dry_run(self, inputs):
        return self.execute(inputs.key_value_pairs)
