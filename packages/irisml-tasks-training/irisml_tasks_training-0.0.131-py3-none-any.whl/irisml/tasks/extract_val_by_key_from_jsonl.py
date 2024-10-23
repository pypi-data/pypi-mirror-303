import dataclasses
import json
import logging
import pathlib
import typing
import irisml.core

logger = logging.getLogger(__name__)


class Task(irisml.core.TaskBase):
    """Extract value for each entry in a JSONL by a key.

    Config:
        key (str): key to extract value
    """
    VERSION = '0.1.0'
    CACHE_ENABLED = False

    @dataclasses.dataclass
    class Inputs:
        jsonl_file_path: pathlib.Path

    @dataclasses.dataclass
    class Outputs:
        results: typing.List[typing.Any]

    @dataclasses.dataclass
    class Config:
        key: str

    def execute(self, inputs):
        logger.info(f"Extracting values from {inputs.jsonl_file_path}, by key {self.config.key}.")

        outputs = []
        with open(inputs.jsonl_file_path, 'r') as file:
            for line in file:
                data = json.loads(line)
                outputs.append(data[self.config.key])

        return self.Outputs(results=outputs)

    def dry_run(self, inputs):
        return self.execute(inputs)
