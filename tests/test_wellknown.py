from bellfre.agent.record import AgentRecord
from bellfre.agent.description import AgentDescription
from bellfre.identity import AgentIdentity
from bellfre.manifest import load_manifest
from bellfre.wellknown import (
    create_agent_document,
)


MANIFEST = (
    "programs/calculator/bellfre.yaml"
)


def test_create_agent_document():

    manifest = load_manifest(
        MANIFEST
    )

    identity = AgentIdentity(
        manifest
    )

    description = (
        AgentDescription
        .from_manifest(manifest)
    )

    record = AgentRecord(
        identity,
        description,
    )

    document = (
        create_agent_document(
            record
        )
    )

    assert (
        document["bui"]
        == record.bui
    )

    assert (
        document["name"]
        == "Bellfre Calculator"
    )

    assert (
        "arithmetic.calculate"
        in document["capabilities"]
    )