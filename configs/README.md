# Configs

This project uses a Hydra-style configuration layout.

- `config.yaml` is the root composition file.
- `sim/`, `navmesh/`, `grid_map/` are config groups.
- `experiment/` contains reproducible experiment presets (compositions).
- `runs/` contains ad-hoc developer run presets.

Precedence (highest to lowest):
1. CLI overrides
2. YAML composition (`configs/*.yaml`)
3. Code defaults (structured configs / dataclasses)
