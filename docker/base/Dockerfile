# CUDA runtime on Ubuntu 22.04 (official NVIDIA CUDA image).
# Note: Docker Hub nvidia/cudagl doesn't have ubuntu22.04 tags; use nvidia/cuda + GLVND/EGL setup instead.
FROM nvidia/cuda:12.4.0-runtime-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive

# System deps:
# - build tools, download tools
# - common X/GL runtime libs
# - GLVND loader libs (EGL/OpenGL)
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget curl git ca-certificates build-essential \
    libglib2.0-0 libsm6 libxext6 libxrender1 \
    libopengl0 libglvnd0 libgl1 libegl1 libglx0 libgles2 \
    && rm -rf /var/lib/apt/lists/*

# IMPORTANT:
# Your failure mode was that only Mesa's vendor file existed (50_mesa.json) and NVIDIA's (10_nvidia.json) did not.
# Add the NVIDIA EGL vendor entry so GLVND can route EGL calls to the NVIDIA driver at runtime.
RUN mkdir -p /usr/share/glvnd/egl_vendor.d && \
    printf '{\n  "file_format_version": "1.0.0",\n  "ICD": { "library_path": "libEGL_nvidia.so.0" }\n}\n' \
      > /usr/share/glvnd/egl_vendor.d/10_nvidia.json

# Make GLVND prefer NVIDIA EGL in headless runs (helps avoid Mesa/conda hijacking).
ENV __EGL_VENDOR_LIBRARY_FILENAMES=/usr/share/glvnd/egl_vendor.d/10_nvidia.json
ENV LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu:${LD_LIBRARY_PATH}

# Install Miniconda
ENV CONDA_DIR=/opt/conda
RUN wget -q https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/miniconda.sh && \
    bash /tmp/miniconda.sh -b -p $CONDA_DIR && \
    rm /tmp/miniconda.sh

ENV PATH=$CONDA_DIR/bin:$PATH

# Accept Anaconda TOS (as you had)
RUN conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main && \
    conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r

# Create conda env
COPY environment.yml /tmp/environment.yml
RUN conda env create -f /tmp/environment.yml && \
    conda clean -afy

# Activate the environment by default
ENV CONDA_DEFAULT_ENV=habitat
ENV PATH=$CONDA_DIR/envs/habitat/bin:$PATH

# Sanity check
RUN python - <<'EOF'
import habitat_sim
print("Habitat-Sim imported successfully")
EOF

WORKDIR /workspace
