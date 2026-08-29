"""
Bellfre Registry Record

Represents an agent registration entry.
"""


from bellfre.agent.record import AgentRecord


class RegistryRecord:
    """
    A registered Bellfre agent.

    Registry metadata wraps a canonical
    AgentRecord.
    """

    def __init__(
        self,
        agent_record: AgentRecord,
        endpoint=None,
        status="active",
    ):

        self.agent_record = agent_record
        self.endpoint = endpoint
        self.status = status

    @property
    def identity(self):
        return self.agent_record.identity

    @property
    def bui(self):
        return self.agent_record.bui

    @property
    def name(self):
        return self.agent_record.name

    def supports(
        self,
        capability_id: str,
    ) -> bool:

        return (
            capability_id
            in self.agent_record
                .description
                .capabilities
        )

    def __repr__(self):

        return (
            f"RegistryRecord("
            f"name={self.name}, "
            f"status={self.status})"
        )