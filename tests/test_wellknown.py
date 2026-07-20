from bellfre.agent.record import AgentRecord
from bellfre.agent.description import AgentDescription
from bellfre.identity import (
    AgentIdentity,
    validate_bui,
)
from bellfre.manifest import load_manifest
from bellfre.wellknown import (
    create_agent_document,
)


MANIFEST = (
    "programs/calculator/bellfre.yaml"
)


def build_record():

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

    return AgentRecord(
        identity,
        description,
    )


def test_create_agent_document():

    record = build_record()

    document = (
        create_agent_document(
            record
        )
    )

    assert (
        document["bui"]
        == record.bui
    )

    assert validate_bui(
        document["bui"]
    )

    assert (
        document["name"]
        == "Bellfre Calculator"
    )

    assert (
        "arithmetic.calculate"
        in document["capabilities"]
    )


def test_agent_document_shape():

    record = build_record()

    document = (
        create_agent_document(
            record
        )
    )

    assert set(
        document.keys()
    ) == {
        "bui",
        "name",
        "version",
        "capabilities",
    }