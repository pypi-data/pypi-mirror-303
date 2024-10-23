import base64
import dataclasses
import io
import json
import logging
import pathlib
import pickle
import tempfile
import typing
import PIL.Image
import torch.utils.data
import irisml.core

logger = logging.getLogger(__name__)


class Task(irisml.core.TaskBase):
    """Load a VQA dataset from a jsonl file.

    JSONL dataset format: {image: <base64 encoded image>, question: str, answer: str}

    Loaded dataset format is a tuple of ((question: str, image: PIL.Image.Image), answer: str)

    The dataset is cached in a temporary directory.

    Config:
        filepath (Path): Path to the jsonl file.
        cache_dirpath (Optional[Path]): Path to the directory where the dataset will be cached. If not specified, a temporary directory will be created.
            Caller is responsible for deleting the directory when it is no longer needed.
    """
    VERSION = '0.2.0'
    CACHE_ENABLED = False

    @dataclasses.dataclass
    class Config:
        filepath: pathlib.Path
        cache_dirpath: typing.Optional[pathlib.Path] = None

    @dataclasses.dataclass
    class Outputs:
        dataset: torch.utils.data.Dataset

    def execute(self, inputs):
        dataset = VQADataset(self.config.filepath, self.config.cache_dirpath)
        return self.Outputs(dataset=dataset)

    def dry_run(self, inputs):
        return self.execute(inputs)


class VQADataset(torch.utils.data.Dataset):
    def __init__(self, filepath, cache_dirpath):
        super().__init__()
        if cache_dirpath:
            self._temp_dir = None
            self._temp_dir_path = cache_dirpath
            self._temp_dir_path.mkdir(parents=True, exist_ok=True)
        else:
            self._temp_dir = tempfile.TemporaryDirectory()
            self._temp_dir_path = pathlib.Path(self._temp_dir.name)

        logger.info(f"Unpacking {filepath} to {self._temp_dir_path}")
        index = 0
        with open(filepath) as f:
            for line in f:
                if not line:
                    continue
                json_data = json.loads(line)
                data = (base64.b64decode(json_data['image']), json_data['question'], json_data['answer'])
                (self._temp_dir_path / f'{index}.pkl').write_bytes(pickle.dumps(data))
                index += 1
        logger.info(f"Loaded {index} images from {filepath}")
        self._num_images = index

    def __len__(self):
        return self._num_images

    def __getitem__(self, index):
        if index >= self._num_images:
            raise IndexError(f"Index {index} out of range")

        if not self._temp_dir_path:
            raise RuntimeError("Dataset is closed")

        image_bytes, question, answer = pickle.loads((self._temp_dir_path / f'{index}.pkl').read_bytes())
        image = PIL.Image.open(io.BytesIO(image_bytes))
        return (question, image), answer

    def get_targets(self, index):
        if index >= self._num_images:
            raise IndexError(f"Index {index} out of range")

        if not self._temp_dir_path:
            raise RuntimeError("Dataset is closed")

        _, _, answer = pickle.loads((self._temp_dir_path / f'{index}.pkl').read_bytes())
        return answer
