"""
Bellfre Capability Provider

Represents an agent that provides
a specific Bellfre capability.
"""

from bellfre.identity import AgentIdentity
 

class CapabilityProvider:
    """
    Represents a resolved capability provider.

    A provider connects:
        Agent Identity
        +
        Capability

    Discovery finds providers.
    Providers do not perform discovery.
    """

    def __init__(
        self,
        identity: AgentIdentity,
        capability_id: str,
    ):
        self.identity = identity
        self.capability_id = capability_id

    @property
    def name(self) -> str:
        """
        Convenience access to provider name.
        """

        return self.identity.name

    @property
    def bui(self) -> str:
        """
        Convenience access to provider BUI.
        """

        return self.identity.bui

    def __repr__(self):
        return (
            f"CapabilityProvider("
            f"name={self.name}, "
            f"capability={self.capability_id})"
        )