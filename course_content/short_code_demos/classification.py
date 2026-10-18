"""Inspect why a binary classification threshold is an engineering choice."""

import numpy as np


def binary_metrics(labels: np.ndarray, probability_of_positive: np.ndarray, threshold: float) -> dict[str, float | int]:
    """Calculate confusion counts and common metrics for a stated threshold."""
    predicted = probability_of_positive >= threshold
    positive = labels.astype(bool)
    true_positive = int(np.sum(predicted & positive))
    true_negative = int(np.sum(~predicted & ~positive))
    false_positive = int(np.sum(predicted & ~positive))
    false_negative = int(np.sum(~predicted & positive))
    total = len(labels)
    return {
        "true_positive": true_positive,
        "true_negative": true_negative,
        "false_positive": false_positive,
        "false_negative": false_negative,
        "accuracy": (true_positive + true_negative) / total,
        "recall": true_positive / max(true_positive + false_negative, 1),
        "precision": true_positive / max(true_positive + false_positive, 1),
    }


if __name__ == "__main__":
    # 1 = defective fastener; a false negative is a missed defective part.
    labels = np.array([0, 1, 0, 1, 0, 0])
    probabilities = np.array([0.10, 0.62, 0.51, 0.44, 0.08, 0.33])
    for threshold in (0.50, 0.35):
        print(f"threshold={threshold:.2f}: {binary_metrics(labels, probabilities, threshold)}")
    print("Choose a threshold from the consequence of false positives and false negatives, not accuracy alone.")
