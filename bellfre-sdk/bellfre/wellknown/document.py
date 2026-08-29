"""
Bellfre Well-Known Agent Document

Creates the public identity document
served from:

/.well-known/bellfre-agent.json
"""


from bellfre.agent.record import AgentRecord


def create_agent_document(
    record: AgentRecord,
) -> dict:
    """
    Create portable Bellfre agent document.
    """

    return {
        "bui": record.bui,
        "name": record.name,
        "version": (
            record.identity.version
        ),
        "capabilities": (
            record.description.capabilities
        ),
    }