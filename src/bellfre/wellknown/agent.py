"""
Bellfre Well-Known Agent Document

Creates the portable document exposed
through /.well-known/bellfre-agent.json
"""

from bellfre.agent.record import AgentRecord


def create_agent_document(
    record: AgentRecord,
) -> dict:
    """
    Create a Bellfre well-known agent document.

    This function does not handle:
    - HTTP
    - networking
    - endpoints
    - transports

    It only creates the agent description.
    """

    return {
        "bui": record.bui,
        "name": record.name,
        "version": (
            record.description.version
        ),
        "capabilities": (
            record.description.capabilities
        ),
    }