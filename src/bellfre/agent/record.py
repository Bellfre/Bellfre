"""
Bellfre Agent Record

Canonical representation of a Bellfre agent.

An AgentRecord combines:
- Agent identity
- Agent description

It does not handle:
- Discovery
- Registry operations
- Network endpoints
- Protocol transports
"""


from bellfre.identity import AgentIdentity
from bellfre.agent.description import AgentDescription


class AgentRecord:
    """
    Represents a complete Bellfre agent record.

    This is the portable object used by
    future registries and adapters.
    """

    def __init__(
        self,
        identity: AgentIdentity,
        description: AgentDescription,
    ):
        self.identity = identity
        self.description = description

    @property
    def bui(self) -> str:
        """
        Convenience access to BUI.
        """

        return self.identity.bui

    @property
    def name(self) -> str:
        """
        Convenience access to agent name.
        """

        return self.identity.name

    def to_dict(self) -> dict:
        """
        Convert record into portable format.
        """

        return {
            "identity": {
                "bui": self.identity.bui,
                "name": self.identity.name,
            },
            "description": (
                self.description.to_dict()
            ),
        }

    def __repr__(self):
        return (
            f"AgentRecord("
            f"name={self.name}, "
            f"bui={self.bui})"
        )