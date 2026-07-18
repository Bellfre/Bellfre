"""
Bellfre Agent Registry

Provides in-memory registration and discovery
of Bellfre agent identities.
"""

from .record import RegistryRecord

class AgentRegistry:
    """
    Simple in-memory agent registry.
    """

    def __init__(self):

        self.records = []

    def register(self, identity, **kwargs):
        """
        Register a Bellfre agent.
        """

        record = RegistryRecord(
            identity,
            **kwargs
        )

        self.records.append(record)

        return record

    def find(self, capability_id: str):

        return [
            record
            for record in self.records
            if record.supports(capability_id)
        ]