"""
Bellfre Example Agent
Agent Runtime v0.2.1

Purpose:
    Provides the base agent container for capabilities.

Architecture:
    An agent is not a model.

    An agent is a collection of capabilities
    that respond to requests.
"""


class Agent:

    def __init__(self, name, version="0.1.0"):

        self.name = name
        self.version = version

        self.memory = []
        self.capabilities = []


    def remember(self, item):
        """
        Store agent memory.
        """

        self.memory.append(item)



    def add_capability(self, capability):
        """
        Attach a capability to this agent.
        """

        self.capabilities.append(capability)



    def list_capabilities(self):
        """
        Return available capability IDs.
        """

        return [
            capability.capability_id
            for capability in self.capabilities
        ]



    def think(self, user_input):
        """
        Route a request to the appropriate capability.

        The agent does not perform the work.
        The agent determines which capability
        should handle the request.
        """

        request = {
            "input": user_input
        }

        for capability in self.capabilities:

            if capability.can_handle(user_input):

                return capability.execute_request(request)


        return {
            "success": False,
            "agent": self.name,
            "error": "No capability available",
            "available_capabilities": self.list_capabilities()
        }