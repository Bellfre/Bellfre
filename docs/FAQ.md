# Bellfre Architecture FAQ

**Document Status:** Early Draft / Architectural Guidepost

## Purpose

This document establishes the initial concepts, terminology, and architectural direction for the Bellfre platform.

The goal of this FAQ is not to define final implementation details. Instead, it provides a common language and a set of guideposts for future development.

Detailed technical specifications, schemas, APIs, and implementation rules will be developed separately as the architecture matures.

> **Business Rule: Fluid Taxonomy**
> Bellfre terminology and naming conventions are considered provisional during this early phase. Names may be refined, replaced, or reorganized as the platform evolves and implementation experience provides additional insight.

---

# What is Bellfre?

Bellfre is an agent-focused framework designed to create reusable, modular, and extensible AI capabilities.

The core idea is that intelligent agents should not be isolated applications. Instead, they should be built from standardized components that can be combined, reused, and expanded.

The initial architectural model:

```
Agent
 |
 +-- Identity
 |
 +-- Instructions
 |
 +-- Memory
 |
 +-- Tools
 |
 +-- Events
```

---

# What is a Bellfre Agent?

An agent is an intelligent entity that can reason, make decisions, maintain context, and interact with available capabilities.

An agent is defined by:

* Who it is
* What it is intended to do
* What capabilities it has access to
* What rules govern its behavior

The initial working term for the agent definition is:

**Bellfre Agent Manifest (BAM)**

The BAM concept represents the identity and configuration of an agent.

---

# What are Bellfre Tools?

Tools are capabilities that an agent can use to perform actions.

Examples:

* Calculations
* Reading files
* Accessing databases
* Calling external services
* Processing information

The goal is for agents to use capabilities through a common interface rather than custom integrations.

The initial working term for this concept is:

**Bellfre Tool Contract (BTC)**

A tool contract describes what a capability does, what it requires, and what it returns.

---

# Why are standardized tools important?

Without standards, every agent becomes a custom system.

A standardized tool model allows:

* Tools to be reused
* Agents to discover capabilities
* Developers to build compatible extensions
* New capabilities to be added without redesigning the agent

The long-term vision is:

```
Agent
 |
 +-- Tool A
 +-- Tool B
 +-- Tool C
```

where each tool follows the same general expectations.

---

# What is Agent Memory?

Memory allows an agent to maintain information over time.

Potential memory capabilities include:

* Conversation context
* Learned information
* User preferences
* Task history
* Agent state

The initial working term is:

**Bellfre Memory Contract (BMC)**

The exact implementation of memory remains open and will be defined later.

---

# What are Agent Events?

Events represent communication between agents, tools, and services.

Events allow the system to respond to changes such as:

* A task beginning
* A tool completing
* Information changing
* An agent state updating

The initial working term is:

**Bellfre Event Contract (BEC)**

---

# What is the Bellfre Agent Framework?

The Bellfre Agent Framework (BAF) represents the overall ecosystem of agent components.

Initial architecture concept:

```
Bellfre Agent Framework

    Agent Manifest
          |
    Tool Contracts
          |
    Memory Contracts
          |
    Event Contracts
          |
    Runtime Services
          |
    SDK Components
```

The framework name represents the complete system, not a single software component.

---

# Where do examples fit?

Early implementations should begin as examples.

Examples allow concepts to be tested without prematurely committing production architecture.

Example:

```
examples/

    simple-agent/

        tools/
            calculator.py
            file_reader.py
            weather.py
```

Examples serve as:

* Reference implementations
* Learning resources
* Architecture experiments
* Validation of concepts

Successful patterns can later move into SDK or service layers.

---

# What is the development philosophy?

Bellfre follows a progression:

```
Concept
   |
Example
   |
Specification
   |
SDK Component
   |
Production Service
```

This allows ideas to be tested before becoming permanent architecture.

---

# Current Bellfre Business Rules

## BR-001: Define Concepts Before Implementing Services

Major architectural concepts should be documented before production implementation.

## BR-002: Examples Validate Ideas

New concepts should first be demonstrated through examples.

## BR-003: Contracts Enable Interoperability

Agents and capabilities should interact through defined contracts.

## BR-004: Components Should Be Modular

Agents, tools, memory, and services should remain independent where practical.

## BR-005: Naming Is Evolutionary

Current Bellfre terminology establishes a working vocabulary and may change as the platform develops.

## BR-006: Bellfre Compatibility

Bellfre should support existing and emerging interoperability standards rather than compete with them.

Bellfre defines agent structure, lifecycle, and governance while allowing external protocols to handle communication and resource exchange.

## BR-007: Single Agent Model

Personal, business, and enterprise agents use the same underlying Bellfre architecture.

Differences between deployments are defined through profiles, permissions, resources, and governance—not separate agent standards.


## BR-NET-001: Discovery is decentralized by design.

Intent: Bellfre should be architected so that agent discovery can operate across multiple independently operated discovery nodes. No single discovery node should be required for the Bellfre ecosystem to function.

That doesn't commit you to blockchain, DHTs, or any specific protocol. It simply states the architectural goal: the ecosystem should not depend on a single central registry.

That gives you room to prototype with a simple centralized registry initially, then evolve toward a federated or peer-to-peer discovery network as the project matures. I think that's the safer path because it lets you validate the agent model before taking on the much harder problem of distributed systems.

## BR-LLM-001: Bellfre is model-agnostic.

Bellfre defines the architecture, lifecycle, discovery, and interoperability of agents. Reasoning is supplied through interchangeable LLM providers. No Bellfre component should require a specific language model or vendor API to function.

I think this is one of the most important architectural decisions we've made. It keeps Bellfre from becoming "another Claude framework" or "another OpenAI framework" and instead positions it as the portable operating architecture that can outlive any single model provider.

## BR-COST-001: Use deterministic computation whenever possible. 

Invoke an LLM only when reasoning, interpretation, or generation is required.

## *INTERNAL USE ONLY* Business Rule: Database Foreign Keys (v0.x)

Purpose

During Bellfre Foundation development, the database schema is expected to evolve rapidly. To minimize development friction, foreign key constraints will be used only when they are required for the correct operation of the application.

Policy

All tables shall define an appropriate Primary Key.
Foreign Key constraints are optional during the Foundation (v0.x) phase.
Foreign Keys should only be implemented when they are required for application correctness or data integrity that cannot reasonably be enforced elsewhere.
Application code is responsible for validating references between records during registration, updates, and deletes.
Orphan detection and cleanup utilities will be part of the Registry and maintenance tooling.
Referential integrity, cascading updates, and cascading deletes will be reviewed during the Database Hardening milestone prior to a production (v1.x) release.

Rationale

This approach:

Reduces schema migration complexity.
Allows rapid iteration on the Bellfre Foundation.
Avoids unnecessary MySQL constraint issues during active design.
Keeps validation logic centralized within the Registry where richer business rules can be enforced.

I would add one engineering guideline alongside it:

Rule: Even without foreign keys, continue to use consistent column names and data types for future compatibility.

For example:

publisher_id BIGINT UNSIGNED NOT NULL
product_id BIGINT UNSIGNED NOT NULL
agent_id BIGINT UNSIGNED NOT NULL
domain_id BIGINT UNSIGNED NOT NULL
subcategory_id BIGINT UNSIGNED NOT NULL

That way, when you decide to add foreign keys later, the tables are already compatible and the "Database Hardening" milestone becomes mostly a matter of adding constraints rather than redesigning columns.

I think this fits Bellfre's philosophy well: keep the foundation simple, keep the interfaces stable, and postpone infrastructure hardening until the architecture has settled.

