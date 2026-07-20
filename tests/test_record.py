from bellfre.identity import AgentIdentity
from bellfre.agent.description import AgentDescription
from bellfre.agent.record import AgentRecord


def test_agent_record():

    manifest = {
        "agent": {
            "bui": "1.0000.0000.00000.0001",
            "name": "Bellfre HelloWorld",
        },
        "capabilities": [
            {
                "id": "greeting.say"
            }
        ],
    }

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

    result = record.to_dict()

    assert (
        record.bui
        == "1.0000.0000.00000.0001"
    )

    assert (
        record.name
        == "Bellfre HelloWorld"
    )

    assert (
        result["description"]["capabilities"]
        == ["greeting.say"]
    )