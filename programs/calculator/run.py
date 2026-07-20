"""
Bellfre Example Agent Runner v0.4

Loads a Bellfre agent from its Bellfre Manifest
and demonstrates capability discovery.
"""

from bellfre.manifest import (
    load_manifest,
    validate_manifest,
)

from bellfre.capability import CapabilityRequest
from bellfre.discovery import Discovery
from bellfre.identity import AgentIdentity
from bellfre.registry import AgentRegistry

from agent import Agent

from capabilities.calculator.calculator import CalculatorCapability
from capabilities.reasoning.reasoning import ReasoningCapability

from bellfre.agent.description import AgentDescription
from bellfre.agent.record import AgentRecord


# ------------------------------------------------------------------
# Load and validate the Bellfre Manifest
# ------------------------------------------------------------------

manifest = load_manifest(
    "programs/calculator/bellfre.yaml"
)

validate_manifest(manifest)


# ------------------------------------------------------------------
# Create the agent using manifest metadata
# ------------------------------------------------------------------

agent = Agent(
    manifest["agent"]["name"]
)


# ------------------------------------------------------------------
# Register capabilities
#
# Future:
# Capabilities will be loaded dynamically from the manifest.
# ------------------------------------------------------------------

agent.add_capability(
    CalculatorCapability()
)

agent.add_capability(
    ReasoningCapability()
)


# ------------------------------------------------------------------
# Bellfre Discovery
# ------------------------------------------------------------------

identity = AgentIdentity(manifest)

description = AgentDescription.from_manifest(
    manifest
)

agent_record = AgentRecord(
    identity,
    description,
)

registry = AgentRegistry()

registry.register(agent_record)

discovery = Discovery(
    registry
)

request = CapabilityRequest(
    "arithmetic.calculate"
)

providers = discovery.find(
    request
)


# ------------------------------------------------------------------
# Startup
# ------------------------------------------------------------------

print(
    f"{agent.name} v{manifest['agent']['version']} ready"
)


print("\nBellfre Unique Identifier (BUI):")
print("---------------------------------")
print(
    manifest["agent"]["bui"]
)


# ------------------------------------------------------------------
# Discovery Output
# ------------------------------------------------------------------

print("\nDiscovery:")
print("---------------------------------")

print("Request:")
print(
    f"  {request.capability_id}"
)


print("\nResolved Provider:")

if providers:

    provider = providers[0]

    print(
        f"  {provider.name}"
    )

    print(
        f"  BUI: {provider.bui}"
    )

else:

    print("  None")


# ------------------------------------------------------------------
# Capabilities
# ------------------------------------------------------------------

print("\nCapabilities:")
print("---------------------------------")

for capability in agent.capabilities:

    print(
        f"- {capability.capability_id}"
    )


# ------------------------------------------------------------------
# REPL
# ------------------------------------------------------------------

while True:

    user = input("> ")

    if user.lower() == "exit":
        break

    response = agent.think(
        user
    )

    print(response)