import dataclasses
import logging

import irisml.core
import torch
import torchvision

logger = logging.getLogger(__name__)


class Task(irisml.core.TaskBase):
    """Perform Non-Maximum Suppression on a list of bounding boxes.

    Inputs:
        predictions (list[Tensor]): A list of tensors, where each tensor has shape (N, 6) and represents a list of
            bounding boxes. Each bounding box is represented as a row in the tensor, with the following columns:
            - Column 0: Class ID
            - Column 1: Confidence score
            - Columns 2-5: Bounding box coordinates (x1, y1, x2, y2)

    Config:
        iou_threshold (float): The IoU threshold to use for NMS.
        class_agnostic (bool): If True, perform NMS without considering the class ID.
    """
    VERSION = '0.1.1'

    @dataclasses.dataclass
    class Inputs:
        predictions: list[torch.Tensor]

    @dataclasses.dataclass
    class Config:
        iou_threshold: float = 0.5
        class_agnostic: bool = False

    @dataclasses.dataclass
    class Outputs:
        predictions: list[torch.Tensor]

    def execute(self, inputs):
        post_nms_predictions = []
        for predictions in inputs.predictions:
            if len(predictions) == 0:
                post_nms_predictions.append(torch.empty(0, 6))
                continue

            if self.config.class_agnostic:
                post_nms_predictions.append(self.nms(predictions, self.config.iou_threshold))
                continue

            # Perform NMS per class
            unique_class_ids = torch.unique(predictions[:, 0])
            post_nms_class_predictions = []
            for class_id in unique_class_ids:
                class_predictions = self.filter_bboxes_by_class_id(predictions, class_id)
                post_nms_class_predictions.append(self.nms(class_predictions, self.config.iou_threshold))
            post_nms_predictions.append(torch.cat(post_nms_class_predictions))

        return self.Outputs(post_nms_predictions)

    def dry_run(self, inputs):
        return self.execute(inputs)

    @staticmethod
    def filter_bboxes_by_class_id(input_tensor, class_id):
        mask = input_tensor[:, 0] == class_id
        filtered_tensor = input_tensor[mask]
        return filtered_tensor

    @staticmethod
    def nms(predictions, iou_threshold=0.5):
        keep_idx = torchvision.ops.nms(predictions[:, 2:], predictions[:, 1], iou_threshold)
        return predictions[keep_idx]
