import unittest
import PIL.Image
import torch
from irisml.tasks.concatenate_datasets import Task


from utils import FakeDataset, FakeDatasetWithGetTargets


class TestConcatenateDatasets(unittest.TestCase):
    def test_same_classsspace_classification(self):
        dataset0 = FakeDataset([(None, torch.tensor(1)), (None, torch.tensor(2)), (None, torch.tensor(3))])
        dataset1 = FakeDataset([(None, torch.tensor(1)), (None, torch.tensor(2)), (None, torch.tensor(3))])
        outputs = Task(Task.Config(use_same_classspace=True)).execute(Task.Inputs(dataset0, dataset1))
        self.assertEqual(len(outputs.dataset), 6)
        self.assertEqual(outputs.dataset[0], (None, torch.tensor(1)))
        self.assertEqual(outputs.dataset[3], (None, torch.tensor(1)))
        self.assertEqual(outputs.dataset[5], (None, torch.tensor(3)))

    def test_class_names_pass_through(self):
        dataset0 = FakeDataset([(None, torch.tensor(1)), (None, torch.tensor(2)), (None, torch.tensor(3))])
        dataset1 = FakeDataset([(None, torch.tensor(1)), (None, torch.tensor(2)), (None, torch.tensor(3))])
        class_names0 = ['label0', 'label1', 'label2', 'label3', 'label4']
        outputs = Task(Task.Config(use_same_classspace=True)).execute(Task.Inputs(dataset0, dataset1, class_names0))
        self.assertEqual(outputs.class_names, class_names0)
        self.assertEqual(outputs.num_classes, len(class_names0))

    def test_same_classspace_with_different_class_names(self):
        dataset0 = FakeDataset([(None, torch.tensor(1)), (None, torch.tensor(2)), (None, torch.tensor(3))])
        dataset1 = FakeDataset([(None, torch.tensor(1)), (None, torch.tensor(2)), (None, torch.tensor(3))])
        class_names0 = ['label0', 'label1', 'label2', 'label3', 'label4']
        class_names1 = ['label5', 'label1', 'label2', 'label3', 'label4']
        with self.assertRaises(ValueError):
            Task(Task.Config(use_same_classspace=True)).execute(Task.Inputs(dataset0, dataset1, class_names0, class_names1))

    def test_different_classsspace_classification_with_same_name(self):
        dataset0 = FakeDataset([(None, torch.tensor(1)), (None, torch.tensor(2)), (None, torch.tensor(3))])
        dataset1 = FakeDataset([(None, torch.tensor(1)), (None, torch.tensor(2)), (None, torch.tensor(3))])
        class_names0 = ['label0', 'label1', 'label2', 'label3', 'label4']
        class_names1 = ['label0', 'label1', 'label2', 'label3', 'label4']
        outputs = Task(Task.Config(use_same_classspace=False)).execute(Task.Inputs(dataset0, dataset1, class_names0, class_names1))
        self.assertEqual(len(outputs.dataset), 6)
        self.assertEqual(outputs.dataset[0], (None, torch.tensor(1)))
        self.assertEqual(outputs.dataset[3], (None, torch.tensor(1)))
        self.assertEqual(outputs.dataset[5], (None, torch.tensor(3)))

    def test_different_classsspace_classification(self):
        dataset0 = FakeDataset([(None, torch.tensor(1)), (None, torch.tensor(2)), (None, torch.tensor(3))])
        dataset1 = FakeDataset([(None, torch.tensor(1)), (None, torch.tensor(2)), (None, torch.tensor(3))])
        class_names0 = ['label0', 'label1', 'label2', 'label3', 'label4']
        class_names1 = ['label00', 'label01', 'label02', 'label03', 'label04']
        outputs = Task(Task.Config(use_same_classspace=False)).execute(Task.Inputs(dataset0, dataset1, class_names0, class_names1))
        self.assertEqual(len(outputs.dataset), 6)
        self.assertEqual(outputs.dataset[0], (None, torch.tensor(1)))
        self.assertEqual(outputs.dataset[3], (None, torch.tensor(6)))
        self.assertEqual(outputs.dataset[5], (None, torch.tensor(8)))

    def test_different_classsspace_classification_with_duplicated_names(self):
        dataset0 = FakeDataset([(None, torch.tensor(1)), (None, torch.tensor(2)), (None, torch.tensor(3))])
        dataset1 = FakeDataset([(None, torch.tensor(1)), (None, torch.tensor(2)), (None, torch.tensor(3))])
        class_names0 = ['label0', 'label1', 'label2', 'label3', 'label4']
        class_names1 = ['label0', 'label1', 'label02', 'label03', 'label04']
        outputs = Task(Task.Config(use_same_classspace=False)).execute(Task.Inputs(dataset0, dataset1, class_names0, class_names1))
        self.assertEqual(len(outputs.dataset), 6)
        self.assertEqual(outputs.dataset[0], (None, torch.tensor(1)))
        self.assertEqual(outputs.dataset[3], (None, torch.tensor(1)))
        self.assertEqual(outputs.dataset[5], (None, torch.tensor(6)))

    def test_different_classsspace_object_detection_with_duplicated_names(self):
        dataset0 = FakeDataset([(None, torch.tensor([[1, 0, 0, 1, 1]])), (None, torch.tensor([[2, 0, 0, 1, 1]])), (None, torch.tensor([[3, 0, 0, 1, 1]]))])
        dataset1 = FakeDataset([(None, torch.tensor([[1, 0, 0, 1, 1]])), (None, torch.tensor([[2, 0, 0, 1, 1], [4, 0, 0, 1, 1]])), (None, torch.tensor([[3, 0, 0, 1, 1]]))])
        class_names0 = ['label0', 'label1', 'label2', 'label3', 'label4']
        class_names1 = ['label0', 'label1', 'label02', 'label03', 'label04']
        outputs = Task(Task.Config(use_same_classspace=False, task_type='object_detection')).execute(Task.Inputs(dataset0, dataset1, class_names0, class_names1))
        self.assertEqual(len(outputs.dataset), 6)
        self.assertTrue(torch.equal(outputs.dataset[0][1], torch.tensor([[1, 0, 0, 1, 1]])))
        self.assertTrue(torch.equal(outputs.dataset[3][1], torch.tensor([[1, 0, 0, 1, 1]])))
        self.assertTrue(torch.equal(outputs.dataset[5][1], torch.tensor([[6, 0, 0, 1, 1]])))

    def test_no_second_dataset(self):
        dataset0 = FakeDataset([(None, torch.tensor(1)), (None, torch.tensor(2)), (None, torch.tensor(3))])
        outputs = Task(Task.Config()).execute(Task.Inputs(dataset0, None))
        self.assertEqual(outputs.dataset, dataset0)

    def test_get_targets(self):
        dataset0 = FakeDatasetWithGetTargets([(None, torch.tensor(1)), (None, torch.tensor(2)), (None, torch.tensor(3))])
        dataset1 = FakeDataset([(None, torch.tensor(1)), (None, torch.tensor(2)), (None, torch.tensor(3))])
        outputs = Task(Task.Config()).execute(Task.Inputs(dataset0, dataset1))
        self.assertEqual(len(outputs.dataset), 6)
        self.assertEqual(outputs.dataset.get_targets(0), torch.tensor(1))
        self.assertEqual(outputs.dataset.get_targets(1), torch.tensor(2))
        self.assertEqual(outputs.dataset.get_targets(2), torch.tensor(3))
        self.assertEqual(dataset0._counter, 3)
        self.assertEqual(outputs.dataset.get_targets(3), torch.tensor(1))
        self.assertEqual(outputs.dataset.get_targets(4), torch.tensor(2))
        self.assertEqual(outputs.dataset.get_targets(5), torch.tensor(3))
        self.assertEqual(dataset0._counter, 3)

    def test_phrase_grounding_dataset(self):
        dataset0 = FakeDataset([(('abc', PIL.Image.new('RGB', (10, 10))), [(0, 2), torch.tensor([[0.1, 0.1, 0.2, 0.2]])]),
                                (('def', PIL.Image.new('RGB', (10, 10))), [(0, 3), torch.tensor([[0.2, 0.2, 0.3, 0.3]])])])
        dataset1 = FakeDataset([(('abc2', PIL.Image.new('RGB', (10, 10))), [(0, 2), torch.tensor([[0.1, 0.1, 0.2, 0.2]])]),
                                (('def2', PIL.Image.new('RGB', (10, 10))), [(0, 3), torch.tensor([[0.2, 0.2, 0.3, 0.3]])])])
        outputs = Task(Task.Config(task_type='phrase_grounding')).execute(Task.Inputs(dataset0, dataset1))
        self.assertEqual(len(outputs.dataset), 4)
        self.assertEqual(outputs.dataset[0][0], ('abc', PIL.Image.new('RGB', (10, 10))))
        self.assertEqual(outputs.dataset[1][0], ('def', PIL.Image.new('RGB', (10, 10))))
        self.assertEqual(outputs.dataset[2][0], ('abc2', PIL.Image.new('RGB', (10, 10))))
        self.assertEqual(outputs.dataset[3][0], ('def2', PIL.Image.new('RGB', (10, 10))))
        self.assertTrue(torch.equal(outputs.dataset[0][1][1], torch.tensor([[0.1, 0.1, 0.2, 0.2]])))
        self.assertTrue(torch.equal(outputs.dataset[1][1][1], torch.tensor([[0.2, 0.2, 0.3, 0.3]])))
        self.assertTrue(torch.equal(outputs.dataset[2][1][1], torch.tensor([[0.1, 0.1, 0.2, 0.2]])))
        self.assertTrue(torch.equal(outputs.dataset[3][1][1], torch.tensor([[0.2, 0.2, 0.3, 0.3]])))
