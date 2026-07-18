"""
Bellfre Agent Registry

Provides in-memory registration and discovery
of Bellfre agent identities.
"""


class AgentRegistry:
    """
    Simple in-memory agent registry.
    """

    def __init__(self):

        self.agents = []

    def register(self, identity):
        """
        Register a Bellfre agent identity.
        """

        self.agents.append(identity)

    def find(self, capability_id: str):
        """
        Find agents supporting a capability.
        """

        return [
            agent
            for agent in self.agents
            if agent.supports(capability_id)
        ]