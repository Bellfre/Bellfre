"""
Bellfre Example Agent Capability
Reasoning Capability v0.3

Purpose:
    Provides a generic reasoning interface for Bellfre agents.

Design Philosophy:

    The agent never calls an LLM directly.

    The agent requests a capability.
    The capability determines how reasoning is provided.

    Today this may route to:
        - Mock Provider
        - ChatGPT
        - Claude
        - Gemini
        - Local LLM

    Future routing may include:
        - Another Bellfre agent discovered through BAT/BDN.

This keeps Bellfre agents independent from any single
AI provider or model ecosystem.
"""

from .providers.mock import MockProvider
from .providers.openai import OpenAIProvider
from .providers.claude import ClaudeProvider
from .providers.gemini import GeminiProvider
from .providers.ollama import OllamaProvider

from config import REASONING_PROVIDER

class ReasoningCapability:
    """
    Generic reasoning capability implementation.
    """
    capability_id = "mathematics.explain"

    name = "Reasoning Capability"

    description = (
        "Provides natural language reasoning, explanations, "
        "and contextual responses using the configured provider."
    )

    def can_handle(self, request):
        """
        Determine whether this capability should handle a request.

        MVP routing:
            Non-mathematical questions are sent here.

        Future:
            Intent classification and BCT matching.
        """

        if not isinstance(request, str):
            return False

        operators = [
            "+",
            "-",
            "*",
            "/"
        ]

        # Calculator gets arithmetic requests.
        if any(
            operator in request
            for operator in operators
        ):
            return False

        return True

    def execute_request(self, request):
        """
        Execute a reasoning request.

        Required capability interface.
        """

        return self.execute(request)
    
    def execute(self, request):
        """
        Execute reasoning using configured provider.

        Provider abstraction remains hidden
        from the agent.
        """

        provider = REASONING_PROVIDER.lower()

        if provider == "mock":
            provider = MockProvider()

        elif provider == "openai":
            provider = OpenAIProvider()

        elif provider == "claude":
            provider = ClaudeProvider()

        elif provider == "gemini":
            provider = GeminiProvider()

        elif provider == "ollama":
            provider = OllamaProvider()

        elif provider == "discovery":
            return {
                "success": False,
                "capability": self.capability_id,
                "error": (
                    "Bellfre Discovery routing is not implemented."
                )
            }

        else:
            return {
                "success": False,
                "capability": self.capability_id,
                "error": f"Unknown reasoning provider: {provider}"
            }

        result = provider.execute(request)

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