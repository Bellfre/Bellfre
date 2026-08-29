# Bellfre Manifest Specification

## Purpose

The Bellfre Manifest is the canonical description of an agent. It defines the agent's identity, capabilities, version, and metadata in a machine-readable format.

Every Bellfre-enabled agent **MUST** provide a valid manifest.

---

# Required Structure

```yaml
agent:
  name: Bellfre Calculator
  bui: 1.0301.0304.00B42.0001
  version: 1.0.0

capabilities:
  - id: arithmetic.calculate
```

---

# Agent Section

| Field       | Required | Description                |
| ----------- | -------- | -------------------------- |
| name        | MUST     | Human-readable agent name  |
| bui         | MUST     | Bellfre Unique Identifier  |
| version     | MUST     | Agent version              |
| publisher   | MAY      | Publisher metadata         |
| description | MAY      | Human-readable description |

---

# Capabilities

Each capability **MUST** define:

* id

Future revisions may include:

* title
* description
* input schema
* output schema
* tags

---

# Validation Rules

A valid manifest MUST:

* contain an `agent` section
* contain a valid BUI
* define an agent name
* define an agent version
* contain a capabilities list

---

# Related Specifications

* BUI Specification
* Registry Specification
* Discovery Specification
