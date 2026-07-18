"""
Discovery tests.
"""

from pathlib import Path

from bellfre.discovery import Discovery
from bellfre.identity import AgentIdentity
from bellfre.manifest import load_manifest
from bellfre.registry import AgentRegistry


MANIFEST = (
    Path(__file__).parent.parent
    / "programs"
    / "calculator"
    / "bellfre.yaml"
)


def test_discovery_empty_registry():

    registry = AgentRegistry()

    discovery = Discovery(registry)

    results = discovery.find(
        "arithmetic.calculate"
    )

    assert results == []


def test_discovery_finds_agent():

    manifest = load_manifest(MANIFEST)

    identity = AgentIdentity(manifest)

    registry = AgentRegistry()

    registry.register(identity)

    discovery = Discovery(registry)

    results = discovery.find(
        "arithmetic.calculate"
    )

    assert len(results) == 1
    assert (
        results[0].identity.name
        == "Bellfre Calculator"
    )


def test_discovery_unknown_capability():

    manifest = load_manifest(MANIFEST)

    identity = AgentIdentity(manifest)

    registry = AgentRegistry()

    registry.register(identity)

    discovery = Discovery(registry)

    results = discovery.find(
        "weather.forecast"
    )

    assert results == []


def test_discovery_multiple_agents():

    manifest = load_manifest(MANIFEST)

    capability = manifest["capabilities"][0]["id"]

    identity1 = AgentIdentity(manifest)

    identity2 = AgentIdentity(manifest)

    registry = AgentRegistry()

    registry.register(identity1)

    registry.register(identity2)

    discovery = Discovery(registry)

    results = discovery.find(
        capability
    )

    assert len(results) == 2