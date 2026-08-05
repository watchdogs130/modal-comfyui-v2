import modal

from .config import VOLUME_NAME

# Persistent storage for ComfyUI
volume = modal.Volume.from_name(
    VOLUME_NAME,
    create_if_missing=True,
)
