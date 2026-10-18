"""Evaluate a binary image mask with overlap metrics rather than pixel accuracy."""

import numpy as np


def overlap_metrics(reference_mask: np.ndarray, predicted_mask: np.ndarray) -> dict[str, float]:
    """Return IoU and Dice score for same-shape binary masks."""
    reference = reference_mask.astype(bool)
    prediction = predicted_mask.astype(bool)
    intersection = int(np.sum(reference & prediction))
    union = int(np.sum(reference | prediction))
    return {
        "iou": intersection / max(union, 1),
        "dice": 2 * intersection / max(int(np.sum(reference)) + int(np.sum(prediction)), 1),
    }


if __name__ == "__main__":
    # Illustrative bubble masks: 1 = bubble pixel, 0 = background pixel.
    reference = np.array([[0, 1, 1], [0, 1, 0], [0, 0, 0]])
    predicted = np.array([[0, 1, 0], [0, 1, 0], [0, 0, 0]])
    print(overlap_metrics(reference, predicted))
    print("A mostly-background image can have high pixel accuracy while missing the object of interest.")
