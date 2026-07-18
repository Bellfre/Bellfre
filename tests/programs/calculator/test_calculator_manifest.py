"""
Calculator Manifest Tests

Validates that the Calculator program
uses a valid Bellfre Manifest.
"""

from pathlib import Path

from bellfre.manifest import (
    load_manifest,
    validate_manifest,
)


MANIFEST_PATH = (
    Path(__file__)
    .parents[3]
    / "programs"
    / "calculator"
    / "bellfre.yaml"
)


def test_calculator_manifest_loads():
    manifest = load_manifest(MANIFEST_PATH)

    assert manifest["agent"]["name"] == "Bellfre Calculator"


def test_calculator_manifest_validates():
    manifest = load_manifest(MANIFEST_PATH)

    assert validate_manifest(manifest) is True