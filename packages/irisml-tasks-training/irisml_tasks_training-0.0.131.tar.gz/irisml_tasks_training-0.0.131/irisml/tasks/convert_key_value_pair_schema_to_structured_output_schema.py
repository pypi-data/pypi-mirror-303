import copy
import dataclasses
import logging
import re

import irisml.core

logger = logging.getLogger(__name__)


class Task(irisml.core.TaskBase):
    """Converts a Field Schema as defined in the vision-datasets KeyValuePair dataset schema format (https://github.com/microsoft/vision-datasets/blob/main/COCO_DATA_FORMAT.md#keyvaluepair-dataset)
    to the structured output json_schema as defined in the OpenAI structured outputs API documentation (https://platform.openai.com/docs/guides/structured-outputs/supported-schemas).

    Inputs:
        schema (dict): A vision-datasets KeyValuePair Field Schema. An example for a VQA task is
            {
                "name": "Visual question-answering schema",
                "description": "Given an image, responds with the answer to the provided question.",
                "fieldSchema": {  // The name of this field can be configured in the task Config.
                    "answer": {
                        "type": "string",
                        "description": "Answer to the question given the provided image.",
                        "classes": {
                            "A": {"description": "Answer choice A."},
                            "B": {"description": ""},
                            "C": {"description": ""},
                            "D": {"description": ""}
                        }
                    }
                }
            }
            Note that one alternative to the "classes" field is the usage of "enum" and "enumDescriptions" together; for instance, instead of the "classes" field above, an alternative is
            "enum": ["A", "B", "C", "D"],
            "enumDescriptions": {
                "A": "Answer choice A."
            }
            More examples can be found at https://github.com/microsoft/vision-datasets/blob/main/DATA_PREPARATION.md and https://github.com/microsoft/vision-datasets/blob/main/tests/resources/util.py.
    Config:
        schema_field_name (str): The key in the input schema dictionary that will hold the schema.
        definitions_field_name (str): The key in the input schema dictionary that will hold the definitions that the schema may reference.
    Outputs:
        json_schema (dict): A json_schema compatible with structured outputs in the OpenAI API. An example for the same VQA task is
            {
                "name": "Visual_question-answering_schema",
                "description": "Given an image, responds with the answer to the provided question.",
                "strict": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "answer": {
                            "type": "string",
                            "description": "Answer to the question given the provided image.\nFor reference, more details for a few of the possible values include:\nA: Answer choice A.",
                            "enum": ["A", "B", "C", "D"]
                        }
                    },
                    "additionalProperties": False,
                    "required": [
                        "answer"
                    ]
                }
            }

    """
    VERSION = "0.3.0"

    @dataclasses.dataclass
    class Inputs:
        schema: dict

    @dataclasses.dataclass
    class Config:
        schema_field_name: str = "fieldSchema"
        definitions_field_name: str = "definitions"

    @dataclasses.dataclass
    class Outputs:
        json_schema: dict

    def _apply_name_regex(self, name: str):
        # Apply regex to name as specified by OpenAI API: ^[a-zA-Z0-9_-]+$
        name = name.strip()
        name = re.sub(r"\s+", "_", name)
        name = re.sub(r"[^a-zA-Z0-9_-]", "", name)
        return name

    def convert_field_schema_to_structured_output_format(self, schema: dict, schema_field_name: str, definitions_field_name: str):
        """
        Changes on the root level:
        - Apply a regex to the "name" field if it exists.
        - Add a "strict": True field.
        - Replace 'fieldSchema' or specified schema_field_name with a 'schema' field that has explicit type 'object' and move the the field schema key to 'schema' -> 'properties'.
        - Replace 'definitions' with a '$defs' field inside 'schema'.

        Changes on the key level:
        - Convert ClassSchema 'classes' keys or 'enum' and 'enumDescriptions' keys to 'enum' format and add descriptions to the field description.
        - Remove 'includeGrounding' fields.
        - Remove 'kind' and 'examples' fields. For 'examples', add examples to the field description.
        - Add 'additionalProperties': 'false' and 'required' list for every 'object' type.
        - Replace references to 'definitions' with '$defs'.
        Details discussed in the OpenAI documentation: https://platform.openai.com/docs/guides/structured-outputs/all-fields-must-be-required.
        """
        if schema_field_name not in schema:
            raise ValueError(f"The input schema must have the key '{schema_field_name}' that stores the root schema.")

        converted = {}
        if 'name' in schema:
            converted['name'] = self._apply_name_regex(schema['name'])
        if 'description' in schema:
            converted['description'] = schema['description']
        converted['strict'] = True
        if schema_field_name in schema:
            converted['schema'] = {}
            converted['schema']['type'] = 'object'
            converted['schema']['properties'] = copy.deepcopy(schema[schema_field_name])
        if definitions_field_name in schema:
            converted['schema']['$defs'] = copy.deepcopy(schema[definitions_field_name])

        def convert_field_schema_recursively(field_schema: dict):
            # 'classes' is compatible with vision-datasets. 'enum' and 'enumDescriptions' is another accepted format that is more aligned with JSON Schema.
            enum_field_name = None
            if 'classes' in field_schema:
                enum_field_name = 'classes'
            elif 'enumDescriptions' in field_schema and 'enum' in field_schema:
                enum_field_name = 'enumDescriptions'
            if enum_field_name:
                if enum_field_name == 'classes':
                    field_schema['enum'] = list(field_schema['classes'].keys())
                    class_descriptions = [(c, field_schema['classes'][c].get('description')) for c in field_schema['classes']]
                elif enum_field_name == 'enumDescriptions':
                    class_descriptions = [(c, field_schema['enumDescriptions'][c]) for c in field_schema['enumDescriptions']]

                non_empty_class_descriptions = [f"{c}: {d}" for c, d in class_descriptions if d]
                if non_empty_class_descriptions:
                    if len(non_empty_class_descriptions) == len(field_schema['enum']):
                        description_leading_string = 'For reference, more details for each of the possible values are:'
                    else:
                        description_leading_string = 'For reference, more details for a few of the possible values include:'
                    # Use chr(10) to join f-string for newline character since before python 3.12, f-string expressions cannot include backslashes
                    if 'description' in field_schema and field_schema['description']:
                        field_schema['description'] += f"\n{description_leading_string}\n{chr(10).join(non_empty_class_descriptions)}"
                    else:
                        field_schema['description'] = f"{description_leading_string}\n{chr(10).join(non_empty_class_descriptions)}"
                del field_schema[enum_field_name]

            if '$ref' in field_schema:
                field_schema['$ref'] = field_schema['$ref'].replace(definitions_field_name, '$defs', 1)
            if 'kind' in field_schema:
                del field_schema['kind']
            if 'examples' in field_schema:
                if 'description' in field_schema and field_schema['description']:
                    field_schema['description'] += f"\nSome examples of valid values include: {', '.join(field_schema['examples'])}"
                else:
                    field_schema['description'] = f"Some examples of valid values include: {', '.join(field_schema['examples'])}"
                del field_schema['examples']
            if 'includeGrounding' in field_schema:
                del field_schema['includeGrounding']
            if 'items' in field_schema:
                convert_field_schema_recursively(field_schema['items'])
            if 'properties' in field_schema:
                for k in field_schema['properties'].keys():
                    convert_field_schema_recursively(field_schema['properties'][k])
                field_schema['additionalProperties'] = False
                field_schema['required'] = list(field_schema['properties'].keys())

        convert_field_schema_recursively(converted['schema'])
        if '$defs' in converted['schema']:
            for definition in converted['schema']['$defs']:
                convert_field_schema_recursively(converted['schema']['$defs'][definition])
        logger.info(f'Converted schema to structured output format: \n{converted}')

        return converted

    def execute(self, inputs):
        json_schema = self.convert_field_schema_to_structured_output_format(inputs.schema, self.config.schema_field_name, self.config.definitions_field_name)
        return self.Outputs(json_schema)

    def dry_run(self, inputs):
        return self.execute(inputs.schema)
