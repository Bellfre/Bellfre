# Bellfre Manifest Specification v0.1

## Overview

The Bellfre Manifest defines the identity, capabilities, runtime information, and execution metadata of a Bellfre-enabled agent.

The manifest is the primary description artifact used by Bellfre tooling to understand:

* What an agent is
* Who publishes it
* What capabilities it provides
* How it executes
* How it can be discovered and integrated

The manifest is designed to support future interoperability with agent protocols such as A2A without replacing those protocols.

---

# File Format

The default manifest filename is:

```
bellfre.yaml
```

The manifest uses YAML format for human readability and developer accessibility.

---

# Root Structure

A Bellfre Manifest contains:

```yaml
manifest:
agent:
runtime:
endpoint:
capabilities:
execution:
```

---

# Manifest

Defines the manifest specification version.

Example:

```yaml
manifest:
  version: "1.0"
```

Fields:

| Field   | Required | Description                            |
| ------- | -------- | -------------------------------------- |
| version | Yes      | Bellfre Manifest specification version |

---

# Agent Identity

Defines the identity and ownership information of the agent.

Example:

```yaml
agent:
  bui: "1.301.0304.B42.001"
  publisher_slug: "B42"

  publisher:
    name: "Bellfre"

  product: "Calculator"
  name: "Bellfre Calculator"
  version: "0.1.0"
```

Fields:

| Field          | Required | Description                     |
| -------------- | -------- | ------------------------------- |
| bui            | Yes      | Bellfre Unique Identifier       |
| publisher_slug | Yes      | Registered publisher reference  |
| publisher.name | Yes      | Human-readable publisher name   |
| product        | No       | Product or application grouping |
| name           | Yes      | Agent display name              |
| version        | Yes      | Agent version                   |

---

# Description

Provides human-readable information about the agent.

Example:

```yaml
description: >
  Performs mathematical calculations
  using deterministic capabilities.
```

---

# Runtime

Defines the execution environment.

Example:

```yaml
runtime:
  language: python
  protocol: a2a
```

Fields:

| Field    | Required | Description                      |
| -------- | -------- | -------------------------------- |
| language | Yes      | Primary implementation language  |
| protocol | No       | Supported communication protocol |

---

# Endpoint

Defines external access information.

Example:

```yaml
endpoint:
  url: "http://localhost:8000"
```

Fields:

| Field | Required | Description            |
| ----- | -------- | ---------------------- |
| url   | No       | Agent network endpoint |

Endpoint information may be added after initial registration.

---

# Capabilities

Defines what the agent can perform.

Example:

```yaml
capabilities:

  - id: arithmetic.calculate
    type: deterministic
    description: >
      Performs mathematical calculations.

    implementation:
      module: capabilities.calculator.calculator
```

Each capability contains:

| Field                 | Required | Description                       |
| --------------------- | -------- | --------------------------------- |
| id                    | Yes      | Unique capability identifier      |
| type                  | Yes      | Capability category               |
| description           | Yes      | Human-readable purpose            |
| implementation.module | No       | Internal implementation reference |

---

# Execution

Defines how the agent starts.

Example:

```yaml
execution:
  entrypoint: run.py
```

Fields:

| Field      | Required | Description               |
| ---------- | -------- | ------------------------- |
| entrypoint | Yes      | Application startup entry |

---

# Design Principles

## Identity First

Every Bellfre agent should have a persistent identity independent of location or runtime.

## Capability Based

Agents describe what they can do rather than exposing internal implementation details.

## Protocol Neutral

The manifest describes the agent. Communication protocols such as A2A provide interaction.

## Extensible

Future versions may add:

* verification
* ownership validation
* trust scoring
* discovery metadata
* security information

without breaking existing manifests.

---

# Version 0.1 Status

This specification defines the minimum viable Bellfre Manifest required for:

* agent identity
* capability discovery
* runtime description
* future registry integration
