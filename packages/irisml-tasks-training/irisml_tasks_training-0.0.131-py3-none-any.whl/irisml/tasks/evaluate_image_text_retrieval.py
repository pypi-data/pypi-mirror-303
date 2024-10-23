import dataclasses
import logging
import typing
import torch
import irisml.core

logger = logging.getLogger(__name__)


class Task(irisml.core.TaskBase):
    """Evaluate the image-text retrieval task.

    Currently it supports {image, text} retrieval recall@{1, 5, 10}.

    Inputs:
        image_features: The image features. The shape is (num_images, feature_size).
        text_features: The text features. The shape is (num_texts, feature_size).
        targets: The target image index for each text. The shape is (num_texts, ).
    """
    VERSION = '0.1.1'

    @dataclasses.dataclass
    class Inputs:
        image_features: torch.Tensor  # Shape: (num_images, num_features)
        text_features: torch.Tensor  # Shape: (num_texts, num_features)
        targets: torch.Tensor  # Shape: (num_text, )

    @dataclasses.dataclass
    class Outputs:
        text_retrieval_recall_1: float
        text_retrieval_recall_5: float
        text_retrieval_recall_10: float
        image_retrieval_recall_1: float
        image_retrieval_recall_5: float
        image_retrieval_recall_10: float

    def execute(self, inputs):
        if len(inputs.text_features) != len(inputs.targets):
            raise ValueError(f"The image_features or the targets have unexpected shape: image_features={inputs.image_features.shape}, targets={inputs.targets.shape}")

        if inputs.image_features.shape[1] != inputs.text_features.shape[1]:
            raise ValueError(f"The image_features or the text_features have unexpected shape: image_features={inputs.image_features.shape}, text_features={inputs.text_features.shape}")

        if max(inputs.targets) >= len(inputs.image_features):
            raise ValueError(f"The targets have unexpected values: max(targets)={max(inputs.targets)}, num_texts={len(inputs.text_features)}")

        if inputs.targets.ndim != 1:
            raise ValueError(f"The targets have unexpected shape: {inputs.targets.shape}")

        logger.info(f"num_images: {len(inputs.image_features)}, num_texts: {len(inputs.text_features)}, num_features: {inputs.image_features.shape[1]}")

        # Nromalize the features
        image_features = inputs.image_features / inputs.image_features.norm(dim=1, keepdim=True)
        text_features = inputs.text_features / inputs.text_features.norm(dim=1, keepdim=True)

        target_text_ids = [[] for _ in range(len(inputs.image_features))]
        for i, target_image_id in enumerate(inputs.targets):
            target_text_ids[target_image_id].append(i)
        max_length = max(len(i) for i in target_text_ids)
        padded = [i + [-1] * (max_length - len(i)) for i in target_text_ids]
        target_text_ids = torch.tensor(padded, dtype=torch.long)

        cosine_similarity = image_features @ text_features.t()  # Shape: (num_images, num_texts)
        text_retrieval_recalls = self._calculate_recalls(cosine_similarity, target_text_ids)
        logger.info(f"Text retrieval recall@1: {text_retrieval_recalls[0]:.3f}, recall@5: {text_retrieval_recalls[1]:.3f}, recall@10: {text_retrieval_recalls[2]:.3f}")

        cosine_similarity = cosine_similarity.t()  # Shape: (num_texts, num_images)
        image_retrieval_recalls = self._calculate_recalls(cosine_similarity, inputs.targets.unsqueeze(1))
        logger.info(f"Image retrieval recall@1: {image_retrieval_recalls[0]:.3f}, recall@5: {image_retrieval_recalls[1]:.3f}, recall@10: {image_retrieval_recalls[2]:.3f}")

        return self.Outputs(text_retrieval_recall_1=text_retrieval_recalls[0],
                            text_retrieval_recall_5=text_retrieval_recalls[1],
                            text_retrieval_recall_10=text_retrieval_recalls[2],
                            image_retrieval_recall_1=image_retrieval_recalls[0],
                            image_retrieval_recall_5=image_retrieval_recalls[1],
                            image_retrieval_recall_10=image_retrieval_recalls[2])

    def dry_run(self, inputs):
        return self.execute(inputs)

    @staticmethod
    def _calculate_recalls(cosine_similarity, targets) -> typing.List[float]:
        assert cosine_similarity.ndim == 2
        assert targets.ndim == 2
        assert len(cosine_similarity) == len(targets)

        sorted_indexes = torch.argsort(cosine_similarity, dim=1, descending=True)
        recalls = []
        for k in [1, 5, 10]:
            top_indexes = sorted_indexes[:, :k].unsqueeze(-1)  # Shape: (num_samples, k, 1)
            k_targets = targets.repeat(1, k).view(len(targets), k, -1)  # Shape: (num_samples, k, num_targets_per_sample)
            correct = torch.eq(top_indexes, k_targets).any(dim=(1, 2)).sum().item()
            recall = correct / len(top_indexes)
            recalls.append(recall)
        return recalls
