"""
HelloWorld Capability

Provides a simple greeting capability.
"""


class GreetingCapability:
    """
    Basic greeting capability.
    """

    capability_id = "greeting.say"

    def execute(self, message: str):
        return (
            "Hello from Bellfre"
        )