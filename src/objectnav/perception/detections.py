from dataclasses import dataclass
from typing import Optional, Tuple

@dataclass(frozen=True) # Immutable (read-only) dataclass
class Detection:
    cls: int
    conf: float
    xyxy: Tuple[float, float, float, float]  # x1,y1,x2,y2
    scale: float  # detection_area / image_area
    probs: Tuple[float, ...]  # class probability vector (softmax)
    track_id: Optional[int] = None # Optional tracking ID
