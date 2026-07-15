"""
Bellfre Example Agent Runner v0.2

Loads a Bellfre agent with multiple capabilities.

Future:
    Capabilities will be discovered and loaded
    from capability.json files.
"""

from agent import Agent

from capabilities.calculator.calculator import CalculatorCapability
from capabilities.reasoning.reasoning import ReasoningCapability


agent = Agent("Bellfre Calculator")


agent.add_capability(CalculatorCapability())


agent.add_capability(ReasoningCapability())


print(f"{agent.name} ready")

print("Capabilities:")
for capability in agent.capabilities:
    print(f"- {capability.capability_id}")


while True:
    user = input("> ")

    if user.lower() == "exit":
        break

    response = agent.think(user)

    print(response)
