"""
Bellfre Capability Request

Defines a request for discovering
agents capable of providing a capability.
"""


class CapabilityRequest:
    """
    Represents a request for a Bellfre capability.
    """

    def __init__(
        self,
        capability_id: str,
    ):
        self.capability_id = capability_id

    def __repr__(self):
        return (
            f"CapabilityRequest("
            f"capability_id={self.capability_id}"
            f")"
        )