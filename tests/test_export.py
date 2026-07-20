from bellfre.agent.record import AgentRecord
from bellfre.agent.description import AgentDescription
from bellfre.identity import AgentIdentity
from bellfre.export import export_agent_json
from bellfre.manifest import load_manifest


MANIFEST = (
    "programs/calculator/bellfre.yaml"
)


def test_agent_json_export():

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

    result = export_agent_json(
        record
    )

    assert '"bui"' in result
    assert (
        "Bellfre Calculator"
        in result
    )