from pathlib import Path

from bellfre.manifest import load_manifest
from bellfre.identity import AgentIdentity
from bellfre.registry import AgentRegistry
from bellfre.agent.record import AgentRecord
from bellfre.agent.description import AgentDescription


MANIFEST = (
    Path(__file__)
    .parents[1]
    / "programs"
    / "calculator"
    / "bellfre.yaml"
)


def test_registry_register_and_find():

    manifest = load_manifest(MANIFEST)

    identity = AgentIdentity(manifest)

    description = AgentDescription.from_manifest(
        manifest
    )

    record = AgentRecord(
        identity,
        description,
    )

    registry = AgentRegistry()

    registry.register(record)

    results = registry.find(
        "arithmetic.calculate"
    )

    assert len(results) == 1
    assert results[0].identity.name == "Bellfre Calculator"


def test_registry_missing_capability():

    manifest = load_manifest(MANIFEST)

    identity = AgentIdentity(
        manifest
    )

    description = AgentDescription.from_manifest(
        manifest
    )

    agent_record = AgentRecord(
        identity,
        description,
    )

    registry = AgentRegistry()

    registry.register(agent_record)

    results = registry.find(
        "finance.analyze"
    )

    assert len(results) == 0

def test_registry_returns_record():

    manifest = load_manifest(MANIFEST)

    registry = AgentRegistry()

    identity = AgentIdentity(manifest)

    description = AgentDescription.from_manifest(
        manifest
    )

    agent_record = AgentRecord(
        identity,
        description,
    )

    record = registry.register(
        agent_record,
        endpoint="http://localhost:8000"
    )

    assert record.bui == "1.0301.0304.00B42.0001"
    assert record.endpoint == "http://localhost:8000"