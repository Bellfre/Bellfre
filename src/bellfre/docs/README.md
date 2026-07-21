# Bellfre SDK

> **The Identity and Discovery Layer for AI Agents**

Bellfre is a lightweight SDK that provides a common identity, discovery, and metadata model for AI agents. It defines how agents identify themselves, describe their capabilities, register with discovery services, and expose standardized metadata.

The Bellfre SDK is intentionally small. Its purpose is to establish stable contracts that can be used by registries, marketplaces, orchestration systems, and agent frameworks.

---

# Philosophy

Bellfre focuses on **identity before execution**.

The SDK does **not** replace an AI framework, LLM provider, workflow engine, or protocol.

Instead, Bellfre standardizes:

* Agent identity
* Agent metadata
* Capability description
* Discovery
* Registration
* Well-Known documents
* JSON export

This allows independent systems to discover and trust agents using a common model.

---

# Design Goals

* Small, composable SDK
* Stable public API
* Provider agnostic
* Protocol agnostic
* Human-readable manifests
* Machine-readable metadata
* Minimal dependencies
* Easy to embed into existing projects

---

# Package Structure

```text
bellfre/
├── agent/
├── capability/
├── discovery/
├── export/
├── identity/
├── manifest/
├── registry/
└── wellknown/
```

Each package has a single responsibility and exposes a small public interface.

---

# Public SDK API

## Identity

Responsible for permanent agent identity.

```python
from bellfre.identity import AgentIdentity
from bellfre.identity import BellfreBUI
from bellfre.identity import validate_bui
```

Provides:

* BUI parsing
* BUI validation
* Agent identity model

---

## Manifest

Loads Bellfre manifests.

```python
from bellfre.manifest import load_manifest
```

Responsibilities:

* YAML loading
* Validation
* Schema mapping

---

## Agent

Defines the core agent models.

```python
from bellfre.agent import AgentDescription
from bellfre.agent import AgentRecord
```

Responsibilities:

* Agent metadata
* Capability description
* Canonical agent record

---

## Registry

Stores and searches agent records.

```python
from bellfre.registry import AgentRegistry
```

Responsibilities:

* Registration
* Lookup
* Capability search

---

## Discovery

Queries registries.

```python
from bellfre.discovery import Discovery
```

Responsibilities:

* Capability discovery
* Provider selection

---

## Capability

Defines discovery requests.

```python
from bellfre.capability import CapabilityRequest
```

---

## Well-Known

Generates the portable Bellfre agent document.

```python
from bellfre.wellknown import create_agent_document
```

This document is intended for publication through:

```text
/.well-known/bellfre-agent.json
```

---

## Export

Exports Bellfre models.

```python
from bellfre.export import export_agent_json
```

---

# Bellfre Manifest

Every Bellfre-enabled agent starts with a manifest.

Example:

```yaml
agent:
  name: Bellfre Calculator
  bui: 1.0301.0304.00B42.0001
  version: 1.0.0

capabilities:
  - id: arithmetic.calculate
```

The manifest is the source of truth for an agent's identity and capabilities.

---

# Bellfre Unique Identifier (BUI)

Every Bellfre agent has a globally unique identity.

Current grammar:

```text
N.AAAA.AAAA.AAAAA.NNNN
```

Example:

```text
1.0301.0304.00B42.0001
```

For complete details see:

```text
docs/specifications/bui.md
```

---

# Typical Workflow

```text
Manifest
    │
    ▼
load_manifest()
    │
    ▼
AgentIdentity
    │
    ▼
AgentDescription
    │
    ▼
AgentRecord
    │
    ├──────────────► JSON Export
    │
    ├──────────────► Well-Known Document
    │
    └──────────────► Registry
                         │
                         ▼
                    Discovery
```

---

# Examples

Reference implementations are included with the SDK.

## HelloWorld

Demonstrates:

* Manifest loading
* Agent identity
* Agent description
* JSON export
* Capability execution

## Calculator

Demonstrates:

* Registry
* Discovery
* Capability lookup
* Reasoning provider integration

---

# Stability

Bellfre follows semantic versioning.

Current release target:

```text
1.0.0 Release Candidate
```

The following contracts are intended to remain stable across the 1.x series:

* BUI format
* Manifest schema
* AgentIdentity
* AgentDescription
* AgentRecord
* AgentRegistry
* Discovery
* Well-Known document
* Public package imports

---

# Documentation

Additional documentation is available in the SDK documentation folder.

## Specifications

* `docs/specifications/bui.md`

Future specifications will include:

* Manifest Specification
* Registry Specification
* Discovery Specification
* Capability Specification
* Well-Known Specification

---

# Roadmap

The SDK provides the foundation for the Bellfre ecosystem.

The primary product built on top of this SDK is the **Bellfre Registry**, which will provide:

* Agent registration
* Identity verification
* Capability indexing
* Discovery APIs
* Trust services
* Marketplace integration

The SDK establishes the contracts. The Registry builds the network.

---

# Contributing

Before submitting changes:

* Run all unit tests.
* Run static analysis (`pyright`).
* Run linting (`ruff`).
* Keep public APIs backward compatible.
* Update documentation when contracts change.

Bellfre values clarity, stability, and simplicity over unnecessary abstraction.

## Specifications

The Bellfre SDK specifications define the stable contracts used throughout the SDK.

| Specification | Purpose                           |
|---------------|-----------------------------------|
| BUI           | Bellfre Unique Identifier format  |
| Manifest      | Agent manifest schema             |
| Registry      | Agent registration model          |
| Discovery     | Capability discovery workflow     |
| Well-Known    | Portable agent document           |