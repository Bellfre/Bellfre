"""
Bellfre Reasoning Provider

Base class for all reasoning providers.
"""


class ReasoningProvider:

    provider_name = "unknown"

    def execute(self, prompt):
        """
        Execute a reasoning request.

        Must return a standardized Bellfre response.
        """

        raise NotImplementedError(
            "Reasoning providers must implement execute()."
        )