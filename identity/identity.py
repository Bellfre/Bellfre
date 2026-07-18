"""
Bellfre Agent Identity

Provides a normalized identity object
created from a validated Bellfre Manifest.
"""


class AgentIdentity:
    """
    Represents the permanent identity
    of a Bellfre-enabled agent.
    """

    def __init__(self, manifest: dict):

        agent = manifest["agent"]

        self.bui = agent["bui"]
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