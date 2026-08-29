"""
Bellfre Manifest Loader

Loads a Bellfre manifest YAML file
and returns the parsed manifest data.
"""

from pathlib import Path
import yaml


def load_manifest(filename: str | Path) -> dict:
    """
    Load a Bellfre manifest YAML file.

    Args:
        filename:
            Path to bellfre.yaml

    Returns:
        Parsed manifest dictionary
    """

    path = Path(filename)

    if not path.exists():
        raise FileNotFoundError(
            f"Manifest not found: {filename}"
        )

    with path.open("r", encoding="utf-8") as file:
        manifest = yaml.safe_load(file)

    if manifest is None:
        raise ValueError(
            f"Manifest is empty: {filename}"
        )

    return manifest