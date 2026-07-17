"""
Bellfre Reasoning Policy
Policy Layer v0.1

Purpose:
    Provides a policy layer between a capability
    and its execution provider.

Design Philosophy:

    A capability determines WHAT work is performed.

    A policy determines HOW that work should
    be executed.

Future policy decisions may include:

    - Scope enforcement
    - Cost management
    - Privacy rules
    - Local knowledge lookup
    - Local LLM routing
    - Cloud provider selection
    - Retry / fallback
    - Response depth
    - Telemetry
"""

from config import REASONING_PROVIDER

from .providers.mock import MockProvider
from .providers.openai import OpenAIProvider
from .providers.claude import ClaudeProvider
from .providers.gemini import GeminiProvider
from .providers.ollama import OllamaProvider


class ReasoningPolicy:
    """
    Bellfre reasoning execution policy.

    This MVP implementation performs provider
    selection only.

    Future versions will become the execution
    gateway for all reasoning requests.
    """

    def execute(self, request):

        provider = REASONING_PROVIDER.lower()

        if provider == "mock":
            engine = MockProvider()

        elif provider == "openai":
            engine = OpenAIProvider()

        elif provider == "claude":
            engine = ClaudeProvider()

        elif provider == "gemini":
            engine = GeminiProvider()

        elif provider == "ollama":
            engine = OllamaProvider()

        elif provider == "discovery":
            return {
                "success": False,
                "error": "Bellfre Discovery routing is not implemented.",
            }

        else:
            return {
                "success": False,
                "error": f"Unknown reasoning provider: {provider}",
            }

        #
        # Future policy hooks:
        #
        # request = validate_scope(request)
        # request = check_cache(request)
        # request = optimize_cost(request)
        # request = apply_privacy(request)
        #
        #
        # The Bellfre Policy Layer exists to separate
        # execution decisions from execution providers.
        #
        # Future versions may enforce scope, optimize
        # cost, select local or cloud providers, or
        # apply enterprise policies before dispatching
        # the request.
        #
        return engine.execute(request)
