"""Reduce correlated sensor features with PCA and retain reconstruction evidence."""

import numpy as np


def fit_pca(data: np.ndarray, n_components: int) -> dict[str, np.ndarray]:
    """Center data, compute PCA by SVD, and return a low-rank reconstruction."""
    mean = np.mean(data, axis=0)
    centered = data - mean
    _, singular_values, right_vectors = np.linalg.svd(centered, full_matrices=False)
    components = right_vectors[:n_components]
    scores = centered @ components.T
    reconstruction = scores @ components + mean
    variance = singular_values**2
    return {
        "mean": mean,
        "components": components,
        "scores": scores,
        "reconstruction": reconstruction,
        "explained_variance_ratio": variance / variance.sum(),
    }


if __name__ == "__main__":
    # Correlated illustrative sensor signals: temperature [K] and pressure [kPa].
    data = np.array([[300.0, 100.0], [302.0, 101.0], [304.0, 102.1], [306.0, 103.0]])
    result = fit_pca(data, n_components=1)
    print(f"variance retained: {result['explained_variance_ratio'][0]:.3f}")
    print("first reconstructed observation:", np.round(result["reconstruction"][0], 3))
    print("Inspect reconstruction error before interpreting a component as a physical mechanism.")
