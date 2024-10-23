import collections
import dataclasses
import logging
import math
import string
import typing
import torch
import irisml.core

logger = logging.getLogger(__name__)


class Task(irisml.core.TaskBase):
    """Evaluate captioning prediction results.

    Supported metrics are BLEU-1, BLEU-2, BLEU-3, BLEU-4 and CIDEr.

    Note that this task uses the simplest tokenizer. It might have different results from the pycocoevalcap results.

    This task is experimental. The evaluation result might not be accurate.
    """
    VERSION = '0.1.1'

    CIDER_SIGMA = 6.0

    @dataclasses.dataclass
    class Inputs:
        predictions: typing.List[str]
        targets: typing.List[typing.List[str]]

    @dataclasses.dataclass
    class Outputs:
        bleu1: float
        bleu2: float
        bleu3: float
        bleu4: float
        cider: float

    def execute(self, inputs):
        if len(inputs.predictions) != len(inputs.targets):
            raise ValueError(f"Number of predictions ({len(inputs.predictions)}) does not match number of targets ({len(inputs.targets)})")

        if len(inputs.predictions) == 0:
            raise ValueError("No predictions provided")

        logger.info(f"Evaluating {len(inputs.predictions)} predictions")

        total_pred_ngrams = collections.Counter()
        document_frequency = collections.Counter()

        all_pred_ngrams = []
        all_target_ngrams = []

        bleu_numerator = [0, 0, 0, 0]
        bleu_denominator = [0, 0, 0, 0]
        bleu_preds_length = 0
        bleu_targets_length = 0
        remove_punctuation = str.maketrans('', '', string.punctuation)
        for pred, targets in zip(inputs.predictions, inputs.targets):
            tokenized_pred = pred.translate(remove_punctuation).lower().split()
            tokenized_targets = [t.translate(remove_punctuation).lower().split() for t in targets]

            bleu_preds_length += len(tokenized_pred)
            bleu_targets_length += len(min(tokenized_targets, key=lambda x: abs(len(tokenized_pred) - len(x))))  # Closest length to prediction

            # Get the count of N grams
            pred_ngrams = self._get_ngrams(tokenized_pred)
            target_ngrams = [self._get_ngrams(t) for t in tokenized_targets]
            total_target_ngrams_for_image = collections.Counter()
            for target_ngram in target_ngrams:
                total_target_ngrams_for_image |= target_ngram

            # Save total counts for CIDEr
            total_pred_ngrams |= pred_ngrams
            document_frequency.update(set(total_target_ngrams_for_image))
            all_pred_ngrams.append(pred_ngrams)
            all_target_ngrams.append(target_ngrams)

            # Count the numbers for BLEU score
            intersection = pred_ngrams & total_target_ngrams_for_image
            for key, value in intersection.items():
                bleu_numerator[len(key) - 1] += value
            for key, value in pred_ngrams.items():
                bleu_denominator[len(key) - 1] += value

        # Calculate BLEU score
        bleu_scores = []
        bleu = 1.0
        penalty = 1.0 if bleu_preds_length > bleu_targets_length else math.exp(1 - bleu_targets_length / bleu_preds_length)
        for i in range(4):
            bleu *= (bleu_numerator[i] + 1e-15) / (bleu_denominator[i] + 1e-9)  # Add epsilon to avoid zero division and zero bleu.
            bleu_scores.append((bleu ** (1 / (i + 1))) * penalty)

        # Calculate CIDEr score
        log_num_targets = math.log(len(inputs.targets))
        cider_scores = []
        for pred_ngrams, target_ngrams in zip(all_pred_ngrams, all_target_ngrams):
            pred_vector = self._get_cider_vec(pred_ngrams, document_frequency, log_num_targets)
            pred_length = self._get_length_from_ngram(pred_ngrams)
            scores = torch.zeros((4,))
            for t in target_ngrams:
                target_vector = self._get_cider_vec(t, document_frequency, log_num_targets)
                target_length = self._get_length_from_ngram(t)
                scores += self._calculate_cider_similarity(pred_vector, target_vector, pred_length, target_length)
            score = scores.mean() / len(target_ngrams) * 10.0
            cider_scores.append(score)
        cider_score = sum(cider_scores) / len(cider_scores)

        logger.info(f"BLEU-1: {bleu_scores[0]:.4f}, BLEU-2: {bleu_scores[1]:.4f}, BLEU-3: {bleu_scores[2]:.4f}, BLEU-4: {bleu_scores[3]:.4f}, CIDEr: {cider_score:.4f}")
        return self.Outputs(bleu1=float(bleu_scores[0]), bleu2=float(bleu_scores[1]), bleu3=float(bleu_scores[2]), bleu4=float(bleu_scores[3]), cider=float(cider_score))

    def dry_run(self, inputs):
        return self.execute(inputs)

    @staticmethod
    def _get_ngrams(tokens):
        ngrams = collections.Counter()
        for n in range(1, 5):
            for i in range(len(tokens) - n + 1):
                ngrams[tuple(tokens[i:i + n])] += 1
        return ngrams

    @staticmethod
    def _get_length_from_ngram(ngram):
        return sum([value for key, value in ngram.items() if len(key) == 1])

    @staticmethod
    def _get_cider_vec(ngrams, document_ngrams, log_num_targets):
        vec = [collections.defaultdict(float) for _ in range(4)]
        for ngram, count in ngrams.items():
            df = math.log(max(1.0, document_ngrams[ngram]))
            vec[len(ngram) - 1][ngram] = count * (log_num_targets - df)
        return vec

    def _calculate_cider_similarity(self, pred_vec, target_vec, pred_length, target_length):
        scores = torch.zeros((4,))
        delta = pred_length - target_length

        for i in range(4):
            for ngram, count in pred_vec[i].items():
                scores[i] += min(count, target_vec[i][ngram]) * target_vec[i][ngram]

            pred_norm = math.sqrt(sum(count * count for count in pred_vec[i].values()))
            target_norm = math.sqrt(sum(count * count for count in target_vec[i].values()))

            if pred_norm != 0 and target_norm != 0:
                scores[i] /= pred_norm * target_norm

            scores[i] *= math.exp(-delta ** 2 / (2 * (self.CIDER_SIGMA ** 2)))

        return scores
