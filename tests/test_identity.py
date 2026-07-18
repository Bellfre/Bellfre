from pathlib import Path

from bellfre.manifest import load_manifest
from bellfre.identity import AgentIdentity


MANIFEST = (
    Path(__file__)
    .parents[1]
    / "programs"
    / "calculator"
    / "bellfre.yaml"
)


def test_agent_identity():

    manifest = load_manifest(MANIFEST)

    identity = AgentIdentity(
        manifest
    )

    assert identity.name == "Bellfre Calculator"
    assert identity.bui == "1.301.0304.B42.001"

    
def test_agent_identity_supports_capability():

    manifest = load_manifest(MANIFEST)

    identity = AgentIdentity(manifest)

    assert identity.supports(
        "arithmetic.calculate"
    )

    assert not identity.supports(
        "finance.analyze"
    )