from pathlib import Path

from bellfre.agent.description import AgentDescription
from bellfre.manifest import load_manifest


MANIFEST = (
    Path(__file__).parent.parent
    / "programs"
    / "calculator"
    / "bellfre.yaml"
)


def test_agent_description():

    description = AgentDescription(
        bui="1.301.0304.B42.001",
        name="Bellfre Calculator",
        version="0.1.0",
        capabilities=[
            "arithmetic.calculate",
            "mathematics.explain",
        ],
    )

    result = description.to_dict()

    assert result["bui"] == "1.301.0304.B42.001"
    assert result["name"] == "Bellfre Calculator"

    assert (
        "arithmetic.calculate"
        in result["capabilities"]
    )


def test_agent_description_from_manifest():

    manifest = load_manifest(MANIFEST)

    description = (
        AgentDescription
        .from_manifest(manifest)
    )

    assert (
        description.name
        == "Bellfre Calculator"
    )

    assert (
        description.bui
        == "1.301.0304.B42.001"
    )

    assert (
        "arithmetic.calculate"
        in description.capabilities
    )