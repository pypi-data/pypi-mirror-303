import dataclasses
import typing
import torch
import irisml.core


class Task(irisml.core.TaskBase):
    """Creates a collate_function for Visual Question Answering (VQA) and Phrase Grounding task.

    Supported formats:
    - (((input_ids, attention_mask), image_tensor), (input_ids, attention_mask))
    - ((question, image_tensor), answer)

    Config:
        pad_token_id (int): The id of the padding token. Default: 1.
    """
    VERSION = '0.2.2'

    @dataclasses.dataclass
    class Config:
        pad_token_id: int = 1

    @dataclasses.dataclass
    class Outputs:
        collate_function: typing.Callable  # [(((input_ids, attention_mask), image_tensor), (input_ids, attention_mask))] => (((input_ids, attention_mask), image_tensor), (input_ids, attention_mask))

    def execute(self, inputs):
        collate_function = Collate(self.config.pad_token_id)
        return self.Outputs(collate_function)

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
        if isinstance(questions[0], (list, tuple)) and isinstance(questions[0][0], torch.Tensor):
            questions = (self._padded_stack([q[0] for q in questions], self._pad_token_id), self._padded_stack([q[1] for q in questions]))
        if isinstance(images[0], torch.Tensor):
            images = torch.stack(images, 0)
        if isinstance(targets[0], torch.Tensor):
            targets = torch.stack(targets, 0)
        elif isinstance(targets[0], (list, tuple)) and isinstance(targets[0][0], torch.Tensor):
            targets = (self._padded_stack([t[0] for t in targets], self._pad_token_id), self._padded_stack([t[1] for t in targets]))

        return (questions, images), targets

    def _padded_stack(self, tensors, pad_token_id=0):
        """Stacks tensors along the first dimension and pads them to the same length."""
        max_length = max([t.shape[0] for t in tensors])
        return torch.stack([torch.nn.functional.pad(t, (0, max_length - t.shape[0]), value=pad_token_id) for t in tensors], 0)
