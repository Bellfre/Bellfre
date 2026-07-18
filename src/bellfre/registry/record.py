"""
Bellfre Registry Record

Represents an agent registration entry.
"""


class RegistryRecord:
    """
    A registered Bellfre agent.
    """

    def __init__(
        self,
        identity,
        endpoint=None,
        status="active",
    ):

        self.identity = identity
        self.endpoint = endpoint
        self.status = status

    @property
    def bui(self):
        return self.identity.bui

    def supports(self, capability_id: str) -> bool:
        return self.identity.supports(
            capability_id
        )

    def __repr__(self):
        return (
            f"RegistryRecord("
            f"name={self.identity.name}, "
            f"status={self.status})"
        )