"""
Bellfre Example Agent Runner v0.3

Loads a Bellfre agent from its Bellfre Manifest.
"""

from bellfre.manifest import (
    load_manifest,
    validate_manifest,
)

from agent import Agent

from capabilities.calculator.calculator import CalculatorCapability
from capabilities.reasoning.reasoning import ReasoningCapability


# ------------------------------------------------------------------
# Load and validate the Bellfre Manifest
# ------------------------------------------------------------------

manifest = load_manifest("programs/calculator/bellfre.yaml")
validate_manifest(manifest)


# ------------------------------------------------------------------
# Create the agent using manifest metadata
# ------------------------------------------------------------------

agent = Agent(manifest["agent"]["name"])


# ------------------------------------------------------------------
# Register capabilities
#
# Future:
# Capabilities will be loaded dynamically from the manifest.
# ------------------------------------------------------------------

agent.add_capability(CalculatorCapability())
agent.add_capability(ReasoningCapability())


# ------------------------------------------------------------------
# Startup
# ------------------------------------------------------------------

print(f"{agent.name} v{manifest['agent']['version']} ready")
print(f"BUI: {manifest['agent']['bui']}")

print("\nCapabilities:")
for capability in agent.capabilities:
    print(f"- {capability.capability_id}")


# ------------------------------------------------------------------
# REPL
# ------------------------------------------------------------------

while True:
    user = input("> ")

    if user.lower() == "exit":
        break

    response = agent.think(user)

    print(response)