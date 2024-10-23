import dataclasses
import logging
import torch.utils.data
import irisml.core

logger = logging.getLogger(__name__)


class Task(irisml.core.TaskBase):
    """Flatten a captioning dataset with multiple targets per image into a dataset with a single target per image.

    """
    VERSION = '0.1.0'

    @dataclasses.dataclass
    class Inputs:
        dataset: torch.utils.data.Dataset

    @dataclasses.dataclass
    class Outputs:
        dataset: torch.utils.data.Dataset

    def execute(self, inputs):
        dataset = FlatDataset(inputs.dataset)
        return self.Outputs(dataset=dataset)

    def dry_run(self, inputs):
        return self.execute(inputs)


class FlatDataset(torch.utils.data.Dataset):
    def __init__(self, dataset):
        self._dataset = dataset

        if hasattr(dataset, 'get_targets'):
            num_targets = [len(dataset.get_targets(i)) for i in range(len(dataset))]
        else:
            num_targets = [len(dataset[i][1]) for i in range(len(dataset))]

        index_mapping = []
        for i, num_target in enumerate(num_targets):
            index_mapping.extend([(i, j) for j in range(num_target)])

        self._index_mapping = index_mapping

        logger.info(f"Flattened dataset from {len(dataset)} to {len(index_mapping)}")

    def __len__(self):
        return len(self._index_mapping)

    def __getitem__(self, index):
        dataset_index, target_index = self._index_mapping[index]
        d = self._dataset[dataset_index]
        assert isinstance(d[1], list)
        return d[0], [d[1][target_index]]

    def get_targets(self, index):
        dataset_index, target_index = self._index_mapping[index]
        if hasattr(self._dataset, 'get_targets'):
            targets = self._dataset.get_targets(dataset_index)
        else:
            targets = self._dataset[dataset_index][1]
        return [targets[target_index]]
