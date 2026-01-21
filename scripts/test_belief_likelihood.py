import numpy as np
from objectnav.belief.legacy_bridge import likelihood_from_detection

def main():
    # Fake detector probs for K=2 classes (will add background later in likelihood)
    score = np.array([0.7, 0.3], dtype=np.float64)

    # Minimal fake priors/bins for two classes
    dirichlet_priors = {
        "classA": [np.array([2.0, 2.0])],
        "classB": [np.array([2.0, 2.0])],
    }
    classes_bins = {
        "classA": [100.0],
        "classB": [100.0],
    }

    lv = likelihood_from_detection(score, bbox_scale=5.0, dirichlet_priors=dirichlet_priors, classes_bins=classes_bins)

    # Should be length K+1 because legacy appends background
    assert lv.shape == (3,), lv.shape
    assert np.isfinite(lv).all()
    assert abs(lv.sum() - 1.0) < 1e-6, lv.sum()

    print("Belief likelihood OK:", lv)

if __name__ == "__main__":
    main()
