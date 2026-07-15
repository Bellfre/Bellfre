from .base import ReasoningProvider


class ClaudeProvider(ReasoningProvider):
    provider_name = "claude"

    def execute(self, prompt):

        return {
            "success": False,
            "provider": "claude",
            "error": "Claude connector not implemented.",
        }
