# Bellfre A2A Protocol Adapter

## Purpose

The Bellfre A2A adapter provides interoperability between Bellfre agents and the Agent2Agent (A2A) protocol ecosystem.

This adapter allows Bellfre agents to participate in A2A-based communication while maintaining Bellfre as the source of truth for agent identity, capabilities, and discovery metadata.

The goal is not to replace A2A.

The goal is to allow Bellfre agents to speak A2A.

---

## Architecture

Bellfre separates internal standards from external protocol integrations.

```text
Bellfre Foundation
        |
        |
        v
 Agent Identity
 Manifest
 Capabilities
 Discovery
        |
        |
        v
 A2A Adapter
        |
        |
        v
 A2A Protocol
        |
        |
        v
 External Agents
```

The adapter acts as a translation layer between Bellfre-native models and A2A-compatible representations.

---

## Responsibilities

The A2A adapter is responsible for:

* Converting Bellfre agent metadata into A2A-compatible structures
* Exposing Bellfre capabilities through A2A concepts
* Supporting A2A agent discovery workflows
* Maintaining protocol compatibility as A2A evolves

---

## Non-Responsibilities

The A2A adapter does not define:

* Bellfre agent identity
* Bellfre manifests
* Bellfre capability standards
* Bellfre discovery rules
* Bellfre governance

Those belong to:

```text
foundation/
```

The adapter only provides interoperability.

---

## Relationship to Bellfre Protocols

Bellfre-owned standards live under:

```text
foundation/protocols/
```

Examples:

```text
proto-identity.py
proto-manifest.py
proto-capabilities.py
```

External protocol integrations live under:

```text
adapters/protocols/
```

Examples:

```text
adapters/protocols/
├── a2a/
└── mcp/
```

---

## Current Goal

The first implementation milestone is:

```
Bellfre Manifest
        |
        v
A2A Agent Card
```

A Bellfre agent should be able to:

1. Load its Bellfre manifest.
2. Convert that identity into an A2A representation.
3. Be discovered and communicated with by A2A-compatible agents.

---

## Design Principle

Bellfre follows:

> Define identity once. Adapt everywhere.

Bellfre provides the identity and discovery foundation.

Protocols such as A2A provide communication mechanisms.

Adapters connect the two.

---

## Status

🚧 Early development

The A2A adapter is being developed as the first external protocol integration for Bellfre.

Future protocol adapters may include:

* MCP
* Additional agent communication protocols
* Registry integrations
* Marketplace integrations
