from bellfre.capability import CapabilityRequest


def test_capability_request():

    request = CapabilityRequest(
        "arithmetic.calculate"
    )

    assert (
        request.capability_id
        == "arithmetic.calculate"
    )