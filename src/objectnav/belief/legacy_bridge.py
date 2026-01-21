from __future__ import annotations

import numpy as np

# Keep legacy dependency in ONE place.
from objectnav.legacy.mylib import probtools
from objectnav.legacy.mylib import simtools


def likelihood_from_detection(
    score_vec: np.ndarray,
    bbox_scale: float,
    dirichlet_priors: dict,
    classes_bins: dict,
) -> np.ndarray:
    """
    Compute likelihood vector for an observation (detection).

    This delegates to the legacy implementation:
    - computes bin index from bbox_scale
    - evaluates Dirichlet pdf per class
    - normalizes, then appends a background likelihood element

    Returns:
        np.ndarray of shape (K+1,) where the last entry is background.
    """
    return probtools.compute_likelihood_vector(
        score_vec=score_vec,
        bbox_scale=bbox_scale,
        dirichlet_priors=dirichlet_priors,
        classes_bins=classes_bins,
    )

def target_probability_map(
    belief_map,
    occ_grid_map,
    target_class_idx: int,
    free_color=(255, 255, 255),
):
    """
    Wrapper around legacy simtools.compute_target_prob_map.

    Returns a 2D numpy array where each cell contains P(target_class | cell belief).
    Free cells (white) are set to 0.0, matching legacy behavior.
    """
    return simtools.compute_target_prob_map(
        belief_map=belief_map,
        occ_grid_map=occ_grid_map,
        target_class_idx=target_class_idx,
        free_color=free_color,
    )
