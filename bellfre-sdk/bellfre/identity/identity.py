"""
Bellfre Agent Identity

Provides a normalized identity object
created from a validated Bellfre Manifest.
"""
from .bui import validate_bui


class AgentIdentity:
    """
    Represents the permanent identity
    of a Bellfre-enabled agent.
    """

    def __init__(self, manifest: dict):

        agent = manifest["agent"]

        self.bui = agent["bui"]

        if not validate_bui(self.bui):
            raise ValueError(
                f"Invalid BUI format: {self.bui}"
            )
                
        self.name = agent["name"]
        self.version = agent.get("version")

        self.publisher = agent.get(
            "publisher",
            {}
        )

        self.capabilities = manifest.get(
            "capabilities",
            []
        )

    def supports(self, capability_id: str) -> bool:
        """
        Check whether this agent supports
        a specific capability.
        """

        return any(
            capability.get("id") == capability_id
            for capability in self.capabilities
        )

    def __repr__(self):
        return (
            f"AgentIdentity("
            f"name={self.name}, "
            f"bui={self.bui})"
        )
    
    