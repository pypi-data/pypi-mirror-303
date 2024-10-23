import dataclasses
import logging
import typing
import torch
import torchvision
import irisml.core

logger = logging.getLogger(__name__)


class Task(irisml.core.TaskBase):
    """Calculate precision/recall for phrase grounding.

    Config:
        top_k (Optional[int]): Number of top predictions to consider. If None, all predictions are considered. Default: 1
        iou_threshold (float): IOU threshold for positive prediction. Default: 0.5
    """
    VERSION = '0.1.0'

    @dataclasses.dataclass
    class Inputs:
        predictions: typing.List[typing.List[typing.Tuple[typing.Tuple[int, int], torch.Tensor]]]
        targets: typing.List[typing.List[typing.Tuple[typing.Tuple[int, int], torch.Tensor]]]

    @dataclasses.dataclass
    class Config:
        top_k: typing.Optional[int] = 1
        iou_threshold: float = 0.5

    @dataclasses.dataclass
    class Outputs:
        precision: float = 0
        recall: float = 0

    def execute(self, inputs):
        if len(inputs.predictions) != len(inputs.targets):
            raise ValueError(f"Number of predictions ({len(inputs.predictions)}) does not match number of targets ({len(inputs.targets)})")

        num_correct = 0
        num_total_targets = 0
        num_total_predictions = 0
        for prediction, target in zip(inputs.predictions, inputs.targets):
            target_span_boxes = {tuple(span): boxes for span, boxes in target}
            assert len(target_span_boxes) == len(target), "Duplicate spans in target"
            assert len(set(tuple(pred[0]) for pred in prediction)) == len(prediction), "Duplicate spans in prediction"
            num_total_targets += len(target_span_boxes)

            for pred in prediction:
                target_boxes = target_span_boxes.get(tuple(pred[0]))
                if target_boxes is not None:
                    num_total_predictions += 1
                    if self._is_positive(pred[1], target_boxes):
                        num_correct += 1

        precision = num_correct / num_total_predictions if num_total_predictions > 0 else 0
        recall = num_correct / num_total_targets if num_total_targets > 0 else 0
        logger.info(f"Precision@{self.config.top_k} IOU({self.config.iou_threshold}): {precision}, correct: {num_correct}, total: {num_total_predictions}")
        logger.info(f"Recall@{self.config.top_k} IOU({self.config.iou_threshold}): {recall}, correct: {num_correct}, total: {num_total_targets}")

        return self.Outputs(precision=precision, recall=recall)

    def _is_positive(self, predicted_boxes, target_boxes):
        if len(predicted_boxes) == 0 or len(target_boxes) == 0:
            return False
        ious = torchvision.ops.box_iou(predicted_boxes, target_boxes)
        return ious[:self.config.top_k].max() >= self.config.iou_threshold
