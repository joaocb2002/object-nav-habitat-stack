# ObjectNav Habitat Stack

This repository provides a reproducible Docker-based stack for running Habitat-Sim / Habitat-Lab experiments locally and on remote GPU servers.

## What you get

- **Reproducible environments** via Docker images stored in GHCR
- **Two-layer image design**
  - `habitat-base`: heavy, stable dependencies (Habitat-Sim, Habitat-Lab, Miniconda)
  - `habitat-project`: project dependencies (YOLO/Ultralytics, CV/ML libs, etc.)
- **Simple run commands**
  - `scripts/run_dev.sh` for interactive development
  - `scripts/run_train.sh` for long training runs

---

## Repository layout

- `docker/base/`
  - Base image build files (`Dockerfile`, `environment.yml`)
  - Changes here trigger rebuilding `habitat-base`
- `docker/project/`
  - Project image build files (`Dockerfile`, `requirements.txt`)
  - Changes here trigger rebuilding `habitat-project`
- `.github/workflows/`
  - GitHub Actions workflows that build/push images to GHCR
- `scripts/`
  - Helper scripts to run containers consistently
- `src/`, `configs/`
  - Your actual research code and configuration files

---

## Images (GHCR)

- Base:  
  `ghcr.io/joaocb2002/object-nav-habitat-stack/habitat-base`
- Project:  
  `ghcr.io/joaocb2002/object-nav-habitat-stack/habitat-project`

**Tags**
- `:main` — latest build from the `main` branch (convenience)
- `:sha-<commit>` — immutable build for exact reproducibility

---

## Prerequisites (host machine)

- Ubuntu 22.04 (recommended)
- NVIDIA driver installed
- Docker Engine installed
- NVIDIA Container Toolkit installed (for `--gpus all`)

---

## Quickstart on a new machine

### 1) Clone the repository

```bash
git clone https://github.com/joaocb2002/object-nav-habitat-stack.git
cd object-nav-habitat-stack
```

### 2) Pull the project image
```bash
docker pull ghcr.io/joaocb2002/object-nav-habitat-stack/habitat-project:main
```

### 3) Prepare datasets and outputs

You must have datasets on the host machine. By default, the scripts expect:

Datasets at ~/datasets

Outputs at ./outputs (auto-created)

If your datasets are elsewhere, set:
```bash
export DATA_DIR=/path/to/datasets
```

### 4) Sanity check
```bash
./scripts/run_dev.sh python scripts/sanity_check.py
```

### 5) Run an experiment

Example:
```bash
./scripts/run_train.sh python train.py
```


## Development workflow

Use **run_dev.sh** for interactive debugging and quick tests:
```bash
./scripts/run_dev.sh bash # Enter the container (common usage!!!)
./scripts/run_dev.sh python some_script.py # Execute the script
```

Your repo is mounted into the container at:

`/workspace`

Datasets are mounted at:

`/data (read-only)`

Outputs are written to:

`/outputs (mapped to host ./outputs by default)`


## Training workflow

Use **run_train.sh** for long runs on servers:

```bash
./scripts/run_train.sh python train.py # Execute the script
```


run_train.sh runs without an interactive terminal and uses `--ipc=host` for better multiprocessing performance.

## Adding Python dependencies

Add project-level Python libraries to:

docker/project/requirements.txt

Then commit + push:

```bash
git add docker/project/requirements.txt
git commit -m "Add dependency: <name>"
git push
```

GitHub Actions will rebuild and push a new habitat-project image.
On any machine where you want the update:

```bash
docker pull ghcr.io/joaocb2002/object-nav-habitat-stack/habitat-project:main
```

## Notes on datasets

Datasets are not included in Docker images. You must download/store them on each machine.
Mount them via DATA_DIR.

## Troubleshooting

If Docker can’t see the GPU: install/configure NVIDIA Container Toolkit.

If habitat_sim import fails: verify host driver + container libs and use the base image sanity check.

If you changed Dockerfiles/env specs: pull the latest image or rebuild.