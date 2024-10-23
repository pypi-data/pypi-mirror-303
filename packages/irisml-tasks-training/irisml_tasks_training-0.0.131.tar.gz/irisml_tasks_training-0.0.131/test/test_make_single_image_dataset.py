import io
import json
import pathlib
import tempfile
import unittest
import PIL.Image
import torch
from irisml.tasks.make_single_image_dataset import Task


class TestMakeSingleImageDataset(unittest.TestCase):
    def test_simple(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            image_path = pathlib.Path(temp_dir) / 'image.jpg'
            image = PIL.Image.new('RGB', (64, 64))
            image.save(image_path)

            outputs = Task(Task.Config(path=image_path, task_type='classification_multiclass')).execute(Task.Inputs())
            dataset = outputs.dataset

            self.assertEqual(len(dataset), 1)
            image, target = dataset[0]
            self.assertIsInstance(image, PIL.Image.Image)
            self.assertEqual(image.size, (64, 64))
            self.assertIsInstance(target, torch.Tensor)
            self.assertEqual(target.item(), 0)

            outputs = Task(Task.Config(path=image_path, task_type='object_detection')).execute(Task.Inputs())
            dataset = outputs.dataset

            self.assertEqual(len(dataset), 1)
            image, target = dataset[0]
            self.assertIsInstance(image, PIL.Image.Image)
            self.assertEqual(image.size, (64, 64))
            self.assertIsInstance(target, torch.Tensor)
            self.assertEqual(target.size(), (0, 5))

            outputs = Task(Task.Config(path=image_path, task_type='key_value_pair')).execute(Task.Inputs())
            dataset = outputs.dataset

            self.assertEqual(len(dataset), 1)
            (text, [(image, meta)]), fields = dataset[0]
            self.assertIsInstance(image, PIL.Image.Image)
            self.assertEqual(image.size, (64, 64))
            self.assertIsNone(text)
            self.assertIsNone(meta)
            self.assertIsNone(fields)

    def test_no_image(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            image_path = pathlib.Path(temp_dir) / 'no_image.jpg'
            outputs = Task(Task.Config(path=image_path, task_type='classification_multiclass')).execute(Task.Inputs())
            dataset = outputs.dataset

            self.assertEqual(len(dataset), 1)
            image, target = dataset[0]
            self.assertIsInstance(image, PIL.Image.Image)
            self.assertEqual(image.size, (224, 224))
            self.assertIsInstance(target, torch.Tensor)
            self.assertEqual(target.item(), 0)

    def test_invalid_image_header(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            image_path = pathlib.Path(temp_dir) / 'image.jpg'
            image_path.write_bytes(b"Invalid header")

            task = Task(Task.Config(path=image_path, task_type='classification_multiclass'))
            outputs = task.execute(Task.Inputs())
            dataset = outputs.dataset

            with self.assertRaises(PIL.UnidentifiedImageError) as cm:
                _ = dataset[0]
            self.assertEqual(f"cannot identify image file {repr(str(image_path))}", cm.exception.args[0])

    def test_invalid_image_body(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            image_path = pathlib.Path(temp_dir) / 'image.jpg'
            image = PIL.Image.new('RGB', (64, 64))
            with io.BytesIO() as bytes_io:
                image.save(bytes_io, format="JPEG")
                image_path.write_bytes(bytes_io.getvalue()[:-1])

            task = Task(Task.Config(path=image_path, task_type='classification_multiclass'))
            outputs = task.execute(Task.Inputs())
            dataset = outputs.dataset

            with self.assertRaises(PIL.UnidentifiedImageError) as cm:
                _ = dataset[0]
            self.assertEqual("image file is truncated (3 bytes not processed)", cm.exception.args[0])

    def test_image_metadata_dict(self):
        with tempfile.TemporaryDirectory(suffix='.jpg') as temp_dir:
            image_path = pathlib.Path(temp_dir) / 'image.jpg'
            image = PIL.Image.new('RGB', (64, 64))
            image.save(image_path)
            image_metadata = json.dumps({"ocr": "OCR text from the image"})

            outputs = Task(Task.Config(path=image_path, task_type='key_value_pair')).execute(Task.Inputs(image_metadata=image_metadata))
            dataset = outputs.dataset

            self.assertEqual(len(dataset), 1)
            (text, [(image, meta)]), fields = dataset[0]
            self.assertIsInstance(image, PIL.Image.Image)
            self.assertEqual(image.size, (64, 64))
            self.assertIsNone(text)
            self.assertEqual(meta, {"ocr": "OCR text from the image"})
            self.assertIsNone(fields)

    def test_image_metadata_string(self):
        with tempfile.TemporaryDirectory(suffix='.jpg') as temp_dir:
            image_path = pathlib.Path(temp_dir) / 'image.jpg'
            image = PIL.Image.new('RGB', (64, 64))
            image.save(image_path)
            image_metadata = "OCR text from the image"
            default_metadata_key = "ocr"

            outputs = Task(Task.Config(path=image_path, task_type='key_value_pair', default_metadata_key=default_metadata_key)).execute(Task.Inputs(image_metadata=image_metadata))
            dataset = outputs.dataset

            self.assertEqual(len(dataset), 1)
            (text, [(image, meta)]), fields = dataset[0]
            self.assertIsInstance(image, PIL.Image.Image)
            self.assertEqual(image.size, (64, 64))
            self.assertIsNone(text)
            self.assertEqual(meta, {"ocr": "OCR text from the image"})
            self.assertIsNone(fields)
