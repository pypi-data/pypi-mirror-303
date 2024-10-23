import dataclasses
from typing import Callable, Optional, Tuple
import PIL.Image
import torch
import irisml.core


class Task(irisml.core.TaskBase):
    """Creates a transform function for VQA task.

    The input to the transform function is ((question, image), targets), where question is a string,
    image is a PIL image, and targets is a string.

    If tokenizer is provided, the output of the transform function is ((question, image_tensor), targets),
    where question is a tuple of tensors, image_tensor is a tensor, and targets is a tuple of tensors.

    If tokenizer is not provided, the output of the transform function is ((question, image_tensor), targets),
    where question is a string, image_tensor is a tensor, and targets is a string.

    Config:
        skip_traget_tokenization (bool): If True, the target is not tokenized. Default: False
        pad_token_id (int): The id of the padding token. Used in the collate_function. Default: 1
    """
    VERSION = '1.2.0'

    @dataclasses.dataclass
    class Inputs:
        image_transform: Callable[[PIL.Image.Image], torch.Tensor]
        text_transform: Optional[Callable[[str], str]] = None
        target_text_transform: Optional[Callable[[str], str]] = None
        tokenizer: Optional[Callable[[str], Tuple[torch.Tensor, torch.Tensor]]] = None  # The output is (input_ids, attention_mask)

    @dataclasses.dataclass
    class Config:
        skip_target_tokenization: bool = False
        pad_token_id: int = 1

    @dataclasses.dataclass
    class Outputs:
        transform: Callable[[Tuple[str, PIL.Image.Image], str], Tuple[Tuple[str, torch.Tensor], str]]
        collate_function: Callable  # [(((input_ids, attention_mask), image_tensor), (input_ids, attention_mask))] => (((input_ids, attention_mask), image_tensor), (input_ids, attention_mask))

    def execute(self, inputs):
        transform = VqaImageTransform(inputs.image_transform, inputs.text_transform, inputs.target_text_transform, inputs.tokenizer, self.config.skip_target_tokenization)
        collate_function = Collate(self.config.pad_token_id)
        return self.Outputs(transform=transform, collate_function=collate_function)

    def dry_run(self, inputs):
        return self.execute(inputs)


class Collate:
    def __init__(self, pad_token_id):
        self._pad_token_id = pad_token_id

    def __call__(self, batch):
        questions = [b[0][0] for b in batch]
        images = [b[0][1] for b in batch]
        targets = [b[1] for b in batch]

        # input_ids, attention_mask. Use 0 for attention_mask padding.
        questions = (self._padded_stack([q[0] for q in questions], self._pad_token_id), self._padded_stack([q[1] for q in questions]))
        images = torch.stack(images, 0)
        if not isinstance(targets[0], str):
            targets = (self._padded_stack([t[0] for t in targets], self._pad_token_id), self._padded_stack([t[1] for t in targets]))

        return (questions, images), targets

    def _padded_stack(self, tensors, pad_token_id=0):
        """Stacks tensors along the first dimension and pads them to the same length."""
        max_length = max([t.shape[0] for t in tensors])
        return torch.stack([torch.nn.functional.pad(t, (0, max_length - t.shape[0]), value=pad_token_id) for t in tensors], 0)


class VqaImageTransform:
    def __init__(self, image_transform, text_transform, target_text_transform, tokenizer, skip_target_tokenization):
        self._image_transform = image_transform
        self._text_transform = text_transform
        self._target_text_transform = target_text_transform
        self._tokenizer = tokenizer
        self._skip_target_tokenization = skip_target_tokenization

    def __call__(self, inputs, targets):
        question, image = inputs
        assert isinstance(question, str)
        assert isinstance(image, PIL.Image.Image)
        assert isinstance(targets, str)

        image_tensor = self._image_transform(image)

        if self._text_transform:
            question = self._text_transform(question)

        if self._target_text_transform:
            targets = self._target_text_transform(targets)

        if self._tokenizer:
            question = self._tokenizer(question)
            if not self._skip_target_tokenization:
                targets = self._tokenizer(targets)

        return (question, image_tensor), targets
