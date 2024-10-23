import unittest
import PIL.Image
import torch
from irisml.tasks.make_classification_dataset_with_context import Task


class FakeDataset(torch.utils.data.Dataset):
    def __init__(self, num_images, targets=None):
        super().__init__()
        if targets is None:
            targets = list(range(num_images))
        self._data = [(PIL.Image.new('RGB', (i + 5, i + 5)), targets[i]) for i in range(num_images)]

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]


class TestMakeClassificationDatasetWithContext(unittest.TestCase):
    def setup(self) -> None:
        self.prompt = '''context:
{context}
test image: <|image|>.'''
        self.context_template = 'category: "{category}", reference image: {image}'

    def test_simple(self):
        self.setup()
        dataset = FakeDataset(5)
        context_dataset = FakeDataset(5)
        context_ids = torch.tensor([[3, 4], [4, 0], [0, 1], [1, 2], [2, 3]])
        class_names = ['a', 'b', 'c', 'd', 'e']

        outputs = Task(Task.Config(class_names, self.prompt, self.context_template)).execute(
            Task.Inputs(dataset=dataset, context_dataset=context_dataset, context_ids=context_ids))

        (images, text), target = outputs.dataset[0]
        self.assertEqual(len(images), 3)
        self.assertIsInstance(images[0], PIL.Image.Image)
        self.assertEqual(images[0], context_dataset[3][0])
        self.assertEqual(images[1], context_dataset[4][0])
        self.assertEqual(target, 0)
        self.assertEqual(images[2], dataset[0][0])
        self.assertEqual(text, '''context:
category: "d", reference image: <|image|>
category: "e", reference image: <|image|>

test image: <|image|>.''')

    def test_default_context_ids(self):
        dataset = FakeDataset(3)
        context_dataset = FakeDataset(3)
        class_names = ['a', 'b', 'c']
        self.setup()

        outputs = Task(Task.Config(class_names, self.prompt, self.context_template)).execute(
            Task.Inputs(dataset=dataset, context_dataset=context_dataset))

        (images, text), target = outputs.dataset[0]

        self.assertEqual(len(images), 4)
        for i in range(3):
            self.assertEqual(images[i], context_dataset[i][0])
        self.assertEqual(images[-1], dataset[0][0])
        self.assertEqual(target, 0)
        self.assertEqual(text, '''context:
category: "a", reference image: <|image|>
category: "b", reference image: <|image|>
category: "c", reference image: <|image|>

test image: <|image|>.''')

    def test_variable_context_len(self):
        dataset = FakeDataset(3)
        context_dataset = FakeDataset(3)
        class_names = ['a', 'b', 'c']
        self.setup()
        context_ids = [[0], [], [1, 2]]

        outputs = Task(Task.Config(class_names, self.prompt, self.context_template)).execute(
            Task.Inputs(dataset=dataset, context_dataset=context_dataset, context_ids=context_ids))
        # first sample
        (images, text), target = outputs.dataset[0]

        self.assertEqual(len(images), 2)
        self.assertEqual(images[0], context_dataset[0][0])
        self.assertEqual(images[1], dataset[0][0])
        self.assertEqual(target, 0)
        self.assertEqual(text, '''context:
category: "a", reference image: <|image|>

test image: <|image|>.''')
        # second sample, no context.
        (images, text), target = outputs.dataset[1]

        self.assertEqual(len(images), 1)
        self.assertEqual(images[0], dataset[1][0])
        self.assertEqual(target, 1)
        self.assertEqual(text, '''context:

test image: <|image|>.''')

    def test_dataset_and_context_have_different_classes(self):
        dataset = FakeDataset(2, targets=[0, 1])
        context_dataset = FakeDataset(2, targets=[1, 2])
        class_names = ['a', 'b', 'c']
        self.setup()
        context_ids = [[1], [0]]

        outputs = Task(Task.Config(class_names, self.prompt, self.context_template)).execute(
            Task.Inputs(dataset=dataset, context_dataset=context_dataset, context_ids=context_ids))
        # first sample
        (images, text), target = outputs.dataset[0]

        self.assertEqual(len(images), 2)
        self.assertEqual(images[0], context_dataset[1][0])
        self.assertEqual(images[1], dataset[0][0])
        self.assertEqual(target, 0)
        self.assertEqual(text, '''context:
category: "c", reference image: <|image|>

test image: <|image|>.''')
