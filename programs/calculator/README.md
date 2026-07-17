# Bellfre Calculator Agent Example

## Overview

This repository contains a reference Bellfre-compatible calculator agent.
The purpose of this example is to demonstrate the Bellfre agent workflow:

    * capability registration
    * capability discovery
    * reasoning delegation
    * policy evaluation
    * controlled capability execution
    * structured responses

The calculator is intentionally simple and deterministic. It exists as a clear reference implementation showing how a Bellfre agent is structured and how the execution pipeline works.

Bellfre is not an AI model provider and does not create or host agents. Bellfre provides the infrastructure layer that allows agents to describe capabilities, apply policies, and participate in a discoverable agent ecosystem.

---

# Bellfre Architecture

A Bellfre-compatible agent separates reasoning, policy, and execution.

    User Input
        |
        v
    Agent Runtime
        |
        v
    Reasoning Layer
        |
        +----------------+
        |                |
        v                |
    Policy Layer <-------+
        |
        v
    Capability Execution
        |
        v
    Response

The calculator example demonstrates this workflow without requiring an external AI model.

---

# What This Example Demonstrates

## Capability Layer

The calculator exposes capabilities that can be discovered and executed.

Example capabilities:
    arithmetic.calculate
    mathematics.explain

Capabilities are responsible for performing actions.

They do not decide:

    * whether an action should happen
    * whether a request is allowed
    * what tools are available

Those decisions belong to other layers.

---

## Reasoning Layer

The reasoning layer determines the intended action.
In a production agent, this layer may connect to:

    * OpenAI
    * Anthropic
    * local models
    * enterprise-hosted models
    * other reasoning systems

Bellfre does not require or provide a specific model provider.
The reasoning layer communicates intent to the Bellfre runtime.

---

## Policy Layer

The policy layer evaluates whether an action is allowed.

Examples:
    * capability restrictions
    * enterprise rules
    * security controls
    * trust requirements
    * agent permissions

The policy layer is intentionally separate from reasoning.

Reasoning answers:

> "What should happen?"

Policy answers:

> "Is this allowed to happen?"

---

# Requirements

## Basic Calculator Example

The calculator example can run without external API credentials.
Requirements:

* Python 3.x
* project dependencies installed


    pip install -r requirements.txt


---

## AI Model Examples

Examples that use external AI reasoning require your own model provider account and API credentials.
Bellfre does not provide:

    * shared API keys
    * free model access
    * hosted inference
    * proxy access to AI providers

Developers connect their own preferred model provider.

Example:

    Developer
        |
        +-- Own API credentials
        |
        v
    Bellfre Agent
        |
        v
    Capabilities


This keeps Bellfre model-neutral and allows agents to use:

    * commercial APIs
    * private enterprise models
    * local models
    * future providers

---

# Running the Example

Start the calculator:

```
python run.py
```

Example:


Bellfre Calculator ready

Capabilities:
    - arithmetic.calculate
    - mathematics.explain

> 6*9


Example response:
    {
        "success": true,
        "capability": "arithmetic.calculate",
        "operation": "multiply",
        "input": {
            "expression": "6*9"
        },
        "result": 54
    }


---

# Standalone Test Mode

This example includes a standalone test path.
The purpose of the standalone test is to validate the Bellfre execution pipeline without requiring an external AI provider.

The test demonstrates:

    Input
    |
    v
    Reasoning Interface
    |
    v
    Policy Evaluation
    |
    v
    Capability Selection
    |
    v
    Capability Execution
    |
    v
    Structured Response


The standalone test is not intended to replace a production reasoning model.

It exists to prove that the Bellfre workflow functions independently from any specific AI provider.

---

# Project Structure

    bellfre-examples/
    |
    └── calc/
        |
        ├── README.md
        ├── run.py
        ├── requirements.txt
        |
        ├── agent/
        |   ├── reasoning.py
        |   ├── policy.py
        |   └── runtime.py
        |
        └── capabilities/
            ├── arithmetic.py
            └── mathematics.py


---

# Design Principles

## Bellfre Does Not Build Agents

Developers build agents.

Bellfre provides the standards and infrastructure that allow agents to become:

    * describable
    * discoverable
    * governable
    * interoperable

---

## Bellfre Does Not Process LLMs

Bellfre does not replace reasoning engines.

Instead, Bellfre provides the adapter layer around agents.

An agent may use any compatible reasoning system while maintaining the same Bellfre execution workflow.

---

## Bring Your Own Intelligence

The developer chooses:

    * model provider
    * model architecture
    * hosting environment
    * enterprise requirements

Bellfre remains provider-neutral.

---

# Future Examples

Additional examples may demonstrate:

    * LLM-powered agents
    * enterprise policy enforcement
    * agent discovery
    * BAT (Bellfre Agent Tag) metadata
    * capability publishing
    * network participation

The calculator remains the baseline example because it demonstrates the Bellfre contract without introducing unnecessary complexity.

---

# Purpose of This Repository

This repository exists to help developers understand how to build Bellfre-compatible agents.
The calculator example proves the foundation:
    Agent
    |
    +-- Reasoning
    |
    +-- Policy
    |
    +-- Capabilities
    |
    +-- Execution

Future Bellfre agents build on this same structure while adding more advanced reasoning, capabilities, and discovery features.
