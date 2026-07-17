# Bellfre A2A Adapter Mapping

## Purpose

This document defines how Bellfre concepts are translated into A2A Agent Card structures.

The A2A adapter provides interoperability. It does not redefine Bellfre identity, capability, or manifest standards.

---

## Identity Mapping

| Bellfre Concept          | A2A Field               |
| ------------------------ | ----------------------- |
| Agent name               | `AgentCard.name`        |
| Agent description        | `AgentCard.description` |
| Agent version            | `AgentCard.version`     |
| Agent ownership/provider | `AgentCard.provider`    |

---

## Capability Mapping

| Bellfre Concept         | A2A Field                 |
| ----------------------- | ------------------------- |
| Capability identifier   | `AgentSkill.id`           |
| Capability name         | `AgentSkill.name`         |
| Capability description  | `AgentSkill.description`  |
| Capability examples     | `AgentSkill.examples`     |
| Capability input modes  | `AgentSkill.input_modes`  |
| Capability output modes | `AgentSkill.output_modes` |

---

## Runtime Mapping

| Bellfre Concept     | A2A Field                         |
| ------------------- | --------------------------------- |
| Runtime endpoint    | `AgentInterface.url`              |
| Supported transport | `AgentInterface.protocol_binding` |
| Protocol version    | `AgentInterface.protocol_version` |

Runtime information is deployment-specific and should not be embedded into Bellfre identity specifications.

---

## Design Rule

Bellfre defines:

* Who the agent is
* What the agent can do
* How capabilities are named

A2A defines:

* How agents communicate
* How tasks are exchanged
* How external clients interact

The adapter connects these models without making either dependent on the other.
