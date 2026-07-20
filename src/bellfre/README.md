# Bellfre Python SDK

The Bellfre Python SDK provides the core runtime components for building
Bellfre-enabled agents.

The SDK allows agents to establish identity, describe capabilities,
register with discovery systems, and participate in the Bellfre ecosystem.

---

# Purpose

A Bellfre-enabled agent uses the SDK to answer four fundamental questions:

1. **Who am I?**
2. **What capabilities do I provide?**
3. **How can I be discovered?**
4. **How can another agent understand my capabilities?**

The SDK provides the building blocks required to answer these questions.

---

# Architecture

The core Bellfre SDK flow:


    Bellfre Manifest
    |
    v
    AgentIdentity
    |
    v
    AgentRegistry
    |
    v
    CapabilityRequest
    |
    v
    Discovery
    |
    v
    CapabilityProvider


An agent declares its identity and capabilities through a Bellfre Manifest.
The SDK converts that information into standardized objects that can be
registered and discovered.

---

# Package Structure


bellfre/

    ├── capability/
    │ Capability requests and capability providers.
    │
    ├── identity/
    │ Agent identity representation.
    │
    ├── manifest/
    │ Manifest loading, mapping, and validation.
    │
    ├── registry/
    │ Agent registration and capability lookup.
    │
    └── discovery/
Capability discovery and provider resolution.


---

# Core Components

## Manifest

The manifest defines the agent's declared identity and capabilities.

Example:

```yaml
agent:
  bui: 1.0301.0304.00B42.001
  name: Bellfre Calculator

capabilities:
  - id: arithmetic.calculate

The SDK loads and validates this information before creating runtime objects.

AgentIdentity

AgentIdentity represents the permanent identity of a Bellfre agent.

It contains:

Bellfre Unique Identifier (BUI)
Agent name
Version information
Publisher information
Declared capabilities

Example:

identity = AgentIdentity(manifest)
AgentRegistry

AgentRegistry stores and indexes known agents.

Example:

registry = AgentRegistry()

registry.register(identity)

The registry provides the source for discovery operations.

CapabilityRequest

CapabilityRequest describes what capability an agent is looking for.

Example:

request = CapabilityRequest(
    "arithmetic.calculate"
)
Discovery

Discovery resolves capability requests into available providers.

Example:

providers = discovery.find(request)
CapabilityProvider

CapabilityProvider represents an agent capable of providing a requested capability.

Example:

provider.name
provider.bui
provider.capability_id
Example Application

The reference implementation is:

programs/calculator

The calculator demonstrates:

Loading a Bellfre Manifest
Creating an agent identity
Registering capabilities
Performing local discovery
Resolving capability providers

Run:

uv run python programs/calculator/run.py
Current Scope

The SDK currently provides local capability discovery.

Current flow:

    Agent
    |
    v
    Local Registry
    |
    v
    Discovery
    |
    v
    Capability Provider

Future versions will extend this model to support:

Remote registries
HTTP discovery endpoints
External agent communication
Protocol integrations

The core SDK model remains the foundation for those capabilities.

Design Principle

The Bellfre SDK separates:

Identity

Who an agent is.

Capability

What an agent can do.

Discovery

How capabilities are found.

Execution

How capabilities are performed.

Keeping these concerns separate allows Bellfre agents to evolve without
coupling identity, discovery, and execution into a single system.

Related Documentation
Root project documentation: README.md
Foundation principles: foundation/README.md
Reference agent: programs/calculator