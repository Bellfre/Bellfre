"""
Abstract Class
Base class to add a provider
"""


class ReasoningProvider:
    provider_name = "base"

    def execute(self, prompt):
        raise NotImplementedError
