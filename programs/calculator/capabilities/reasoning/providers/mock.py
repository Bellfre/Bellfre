"""
Bellfre Example Agent Capability
Mock Reasoning Provider v0.1

Purpose:
    Development and testing provider for the
    Reasoning Capability.

This provider requires no external services.
"""

from .base import ReasoningProvider


class MockProvider(ReasoningProvider):
    provider_name = "mock"
    model_name = "none"

    def execute(self, prompt):

        return {
            "success": True,
            "provider": self.provider_name,
            "model": self.model_name,
            "prompt": prompt,
            "response": (
                "Mock reasoning provider. No external reasoning engine configured."
            ),
        }
