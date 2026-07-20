from bellfre.capability import (
    CapabilityProvider,
    CapabilityRequest,
)


def test_capability_request():

    request = CapabilityRequest(
        "arithmetic.calculate"
    )

    assert (
        request.capability_id
        == "arithmetic.calculate"
    )


def test_capability_provider():

    from bellfre.identity import AgentIdentity

    manifest = {
        "agent": {
            "bui": "1.0301.0304.00B42.0001",
            "name": "Bellfre Calculator",
        },
        "capabilities": [
            {
                "id": "arithmetic.calculate"
            }
        ],
    }

    identity = AgentIdentity(manifest)

    provider = CapabilityProvider(
        identity,
        "arithmetic.calculate",
    )

    assert provider.name == "Bellfre Calculator"
    assert provider.bui == "1.0301.0304.00B42.0001"
    assert (
        provider.capability_id
        == "arithmetic.calculate"
    )