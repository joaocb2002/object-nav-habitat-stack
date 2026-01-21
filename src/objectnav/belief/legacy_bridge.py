from __future__ import annotations
import numpy as np

# We keep the dependency on legacy in ONE place.
from objectnav.legacy.mylib import probtools


def likelihood_from_detection(
    score_vec: np.ndarray,
    bbox_scale: float,
    dirichlet_priors: dict,
    classes_bins: dict,
) -> np.ndarray:
    """
    Wrapper around legacy probtools.compute_likelihood_vector.

    score_vec: categorical probs from detector (sum ~ 1)
    bbox_scale: bbox area as % of image (or whatever you used)
    dirichlet_priors/classes_bins: calibration data
    """
    return probtools.compute_likelihood_vector(
        score_vec=score_vec,
        bbox_scale=bbox_scale,
        dirichlet_priors=dirichlet_priors,
        classes_bins=classes_bins,
    )
