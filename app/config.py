from pathlib import Path

# -------------------------
# Modal App Configuration
# -------------------------

APP_NAME = "modal-comfyui-v2"

# GPU
GPU_TYPE = "T4"

# Persistent storage
VOLUME_NAME = "comfyui-storage"

# Directory inside the container
COMFY_ROOT = Path("/root/comfy")

COMFY_DIR = COMFY_ROOT / "ComfyUI"

MODELS_DIR = COMFY_DIR / "models"

OUTPUT_DIR = COMFY_DIR / "output"

INPUT_DIR = COMFY_DIR / "input"

CUSTOM_NODES_DIR = COMFY_DIR / "custom_nodes"

# Default server settings
HOST = "0.0.0.0"

PORT = 8188
