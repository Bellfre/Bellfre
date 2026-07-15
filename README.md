# Bellfre

**Bellfre** is an experimental open-source project exploring a simple question:

**How do AI agents discover, identify, and connect with each other?**

As AI systems evolve beyond chat interfaces into autonomous software, services, and business workflows, a new challenge emerges: agents need a reliable way to advertise what they are, what they can do, and how other systems can interact with them.

Bellfre explores the discovery layer for agent interoperability.

## What Bellfre Is

Bellfre is an open specification and reference implementation for **Agent Discovery Metadata**.

The project introduces **Bellfre Agent Tags (BAT)** — lightweight, machine-readable metadata attached to an agent that describes:

    * Agent identity
    * Capabilities and supported tasks
    * Available protocols
    * Authentication requirements
    * Connection endpoints
    * Service metadata
    * Compatibility information

The goal is simple:

**Help people, software, and AI agents discover the right agent for the right task.**

Bellfre does not create AI agents, train models, or replace agent runtimes. Instead, it provides the infrastructure layer that allows existing agents and services to become discoverable.

## Relationship to Emerging Agent Standards

Bellfre is designed to complement emerging agent communication standards such as:

    * Agent-to-Agent (A2A) protocols
    * Model Context Protocol (MCP)
    * Future agent interoperability standards

Where communication protocols define **how agents interact**, Bellfre focuses on **how agents are found, identified, and understood before interaction begins**.

A simplified view:

```
    User / Application
            |
            v
    Bellfre Discovery Layer
            |
            +---- Agent A (A2A endpoint)
            |
            +---- Agent B (MCP service)
            |
            +---- Agent C (custom protocol)
```

Bellfre aims to provide the metadata and discovery foundation that allows different agent ecosystems to connect.

## Project Architecture

Bellfre is being developed as a layered system:

```
    Bellfre
    |
    ├── Foundation
    │   └── Agent specifications and schemas
    |
    ├── Services
    │   └── Discovery and registry components
    |
    ├── SDK
    │   └── Tools for developers building compatible agents
    |
    └── Examples
        └── Reference implementations
```

The current prototype includes a Python reference implementation demonstrating capability registration, reasoning policies, and provider routing.

## Development Setup

Bellfre uses **uv** for Python environment and dependency management.

### Requirements

    * Python 3.10+
    * uv

    Install uv:

    ```bash
    pip install uv
    ```

    Clone the repository:

    ```bash
    git clone <repository-url>
    cd bellfre
    ```

    Create the development environment:

    ```bash
    uv sync
    ```

    Run the example:

    ```bash
    uv run python examples/calc/run.py
    ```

    The example demonstrates Bellfre capability routing:

    ```
    User Input
        |
        v
    Capability Selection
        |
        v
    Policy Evaluation
        |
        v
    Provider Execution
    ```

## Current Status

Bellfre is currently in the research and prototype stage.

Current development goals:

    * Define the Bellfre Agent Tag specification
    * Establish interoperable discovery metadata
    * Build reference implementations
    * Explore alignment with A2A, MCP, and future agent protocols
    * Create developer tools for publishing and discovering agents

## Why Bellfre?

The future of AI is unlikely to be a single intelligent system. It will be a network of specialized agents:

    * A financial agent analyzing transactions
    * A scheduling agent managing calendars
    * A customer service agent handling requests
    * A business workflow agent coordinating tasks

For that ecosystem to work, agents need a common way to announce:

> "This is who I am. This is what I can do. This is how you can connect with me."

Bellfre is an exploration of that missing discovery layer.

## Contributing

Bellfre is an open-source project. Contributions, ideas, specifications, and implementation feedback are welcome as the project evolves.

The project is intentionally being developed through open experimentation and incremental standards development.


# Bellfre

The Identity and Discovery Layer for AI Agents

[![CI](https://github.com/Bellfre/Bellfre/actions/workflows/ci.yml/badge.svg)](https://github.com/YOUR_ORG/Bellfre/actions)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Version](https://img.shields.io/github/v/tag/YOUR_ORG/Bellfre)](https://github.com/YOUR_ORG/Bellfre/tags)