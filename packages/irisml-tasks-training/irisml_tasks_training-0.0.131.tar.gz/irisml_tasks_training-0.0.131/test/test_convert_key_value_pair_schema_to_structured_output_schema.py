import copy
import unittest
from irisml.tasks.convert_key_value_pair_schema_to_structured_output_schema import Task


class TestConvertKeyValuePairSchemaToStructuredOutputSchema(unittest.TestCase):
    simple_schema = {
        "name": "Simple Schema",
        "description": "A simple schema with only root keys.",
        "fieldSchema": {
            "image_description": {
                "type": "string",
                "description": "Description of the image in a few sentences, with attention to detail."
            },
            "number_of_chinchillas": {
                "type": "integer",
                "description": "Number of chinchillas visible in the image."
            },
            "activity": {
                "type": "string",
                "description": "The most salient activity of the chinchillas in the image.",
                "classes": {
                    "sleeping": {"description": "Often in a supine position."},
                    "running": {"description": ""},
                    "eating": {"description": "Consuming solid foods."}
                }
            }
        }
    }
    simple_list_schema = {
        "name": "defect detection",
        "description": "detect the defects in the image",
        "fieldSchema": {
            "defects": {
                "type": "array",
                "description": "The defect types present in the image.",
                "items": {
                    "type": "string",
                    "description": "The type of defect detected",
                    "classes": {
                        "scratch": {},
                        "dent": {},
                        "discoloration": {},
                        "crack": {}
                    },
                    "includeGrounding": True
                }
            }
        }
    }
    complex_list_schema_invalid_name_char = {
        "name": "Defect detection!",
        "description": "Detect the defects!",
        "fieldSchema": {
            "defects": {
                "type": "array",
                "description": "The defect types present in the image.",
                "items": {
                    "type": "object",
                    "properties": {
                        "defect_type": {
                            "type": "string",
                            "description": "The type of defect detected",
                            "classes": {
                                "scratch": {},
                                "dent": {},
                                "discoloration": {},
                                "crack": {}
                            },
                            "includeGrounding": True
                        },
                        "explanation": {
                            "type": "string",
                            "description": "Rationale for the defects identified."
                        }
                    }
                }
            }
        }
    }
    nested_object_schema = {
        "name": "Brand sentiment identification",
        "description": "Identify various attributes pertaining to brand sentiment.",
        "fieldSchema": {
            "brand_sentiment": {
                "type": "object",
                "description": "Attributes of sentiment toward brands depicted in the image.",
                "properties": {
                    "has_non_contoso_brands": {
                        "type": "boolean",
                        "description": "Whether the image depicts or contains anything about non-Contoso brands."
                    },
                    "contoso_specific": {
                        "type": "object",
                        "description": "Sentiment related specifically to the company Contoso.",
                        "properties": {
                            "sentiment": {
                                "type": "string",
                                "description": "Sentiment toward the brand as depicted in the image.",
                                "classes": {
                                    "very positive": {"description": "The highest possible positivity"},
                                    "somewhat positive": {},
                                    "neutral": {},
                                    "somewhat negative": {},
                                    "very negative": {"description": "The lowest possible positivity"}
                                }
                            },
                            "logos": {
                                "type": "array",
                                "description": "The types of Contoso logos present in the image.",
                                "items": {
                                    "type": "string",
                                    "description": "The type of Contoso logo in the image.",
                                    "classes": {
                                        "text": {"description": "The text-only logo"},
                                        "grayscale": {"description": "The grayscale logo"},
                                        "rgb": {"description": "The full-color logo"}
                                    },
                                    "includeGrounding": True
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    def test_simple_schema(self):
        schema = copy.deepcopy(self.simple_schema)
        expected_output = {
            "name": "Simple_Schema",
            "description": "A simple schema with only root keys.",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {
                    "image_description": {
                        "type": "string",
                        "description": "Description of the image in a few sentences, with attention to detail."
                    },
                    "number_of_chinchillas": {
                        "type": "integer",
                        "description": "Number of chinchillas visible in the image."
                    },
                    "activity": {
                        "type": "string",
                        "description": "The most salient activity of the chinchillas in the image.\n"
                        "For reference, more details for a few of the possible values include:\nsleeping: Often in a supine position.\neating: Consuming solid foods.",
                        "enum": ["sleeping", "running", "eating"]
                    }
                },
                "additionalProperties": False,
                "required": [
                    "image_description", "number_of_chinchillas", "activity"
                ]
            }
        }
        schema_before_execution = copy.deepcopy(schema)
        outputs = Task(Task.Config(schema_field_name="fieldSchema", definitions_field_name="definitions")).execute(Task.Inputs(schema=schema))
        self.assertEqual(outputs.json_schema, expected_output)
        self.assertEqual(schema, schema_before_execution)

        schema['fields'] = schema.pop('fieldSchema')
        schema_before_execution = copy.deepcopy(schema)
        outputs = Task(Task.Config(schema_field_name="fields", definitions_field_name="definitions")).execute(Task.Inputs(schema=schema))
        self.assertEqual(outputs.json_schema, expected_output)
        self.assertEqual(schema, schema_before_execution)

    def test_simple_list_schema(self):
        schema = copy.deepcopy(self.simple_list_schema)
        expected_output = {
            "name": "defect_detection",
            "description": "detect the defects in the image",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {
                    "defects": {
                        "type": "array",
                        "description": "The defect types present in the image.",
                        "items": {
                            "type": "string",
                            "description": "The type of defect detected",
                            "enum": ["scratch", "dent", "discoloration", "crack"]
                        }
                    }
                },
                "additionalProperties": False,
                "required": [
                    "defects"
                ]
            }
        }
        schema_before_execution = copy.deepcopy(schema)
        outputs = Task(Task.Config(schema_field_name="fieldSchema", definitions_field_name="definitions")).execute(Task.Inputs(schema=schema))
        self.assertEqual(outputs.json_schema, expected_output)
        self.assertEqual(schema, schema_before_execution)

        schema['fields'] = schema.pop('fieldSchema')
        schema_before_execution = copy.deepcopy(schema)
        outputs = Task(Task.Config(schema_field_name="fields", definitions_field_name="definitions")).execute(Task.Inputs(schema=schema))
        self.assertEqual(outputs.json_schema, expected_output)
        self.assertEqual(schema, schema_before_execution)

    def test_complex_list_schema_invalid_name_char(self):
        schema = copy.deepcopy(self.complex_list_schema_invalid_name_char)
        expected_output = {
            "name": "Defect_detection",
            "description": "Detect the defects!",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {
                    "defects": {
                        "type": "array",
                        "description": "The defect types present in the image.",
                        "items": {
                            "type": "object",
                            "properties": {
                                "defect_type": {
                                    "type": "string",
                                    "description": "The type of defect detected",
                                    "enum": ["scratch", "dent", "discoloration", "crack"]
                                },
                                "explanation": {
                                    "type": "string",
                                    "description": "Rationale for the defects identified."
                                }
                            },
                            "additionalProperties": False,
                            "required": [
                                "defect_type", "explanation"
                            ]
                        }
                    }
                },
                "additionalProperties": False,
                "required": [
                    "defects"
                ]
            }
        }
        schema_before_execution = copy.deepcopy(schema)
        outputs = Task(Task.Config(schema_field_name="fieldSchema", definitions_field_name="definitions")).execute(Task.Inputs(schema=schema))
        self.assertEqual(outputs.json_schema, expected_output)
        self.assertEqual(schema, schema_before_execution)

        schema['fields'] = schema.pop('fieldSchema')
        schema_before_execution = copy.deepcopy(schema)
        outputs = Task(Task.Config(schema_field_name="fields", definitions_field_name="definitions")).execute(Task.Inputs(schema=schema))
        self.assertEqual(outputs.json_schema, expected_output)
        self.assertEqual(schema, schema_before_execution)

    def test_nested_object_schema(self):
        schema = copy.deepcopy(self.nested_object_schema)
        expected_output = {
            "name": "Brand_sentiment_identification",
            "description": "Identify various attributes pertaining to brand sentiment.",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {
                    "brand_sentiment": {
                        "type": "object",
                        "description": "Attributes of sentiment toward brands depicted in the image.",
                        "properties": {
                            "has_non_contoso_brands": {
                                "type": "boolean",
                                "description": "Whether the image depicts or contains anything about non-Contoso brands."
                            },
                            "contoso_specific": {
                                "type": "object",
                                "description": "Sentiment related specifically to the company Contoso.",
                                "properties": {
                                    "sentiment": {
                                        "type": "string",
                                        "description": "Sentiment toward the brand as depicted in the image.\n"
                                        "For reference, more details for a few of the possible values include:\nvery positive: The highest possible positivity\n"
                                        "very negative: The lowest possible positivity",
                                        "enum": ["very positive", "somewhat positive", "neutral", "somewhat negative", "very negative"]
                                    },
                                    "logos": {
                                        "type": "array",
                                        "description": "The types of Contoso logos present in the image.",
                                        "items": {
                                            "type": "string",
                                            "description": "The type of Contoso logo in the image.\n"
                                            "For reference, more details for each of the possible values are:\n"
                                            "text: The text-only logo\ngrayscale: The grayscale logo\nrgb: The full-color logo",
                                            "enum": ["text", "grayscale", "rgb"]
                                        }
                                    }
                                },
                                "additionalProperties": False,
                                "required": [
                                    "sentiment", "logos"
                                ]
                            }
                        },
                        "additionalProperties": False,
                        "required": [
                            "has_non_contoso_brands", "contoso_specific"
                        ]
                    }
                },
                "additionalProperties": False,
                "required": [
                    "brand_sentiment"
                ]
            }
        }
        schema_before_execution = copy.deepcopy(schema)
        outputs = Task(Task.Config(schema_field_name="fieldSchema", definitions_field_name="definitions")).execute(Task.Inputs(schema=schema))
        self.assertEqual(outputs.json_schema, expected_output)
        self.assertEqual(schema, schema_before_execution)

        schema['fields'] = schema.pop('fieldSchema')
        schema_before_execution = copy.deepcopy(schema)
        outputs = Task(Task.Config(schema_field_name="fields", definitions_field_name="definitions")).execute(Task.Inputs(schema=schema))
        self.assertEqual(outputs.json_schema, expected_output)
        self.assertEqual(schema, schema_before_execution)

    def test_simple_schema_with_definitions(self):
        schema = copy.deepcopy(self.simple_schema)
        schema["definitions"] = {
            "activity": {
                "type": "string",
                "description": "The most salient activity of the chinchillas in the image.",
                "classes": {
                    "sleeping": {"description": "Often in a supine position."},
                    "running": {"description": ""},
                    "eating": {"description": "Consuming solid foods."}
                }
            }
        }
        schema['fieldSchema']['activity'] = {'$ref': '#/definitions/activity'}
        expected_output = {
            "name": "Simple_Schema",
            "description": "A simple schema with only root keys.",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {
                    "image_description": {
                        "type": "string",
                        "description": "Description of the image in a few sentences, with attention to detail."
                    },
                    "number_of_chinchillas": {
                        "type": "integer",
                        "description": "Number of chinchillas visible in the image."
                    },
                    "activity": {
                        "$ref": "#/$defs/activity"
                    }
                },
                "$defs": {
                    "activity": {
                        "type": "string",
                        "description": "The most salient activity of the chinchillas in the image.\n"
                        "For reference, more details for a few of the possible values include:\nsleeping: Often in a supine position.\neating: Consuming solid foods.",
                        "enum": ["sleeping", "running", "eating"]
                    }
                },
                "additionalProperties": False,
                "required": [
                    "image_description", "number_of_chinchillas", "activity"
                ]
            }
        }
        schema_before_execution = copy.deepcopy(schema)
        outputs = Task(Task.Config(schema_field_name="fieldSchema", definitions_field_name="definitions")).execute(Task.Inputs(schema=schema))
        self.assertEqual(outputs.json_schema, expected_output)
        self.assertEqual(schema, schema_before_execution)

        schema['fields'] = schema.pop('fieldSchema')
        schema_before_execution = copy.deepcopy(schema)
        outputs = Task(Task.Config(schema_field_name="fields", definitions_field_name="definitions")).execute(Task.Inputs(schema=schema))
        self.assertEqual(outputs.json_schema, expected_output)
        self.assertEqual(schema, schema_before_execution)

    def test_nested_object_schema_with_definitions(self):
        schema = copy.deepcopy(self.nested_object_schema)
        schema["definitions"] = {
            "logo": {
                "type": "object",
                "description": "The type of Contoso logo in the image.",
                "properties": {
                    "type": {
                        "type": "string",
                        "description": "The type of Contoso logo in the image.",
                        "classes": {
                            "text": {"description": "The text-only logo"},
                            "grayscale": {"description": "The grayscale logo"},
                            "rgb": {"description": "The full-color logo"}
                        },
                        "includeGrounding": True
                    },
                    "inner_logos": {
                        "type": "array",
                        "description": "List of logos that are subcomponents of this logo.",
                        "items": {
                            "$ref": "#/definitions/logo"
                        }
                    }
                }
            }
        }
        schema["fieldSchema"]["brand_sentiment"]["properties"]["contoso_specific"]["properties"]["logos"]["items"] = {"$ref": "#/definitions/logo"}
        expected_output = {
            "name": "Brand_sentiment_identification",
            "description": "Identify various attributes pertaining to brand sentiment.",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {
                    "brand_sentiment": {
                        "type": "object",
                        "description": "Attributes of sentiment toward brands depicted in the image.",
                        "properties": {
                            "has_non_contoso_brands": {
                                "type": "boolean",
                                "description": "Whether the image depicts or contains anything about non-Contoso brands."
                            },
                            "contoso_specific": {
                                "type": "object",
                                "description": "Sentiment related specifically to the company Contoso.",
                                "properties": {
                                    "sentiment": {
                                        "type": "string",
                                        "description": "Sentiment toward the brand as depicted in the image.\n"
                                        "For reference, more details for a few of the possible values include:\nvery positive: The highest possible positivity\n"
                                        "very negative: The lowest possible positivity",
                                        "enum": ["very positive", "somewhat positive", "neutral", "somewhat negative", "very negative"]
                                    },
                                    "logos": {
                                        "type": "array",
                                        "description": "The types of Contoso logos present in the image.",
                                        "items": {
                                            "$ref": "#/$defs/logo"
                                        }
                                    }
                                },
                                "additionalProperties": False,
                                "required": [
                                    "sentiment", "logos"
                                ]
                            }
                        },
                        "additionalProperties": False,
                        "required": [
                            "has_non_contoso_brands", "contoso_specific"
                        ]
                    }
                },
                "$defs": {
                    "logo": {
                        "type": "object",
                        "description": "The type of Contoso logo in the image.",
                        "properties": {
                            "type": {
                                "type": "string",
                                "description": "The type of Contoso logo in the image.\n"
                                "For reference, more details for each of the possible values are:\n"
                                "text: The text-only logo\ngrayscale: The grayscale logo\nrgb: The full-color logo",
                                "enum": ["text", "grayscale", "rgb"]
                            },
                            "inner_logos": {
                                "type": "array",
                                "description": "List of logos that are subcomponents of this logo.",
                                "items": {
                                    "$ref": "#/$defs/logo"
                                }
                            }
                        },
                        "additionalProperties": False,
                        "required": [
                            "type", "inner_logos"
                        ]
                    }
                },
                "additionalProperties": False,
                "required": [
                    "brand_sentiment"
                ]
            }
        }
        schema_before_execution = copy.deepcopy(schema)
        outputs = Task(Task.Config(schema_field_name="fieldSchema", definitions_field_name="definitions")).execute(Task.Inputs(schema=schema))
        self.assertEqual(outputs.json_schema, expected_output)
        self.assertEqual(schema, schema_before_execution)

        schema['fields'] = schema.pop('fieldSchema')
        schema_before_execution = copy.deepcopy(schema)
        outputs = Task(Task.Config(schema_field_name="fields", definitions_field_name="definitions")).execute(Task.Inputs(schema=schema))
        self.assertEqual(outputs.json_schema, expected_output)
        self.assertEqual(schema, schema_before_execution)

    def test_schema_with_definitions_field(self):
        schema = {
            "name": "definitions field schema",
            "description": "A simple schema to test whether the definitions field name remains unchanged after conversion.",
            "fieldSchema": {
                "definitions": {
                    "$ref": "#/definitions/definitions"
                }
            },
            "definitions": {
                "definitions": {
                    "type": "string",
                    "description": "The requested definitions."
                }
            }
        }
        expected_output = {
            "name": "definitions_field_schema",
            "description": "A simple schema to test whether the definitions field name remains unchanged after conversion.",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {
                    "definitions": {
                        "$ref": "#/$defs/definitions"
                    }
                },
                "$defs": {
                    "definitions": {
                        "type": "string",
                        "description": "The requested definitions."
                    }
                },
                "additionalProperties": False,
                "required": [
                    "definitions"
                ]
            }
        }
        schema_before_execution = copy.deepcopy(schema)
        outputs = Task(Task.Config(schema_field_name="fieldSchema", definitions_field_name="definitions")).execute(Task.Inputs(schema=schema))
        self.assertEqual(outputs.json_schema, expected_output)
        self.assertEqual(schema, schema_before_execution)

        schema['fields'] = schema.pop('fieldSchema')
        schema_before_execution = copy.deepcopy(schema)
        outputs = Task(Task.Config(schema_field_name="fields", definitions_field_name="definitions")).execute(Task.Inputs(schema=schema))
        self.assertEqual(outputs.json_schema, expected_output)
        self.assertEqual(schema, schema_before_execution)

    def test_schema_with_invalid_field_schema(self):
        schema = copy.deepcopy(self.simple_schema)
        schema["fieldDefinitions"] = schema.pop("fieldSchema")
        with self.assertRaisesRegex(ValueError, "The input schema must have the key 'fieldSchema' that stores the root schema."):
            Task(Task.Config(schema_field_name="fieldSchema", definitions_field_name="definitions")).execute(Task.Inputs(schema=schema))

    def test_schema_with_kind_field(self):
        schema = {
            "name": "kind field schema",
            "description": "A simple schema to test whether the kind field is removed after conversion.",
            "fieldSchema": {
                "object_1": {
                    "type": "object",
                    "kind": "kind1",
                    "properties": {
                        "object_2": {
                            "type": "string",
                            "kind": "kind2"
                        }
                    }
                }
            }
        }
        expected_output = {
            "name": "kind_field_schema",
            "description": "A simple schema to test whether the kind field is removed after conversion.",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {
                    "object_1": {
                        "type": "object",
                        "properties": {
                            "object_2": {
                                "type": "string"
                            }
                        },
                        "additionalProperties": False,
                        "required": [
                            "object_2"
                        ]
                    }
                },
                "additionalProperties": False,
                "required": [
                    "object_1"
                ]
            }
        }
        schema_before_execution = copy.deepcopy(schema)
        outputs = Task(Task.Config(schema_field_name="fieldSchema", definitions_field_name="definitions")).execute(Task.Inputs(schema=schema))
        self.assertEqual(outputs.json_schema, expected_output)
        self.assertEqual(schema, schema_before_execution)

    def test_schema_with_examples_field(self):
        schema = {
            "name": "examples field schema",
            "description": "A simple schema to test whether the examples field is removed and added into the description after conversion.",
            "fieldSchema": {
                "object_1": {
                    "type": "object",
                    "properties": {
                        "object_2": {
                            "type": "string",
                            "examples": ["one", "two", "three"]
                        }
                    }
                }
            }
        }
        expected_output = {
            "name": "examples_field_schema",
            "description": "A simple schema to test whether the examples field is removed and added into the description after conversion.",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {
                    "object_1": {
                        "type": "object",
                        "properties": {
                            "object_2": {
                                "type": "string",
                                "description": "Some examples of valid values include: one, two, three"
                            }
                        },
                        "additionalProperties": False,
                        "required": [
                            "object_2"
                        ]
                    }
                },
                "additionalProperties": False,
                "required": [
                    "object_1"
                ]
            }
        }
        schema_before_execution = copy.deepcopy(schema)
        outputs = Task(Task.Config(schema_field_name="fieldSchema", definitions_field_name="definitions")).execute(Task.Inputs(schema=schema))
        self.assertEqual(outputs.json_schema, expected_output)
        self.assertEqual(schema, schema_before_execution)

    def test_schema_with_enum_descriptions_field(self):
        schema = copy.deepcopy(self.simple_list_schema)
        del schema["fieldSchema"]["defects"]["items"]["classes"]
        schema["fieldSchema"]["defects"]["items"]["enum"] = ["scratch", "dent", "discoloration", "crack"]
        schema["fieldSchema"]["defects"]["items"]["enumDescriptions"] = {
            "scratch": "A long, thin mark.",
            "discoloration": "Deviation from the expected color."
        }
        expected_output = {
            "name": "defect_detection",
            "description": "detect the defects in the image",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {
                    "defects": {
                        "type": "array",
                        "description": "The defect types present in the image.",
                        "items": {
                            "type": "string",
                            "description": "The type of defect detected\nFor reference, more details for a few of the possible values include:"
                            "\nscratch: A long, thin mark.\ndiscoloration: Deviation from the expected color.",
                            "enum": ["scratch", "dent", "discoloration", "crack"]
                        }
                    }
                },
                "additionalProperties": False,
                "required": [
                    "defects"
                ]
            }
        }
        schema_before_execution = copy.deepcopy(schema)
        outputs = Task(Task.Config(schema_field_name="fieldSchema", definitions_field_name="definitions")).execute(Task.Inputs(schema=schema))
        self.assertEqual(outputs.json_schema, expected_output)
        self.assertEqual(schema, schema_before_execution)
