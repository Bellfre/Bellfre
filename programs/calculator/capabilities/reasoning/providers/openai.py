"""
Bellfre OpenAI Provider

Reasoning Provider Implementation
"""

from openai import OpenAI
from .provider import ReasoningProvider

import config


class OpenAIProvider(ReasoningProvider):
    provider_name = "openai"

    def __init__(self):

        self.client = OpenAI(api_key=config.OPENAI_API_KEY)

    def execute(self, prompt):

        request = prompt

        try:
            prompt = request["input"]

            response = self.client.responses.create(
                model=config.OPENAI_MODEL, input=prompt
            )

            return {
                "success": True,
                "provider": self.provider_name,
                "model": config.OPENAI_MODEL,
                "input": prompt,
                "response": response.output_text,
            }

        except Exception as e:
            return {"success": False, "provider": self.provider_name, "error": str(e)}


if __name__ == "__main__":
    print("Bellfre OpenAI Provider ready")
    print("Type 'exit' or 'quit' to stop")

    provider = OpenAIProvider()

    while True:
        prompt = input("> ")

        if prompt.lower() in ["exit", "quit"]:
            break

        result = provider.execute({"input": prompt})

        print(result)
