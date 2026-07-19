"""
Discovery tests.
"""

from pathlib import Path

from bellfre.capability import CapabilityRequest
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

    request = CapabilityRequest(
        "arithmetic.calculate"
    )

    results = discovery.find(request)

    assert results == []


def test_discovery_finds_agent():

    manifest = load_manifest(MANIFEST)

    identity = AgentIdentity(manifest)

    registry = AgentRegistry()

    registry.register(identity)

    discovery = Discovery(registry)

    request = CapabilityRequest(
        "arithmetic.calculate"
    )

    results = discovery.find(request)

    assert len(results) == 1

    provider = results[0]

    assert provider.name == "Bellfre Calculator"
    assert provider.bui == "1.301.0304.B42.001"
    assert (
        provider.capability_id
        == "arithmetic.calculate"
    )


def test_discovery_unknown_capability():

    manifest = load_manifest(MANIFEST)

    identity = AgentIdentity(manifest)

    registry = AgentRegistry()

    registry.register(identity)

    discovery = Discovery(registry)

    request = CapabilityRequest(
        "weather.forecast"
    )

    results = discovery.find(request)

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

    request = CapabilityRequest(
        capability
    )

    results = discovery.find(request)

    assert len(results) == 2

    assert all(
        provider.capability_id == capability
        for provider in results
    )