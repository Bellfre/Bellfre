from pathlib import Path

from bellfre.manifest import load_manifest
from bellfre.identity import AgentIdentity
from bellfre.registry import AgentRegistry


MANIFEST = (
    Path(__file__)
    .parents[1]
    / "programs"
    / "calculator"
    / "bellfre.yaml"
)


def test_registry_register_and_find():

    manifest = load_manifest(MANIFEST)

    identity = AgentIdentity(
        manifest
    )

    registry = AgentRegistry()

    registry.register(identity)

    results = registry.find(
        "arithmetic.calculate"
    )

    assert len(results) == 1
    assert results[0].name == "Bellfre Calculator"


def test_registry_missing_capability():

    manifest = load_manifest(MANIFEST)

    identity = AgentIdentity(
        manifest
    )

    registry = AgentRegistry()

    registry.register(identity)

    results = registry.find(
        "finance.analyze"
    )

    assert len(results) == 0