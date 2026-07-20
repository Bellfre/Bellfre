"""
Bellfre Agent Description

Provides a portable representation of a Bellfre agent.

This object describes:
- Identity
- Version
- Capabilities

It does not handle:
- Endpoints
- Networking
- Discovery
- Transport protocols
"""


class AgentDescription:
    """
    Represents a Bellfre agent description.

    This is the common object used by:
    - registries
    - adapters
    - endpoints
    """

    def __init__(
        self,
        bui: str,
        name: str,
        version: str,
        capabilities: list[str],
    ):
        self.bui = bui
        self.name = name
        self.version = version
        self.capabilities = capabilities

    def to_dict(self) -> dict:
        """
        Convert description to portable format.
        """

        return {
            "bui": self.bui,
            "name": self.name,
            "version": self.version,
            "capabilities": self.capabilities,
        }

    def __repr__(self):
        return (
            f"AgentDescription("
            f"name={self.name}, "
            f"bui={self.bui})"
        )
    
    @classmethod
    def from_manifest(cls, manifest: dict):
        """
        Create an AgentDescription from
        a Bellfre manifest.
        """

        agent = manifest["agent"]

        capabilities = [
            capability["id"]
            for capability in manifest.get(
                "capabilities",
                []
            )
        ]

        return cls(
            bui=agent["bui"],
            name=agent["name"],
            version=agent.get(
                "version",
                "unknown"
            ),
            capabilities=capabilities,
        )