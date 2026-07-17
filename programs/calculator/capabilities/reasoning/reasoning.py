"""
Bellfre Example Agent Capability
Reasoning Capability v0.4

Purpose:
    Provides a generic reasoning interface for Bellfre agents.

Design Philosophy:

    The agent never calls an LLM directly.

    The agent requests a capability.
    The capability determines WHAT work
    should be performed.

    The Bellfre Policy Layer determines
    HOW that work is executed.

This keeps Bellfre agents independent from
any specific AI provider or execution policy.
"""

from .policy import ReasoningPolicy


class ReasoningCapability:
    """
    Generic reasoning capability implementation.
    """

    capability_id = "mathematics.explain"

    name = "Reasoning Capability"

    description = (
        "Provides natural language reasoning, explanations, "
        "and contextual responses using the configured policy."
    )

    def can_handle(self, request):
        """
        Determine whether this capability
        should handle a request.

        MVP routing:
            Non-arithmetic requests
            are sent here.

        Future:
            Intent classification
            and BAT capability matching.
        """

        if not isinstance(request, str):
            return False

        operators = ["+", "-", "*", "/"]

        #
        # Calculator receives arithmetic.
        #
        if any(operator in request for operator in operators):
            return False

        return True

    def execute_request(self, request):
        """
        Required capability interface.
        """

        return self.execute(request)

    def execute(self, request):
        """
        Execute reasoning through the
        Bellfre Policy Layer.
        """

        policy = ReasoningPolicy()

        result = policy.execute(request)

        #
        # Capabilities identify themselves.
        #
        result["capability"] = self.capability_id

        return result


#
# Standalone Test
#

if __name__ == "__main__":
    reasoning = ReasoningCapability()

    result = reasoning.execute_request(
        "How were modern mathematical symbols developed?"
    )

    print(result)
