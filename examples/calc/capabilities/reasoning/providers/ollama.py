from .base import ReasoningProvider


class OllamaProvider(ReasoningProvider):
    provider_name = "ollama"

    def execute(self, prompt):

        return {
            "success": False,
            "provider": "ollama",
            "error": "Ollama connector not implemented.",
        }
