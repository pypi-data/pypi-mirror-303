import copy
import unittest
import PIL.Image
import torch
import torchvision
from irisml.tasks.make_key_value_pair_dataset_transform import Task


class TestMakeKeyValuePairDatasetTransform(unittest.TestCase):
    def test_simple(self):
        image_transform = torchvision.transforms.ToTensor()
        im1 = PIL.Image.new('RGB', (1, 1))
        im2 = PIL.Image.new('RGB', (2, 2))

        # a sample of key_value_pair dataset
        inputs = ({"question": "what's different between the images?"}, [(im1, {"catalog": True}), (im2, None)])
        targets = {"answer": {"value": {"difference": "size."}}}

        # test default template
        transform = Task(Task.Config()).execute(Task.Inputs(image_transform)).transform

        (text_prompt, transformed_imgs), t = transform(inputs, targets)
        self.assertEqual(text_prompt, "<|image|>, {\"catalog\": true}\n<|image|>\n{\"question\": \"what's different between the images?\"}")
        self.assertEqual(transformed_imgs[0].shape, torch.Size([3, 1, 1]))
        self.assertEqual(transformed_imgs[1].shape, torch.Size([3, 2, 2]))
        self.assertEqual(t, targets)

        # test customized template
        jinja_template = """{% for _, meta in imgs_with_meta %}image: <|image|>{% if meta is not none %}, text: {{meta}}{% endif %}
{% endfor %}
{% if text is not none %}{{text}}{% endif %}"""

        transform = Task(Task.Config()).execute(Task.Inputs(image_transform, jinja_template)).transform

        (text_prompt, transformed_imgs), t = transform(inputs, targets)
        self.assertEqual(text_prompt, "image: <|image|>, text: {\"catalog\": true}\nimage: <|image|>\n\n{\"question\": \"what's different between the images?\"}")
        self.assertEqual(transformed_imgs[0].shape, torch.Size([3, 1, 1]))
        self.assertEqual(transformed_imgs[1].shape, torch.Size([3, 2, 2]))
        self.assertEqual(t, targets)

    def test_deepcopy(self):
        image_transform = torchvision.transforms.ToTensor()
        transform = Task(Task.Config()).execute(Task.Inputs(image_transform)).transform

        # Deep copy shouldn't raise an error
        transform2 = copy.deepcopy(transform)

        image = PIL.Image.new('RGB', (8, 8))
        (text_prompt, transformed_imgs), t = transform(({"question": "Q"}, [(image, None)]), {"answer": {"value": "A"}})
        (text_prompt2, transformed_imgs2), t2 = transform2(({"question": "Q"}, [(image, None)]), {"answer": {"value": "A"}})
        self.assertEqual(text_prompt, text_prompt2)
        self.assertEqual(t, t2)
        self.assertTrue(torch.equal(transformed_imgs[0], transformed_imgs2[0]))
