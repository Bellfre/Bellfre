# Bellfre

## The Identity and Discovery Layer for AI Agents

[![CI](https://github.com/Bellfre/Bellfre/actions/workflows/ci.yml/badge.svg)](https://github.com/Bellfre/Bellfre/actions)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Version](https://img.shields.io/github/v/tag/Bellfre/Bellfre)](https://github.com/Bellfre/Bellfre/tags)

---

## What is Bellfre?

Bellfre is an open specification and reference implementation for **AI agent identity, capability discovery, and interoperability metadata**.
As AI systems evolve into networks of specialized agents, a fundamental problem emerges:

**How does one agent discover, identify, and understand another agent before interaction begins?**

Bellfre provides the discovery and identity layer that exists before agent communication.

# A simple analogy:

A2A is the telephone system.

Bellfre is the phone book,
identity verification,
and directory service.


Bellfre helps answer:

> Who are you?  
> What can you do?  
> How can I find you?  
> Can I trust this identity?

---

# Core Concepts

## Bellfre Manifest

The Bellfre Manifest is a machine-readable description of an agent.

A manifest defines:

- Agent identity
- Publisher information
- Capabilities
- Runtime information
- Connection metadata
- Execution information

Example:

```yaml
manifest:
  version: "1.0"

agent:
  bui: "1.301.0304.B42.001"
  name: "Bellfre Calculator"
  version: "0.1.0"

runtime:
  language: python

capabilities:
  - id: arithmetic.calculate
    type: deterministic

```
## The manifest is the foundation for Bellfre discovery and registration.

Bellfre Unique Identifier (BUI)

Every Bellfre-enabled agent can have a persistent identity.

The BUI identifies an agent independently of:

Hosting location
Runtime implementation
Communication protocol
Deployment environment

Identity belongs to the agent, not the endpoint.

Capability-Based Discovery

Bellfre focuses on discovering what agents can do.

Agents advertise capabilities rather than exposing internal implementation details.

## Examples:

    finance.analyze
    documents.summarize
    calendar.schedule
    mathematics.calculate

Applications and agents can discover the appropriate capability provider without needing to understand how it is implemented.

Relationship to Agent Standards

Bellfre complements existing and emerging agent communication standards:

Agent-to-Agent (A2A)
Model Context Protocol (MCP)
Future interoperability standards

Communication protocols define:

How agents interact

Bellfre defines:

How agents are found, identified, and understood

## Architecture:

                 Application
                      |
                      v

              Bellfre Discovery Layer
                      |
        +-------------+-------------+
        |             |             |
        v             v             v

      Agent A       Agent B       Agent C

        A2A           MCP       Custom API

Bellfre does not replace agent runtimes or communication protocols.

It provides the identity and discovery foundation that allows those systems to scale.

And, Bellfre is being developed as a layered platform:

    Bellfre
    |
    ├── Manifest
    │   └── Agent identity and metadata specification
    |
    ├── Identity
    │   └── BUI and publisher registration
    |
    ├── Discovery
    │   └── Registry and lookup services
    |
    ├── SDK
    │   └── Developer tools for Bellfre agents
    |
    └── Programs
        └── Reference agent implementations

##  Current Implementation

The current reference implementation includes:

    Python SDK foundation
    Bellfre Manifest loading
    Manifest validation
    Capability-based agent structure
    Example calculator agent

Current development focuses on:

    Manifest specification stabilization
    Registry architecture
    Agent publishing workflows
    A2A interoperability
    Development Setup

Bellfre uses uv for Python package and dependency management.

# Requirements
    Python 3.10+
    uv

# Install dependencies:

    uv sync

Run the calculator program:

    uv run python programs/calculator/run.py

## Project Status

Bellfre is currently in active prototype development.

# Completed
    Capability-based agent architecture
    Reasoning policy architecture
    Provider abstraction
    Bellfre Manifest v1 foundation
    Python package structure
    Manifest loading and validation
    Current Work
    Manifest schema definitions
    Agent registry design
    Publishing workflow
    A2A interoperability layer
    Why Bellfre?

# The future of AI is likely to be a network of specialized agents:

    Financial analysis agents
    Scheduling agents
    Research agents
    Business workflow agents
    Personal assistants
    Domain-specific services

# For this ecosystem to work, agents need a common way to announce:

    This is who I am.
    This is what I can do.
    This is how you can discover me.

Bellfre provides the identity and discovery foundation for interoperable AI agents.

## Contributing

Bellfre is an open-source project exploring the infrastructure required for interoperable AI agent ecosystems.
Contributions, design feedback, and implementation ideas are welcome as the specification evolves.
