import dataclasses
import logging
import typing

import torch
import irisml.core

logger = logging.getLogger(__name__)

IMAGE_PLACEHOLDER = '<|image|>'
CONTEXT_TEMPLATE = 'category: "{category}", reference image: {image}\n'


class Task(irisml.core.TaskBase):
    """Make a in-context classification dataset with prompts.

    This task takes an IC dataset and context_ids referring to the context dataset, returns an in-context IC dataset with customized prompts.
    Each item in context_ids is the sample indices of context dataset, corresponding to the sample in IC dataset. e.g. if context_ids[0] = [2,3],
      then the context of dataset[0] context_dataset[2], context_dataset[3].
    In the final prompt, images are noted as "<|image|>".

    e.g. dataset is [(img1, 0), (img2, 1)], class names ['0', '1'], context_dataset is ((img3, 1), (img4, 0)), context_ids is [[1], [0]]. Propmt is "context:\n{context}\ntest image: <|image|>."
    Then the prompt the first sample is:'''
context:
category: 1, reference image: <|image|>

test image: <|image|>.''',
      where the two <|image|> correspond to img3 and img1. The first sample is ([img3, img1], prompt), 0

    Inputs:
        dataset: IC dataset
        context_dataset: context dataset
        context_ids: context dataset ids for each image of dataset, list[list[int]] where each inner list is the candidate class indices of corresponding sample.
            default: all context samples, [range(len(context_dataset))] * len(dataset)

    Config:
        class_names: class names of context dataset
        prompt: Prompt for each sample of in-context dataset, the context placeholder is "{context}"
        context_template: Prompt template for each context sample, default is CONTEXT_TEMPLATE

    Outputs:
        dataset: in-context IC dataset, each item is (images, final prompt), target

    """
    VERSION = '0.1.0'

    @dataclasses.dataclass
    class Inputs:
        dataset: torch.utils.data.Dataset
        context_dataset: torch.utils.data.Dataset
        context_ids: list[list[int]] = None

    @dataclasses.dataclass
    class Config:
        class_names: typing.List[str]
        prompt: str = "{context}"
        context_template: str = CONTEXT_TEMPLATE

    @dataclasses.dataclass
    class Outputs:
        dataset: torch.utils.data.Dataset

    def execute(self, inputs):
        if self.config.prompt.count(IMAGE_PLACEHOLDER) != 1:
            raise ValueError(f'Prompt should contain exactly one image placeholder "{IMAGE_PLACEHOLDER}", got "{self.config.prompt}"')

        if inputs.context_ids is None:
            context_ids = [range(0, len(inputs.context_dataset))] * len(inputs.dataset)
            logger.info('Using all context samples for each dataset sample.')
        else:
            context_ids = inputs.context_ids
            logger.info('Using provided context samples for each dataset sample')
            logger.debug(f'context_ids: {context_ids}')

        if len(inputs.dataset) != len(context_ids):
            raise ValueError(f"Dataset and context_ids inputs have different lengths: {len(inputs.dataset)} vs {len(context_ids)}")

        return self.Outputs(dataset=DatasetWithContext(inputs.dataset, inputs.context_dataset, self.config.class_names, context_ids,
                            self.config.prompt, self.config.context_template))

    def dry_run(self, inputs):
        return self.execute(inputs)


class DatasetWithContext(torch.utils.data.Dataset):
    """Make in-context IC dataset with customized prompts, from IC dataset and context dataset. Each sample is (images, final prompt), target,
    where images consists of the original image in IC dataset and the context images from context dataset, image positions are determined
    by the prompt.
    """
    def __init__(self, dataset, context_dataset, class_names, context_ids,
                 prompt, context_template):
        super().__init__()

        self._dataset = dataset
        self._context_ids = context_ids
        self._class_names = class_names
        self._prompt = prompt
        self._context_template = context_template
        # If test image is after context or not.
        self._test_image_last = prompt.find(IMAGE_PLACEHOLDER) > prompt.find("{context}")

        self._context_dataset = context_dataset

    def __len__(self):
        return len(self._dataset)

    def _construct(self, index):
        text = ''
        context_images = []
        for idx in self._context_ids[index]:
            context_img, context_tgt = self._context_dataset[idx]
            t = self._context_template.format(category=self._class_names[context_tgt], image=IMAGE_PLACEHOLDER)
            if not t.endswith('\n'):
                t += '\n'
            text += t
            context_images.append(context_img)

        if self._prompt:
            text = self._prompt.format(context=text)
        logger.debug(f'Index {index}, constructed prompt: {text}')
        return text, context_images

    def __getitem__(self, index):
        input, target = self._dataset[index]
        text, context_images = self._construct(index)
        # add the test image
        images = context_images + [input] if self._test_image_last else [input] + context_images
        if len(images) != text.count(IMAGE_PLACEHOLDER):
            raise ValueError(f'Number of images ({len(images)}) does not match number of image placeholders ({text.count(IMAGE_PLACEHOLDER)})')
        return (images, text), target
