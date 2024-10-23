import dataclasses
import json
import logging
import typing

import PIL.Image
import torch
from jinja2 import Template

import irisml.core

logger = logging.getLogger(__name__)


class Task(irisml.core.TaskBase):
    """Make a transform function to construct input images and text prompts for KeyValuePair(https://github.com/microsoft/vision-datasets/blob/main/COCO_DATA_FORMAT.md#keyvaluepair-dataset) dataset
      training/inference.
    Given an image transform T, a sample of dataset (text_dict, [(im1, meta1), (im2, meta2), key_value_pairs]) is transformed to (([T(im1), T(im2)], text prompt), key_value_pairs). Where text_dict is
      the optional text input for the annotation, im1 and im2 are input images (this can be either single-image or multi-image annotation), and meta1, meta2 are optional metadata dictionary for the
      images. key_value_pairs is the target, a dictionary of key-value pairs.
    The text prompt is composed from text_dict, meta1 and meta2. Target key_value_pairs is unchanged.

    The interface of the transform function is:
    - Input: Tuple[Tuple[Dict, List[Tuple[PIL.Image.Image, Dict]]], Dict]
    - Output: Tuple[str, Tuple[List[torch.Tensor]], Dict]
    """

    VERSION = '0.1.1'

    @dataclasses.dataclass
    class Inputs:
        image_transform: typing.Callable[[PIL.Image.Image], torch.Tensor]
        text_prompt_jinja_template: str = None

    @dataclasses.dataclass
    class Outputs:
        transform: typing.Callable

    def execute(self, inputs):
        transform = KeyValuePairDatasetTransform(inputs.image_transform, inputs.text_prompt_jinja_template)
        return self.Outputs(transform=transform)

    def dry_run(self, inputs):
        return self.execute(inputs)


class KeyValuePairDatasetTransform:
    """Transform class for key-value-pair dataset training/inference.
    The transform accepts inputs, targets and returns transformed (text_prompt, transformed_imgs), targets, where inputs is tuple of text dict and list of (image, optional metadata dict) tuples

    It (i) applies image transform to images, (ii) construct text prompt from a jinja template given inputs
    The metadata and text dict are converted to JSON strings before passed to template.
    If no template file path is provided, the default template is used.

    Example (using default template):
        1. Multi-image question answering, each sample can have different question:
           inputs: (({"question": "what's different between the images?"}, [(im1, {"catalog": True}), (im2, None)]),
                     {"answer": {"value": "the first is coke catalog image, while the second a captured coke photo."}});
           text_prompt: "<|image|>,{\"catalog\": true}\n<|image|>\n{\"question\": \"what's different between the images?\"}"
        2. Image comparison, the comparison task is defined in key value pair schema, so text_dict is not needed:
           inputs: ((None, [(im1, {"catalog": True}), (im2, None)]), {"comparison": {"value": "the first is coke catalog image, while the second a captured coke photo."}}});
           text_prompt: "<|image|>,{\"catalog\": true}\n<|image|>\n"
        3. Single image people counting, the counting task is defined in key value pair schema:
           inputs: ((None, [(im1, {"place": "Time Square"})]), {"people": {"value": 3}});
           text_prompt: "<|image|>,{\"place\": \"Time Square\"}"

    Args:
        img_transform (callable): Image transform function
        text_transform_jinja_template (str): jinja template str for text transformation. The template should have two variables: imgs_with_meta and text. imgs_with_meta is a list of (image, meta)
            tuples where meta is None or a dictionary, and text is None or a dictionary. In the returned prompt, each image is represented as "<|image|>", meta and text are dumped to JSON strings.
            Refer to text_prompt_template_str for the default template.
    """

    text_prompt_template_str = """{% for _, meta in imgs_with_meta %}<|image|>{% if meta is not none %}, {{meta}}{% endif %}
{% endfor %}{% if text is not none %}{{text}}{% endif %}"""

    def __init__(self, img_transform, text_prompt_jinja_template: str = None):
        self._img_transform = img_transform
        if text_prompt_jinja_template is not None:
            self.text_prompt_template_str = text_prompt_jinja_template
        self._template = Template(self.text_prompt_template_str)

    def __call__(self, inputs, targets):
        text_dict: dict = inputs[0]
        imgs_with_meta: list[tuple] = inputs[1]

        text = json.dumps(text_dict)
        imgs_with_meta = [(img, json.dumps(meta) if meta is not None else None) for img, meta in imgs_with_meta]
        tensors = [self._img_transform(img) for img, _ in imgs_with_meta]
        text_prompt = self._template.render(imgs_with_meta=imgs_with_meta, text=text)
        logger.debug(f"User prompt:\n{text_prompt}")
        return (text_prompt, tensors), targets

    def __getstate__(self):
        return {'img_transform': self._img_transform, 'text_prompt_template_str': self.text_prompt_template_str}

    def __setstate__(self, state):
        self._img_transform = state['img_transform']
        self.text_prompt_template_str = state['text_prompt_template_str']
        self._template = Template(self.text_prompt_template_str)
