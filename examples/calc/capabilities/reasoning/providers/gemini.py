from .base import ReasoningProvider


class GeminiProvider(ReasoningProvider):
    provider_name = "gemini"

    def execute(self, prompt):

        return {
            "success": False,
            "provider": "gemini",
            "error": "Gemini connector not implemented.",
        }
