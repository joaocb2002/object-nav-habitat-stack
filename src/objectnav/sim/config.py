from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

@dataclass(frozen=True)
class SimConfig:
    """
    Simulation/environment configuration constants.
    Prefer overriding via a run config (YAML) rather than editing code.
    """

    # --- Maps / grids ---
    map_resolution: float = 0.05
    grid_resolution: float = 0.25
    cell_side: float = 0.25

    # --- Agent geometry ---
    agent_height: float = 1.5
    agent_radius: float = 0.20 
    agent_max_climb: float = 0.2
    agent_max_slope: float = 45.0

    # --- Sensors ---
    obs_scale: float = 9/16
    rgb_width: int = 1024
    rgb_height: int = int(1024*obs_scale)
    sensor_height: float = 1.5
    hfov_deg: float = 90.0

    # --- Action magnitudes ---
    forward_step: float = 0.25
    turn_deg: float = 30.0

    # --- Habitat dataset paths ---
    scene_dataset_config: Optional[Path] = None
    scene_id: Optional[str] = None

    # --- Physics ---
    enable_physics: bool = False