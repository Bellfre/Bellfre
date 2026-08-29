"""
Bellfre JSON Export

Provides JSON serialization
for Bellfre agent records.
"""

import json

from bellfre.agent.record import AgentRecord


def export_agent_json(
    record: AgentRecord,
) -> str:
    """
    Export an AgentRecord as JSON.
    """

    return json.dumps(
        record.to_dict(),
        indent=2,
    )