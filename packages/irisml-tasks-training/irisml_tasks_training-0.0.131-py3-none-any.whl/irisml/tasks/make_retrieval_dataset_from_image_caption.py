import dataclasses
import logging
import torch.utils.data
import irisml.core

logger = logging.getLogger(__name__)


class Task(irisml.core.TaskBase):
    """Make a image-text retrieval dataset from a image-caption dataset.

    This task creates two datasets: one for image retrieval and the other for text retrieval.

    The input dataset should have the following structure: (image, [text1, text2, ...]).

    The image retrieval dataset has the following structure: (image, [text_id1, text_id2, ...]).
    The text retrieval dataset has the following structure: (text, image_id).
    """
    VERSION = '0.1.0'

    @dataclasses.dataclass
    class Inputs:
        dataset: torch.utils.data.Dataset

    @dataclasses.dataclass
    class Outputs:
        image_retrieval_dataset: torch.utils.data.Dataset
        text_retrieval_dataset: torch.utils.data.Dataset

    def execute(self, inputs):
        num_texts = [len(d[1]) for d in inputs.dataset]
        if 0 in num_texts:
            raise ValueError('Some data samples do not have any text.')

        logger.info(f"Creating image retrieval dataset. num_images={len(inputs.dataset)}, num_texts={sum(num_texts)}")
        return self.Outputs(ImageRetrievalDataset(inputs.dataset, num_texts), TextRetrievalDataset(inputs.dataset, num_texts))

    def dry_run(self, inputs):
        return self.execute(inputs)


class ImageRetrievalDataset(torch.utils.data.Dataset):
    def __init__(self, dataset, num_texts):
        assert len(dataset) == len(num_texts)
        self._dataset = dataset
        self._targets = []
        c = 0
        for n in num_texts:
            self._targets.append([c + i for i in range(n)])
            c += n

    def __getitem__(self, index):
        return self._dataset[index][0], torch.tensor(self._targets[index])

    def __len__(self):
        return len(self._dataset)


class TextRetrievalDataset(torch.utils.data.Dataset):
    def __init__(self, dataset, num_texts):
        assert len(dataset) == len(num_texts)
        self._dataset = dataset
        self._mappings = [(i, j) for i, n in enumerate(num_texts) for j in range(n)]

    def __getitem__(self, index):
        image_id, text_id = self._mappings[index]
        return self._dataset[image_id][1][text_id], torch.tensor(image_id)

    def __len__(self):
        return len(self._mappings)
