"""
Bellfre Example Agent Runner v0.3

Loads a Bellfre agent from its Bellfre Manifest.
"""

from bellfre.discovery import Discovery
from bellfre.identity import AgentIdentity
from bellfre.manifest import (
    load_manifest,
    validate_manifest,
)
from bellfre.registry import AgentRegistry

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
# Bellfre Identity & Discovery
# ------------------------------------------------------------------

identity = AgentIdentity(manifest)

registry = AgentRegistry()

registry.register(identity)

discovery = Discovery(registry)

capability = manifest["capabilities"][0]["id"]

matches = discovery.find(capability)


# ------------------------------------------------------------------
# Startup
# ------------------------------------------------------------------

print("\nProgram:")
print("---------------------------------")
print(f"{agent.name}, Agent: v{manifest['agent']['version']}")

print("\nBellfre Unique Identifier (BUI):")
print("---------------------------------")
print(f"{manifest['agent']['bui']}")

print("\nDiscovery:")
print("---------------------------------")
for record in matches:
    print(
        f"✓ {record.identity.name}"
    )

print("\nCapabilities:")
print("---------------------------------")
for capability in agent.capabilities:
    print(f"- {capability.capability_id}")
print("\n")

# ------------------------------------------------------------------
# REPL
# ------------------------------------------------------------------

while True:

    user = input("> ")

    if user.lower() == "exit":
        break

    response = agent.think(user)

    print(response)