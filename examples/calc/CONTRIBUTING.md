# Contributing to Bellfre Examples

Thank you for your interest in contributing to Bellfre examples.

The purpose of this repository is to provide clear, working reference implementations of Bellfre-compatible agents. Contributions should help developers understand how Bellfre agents are structured, how capabilities are exposed, and how the execution workflow operates.

---

# Before Contributing

Please understand the role of this repository.
Bellfre examples are intended to demonstrate:

    * agent structure
    * capability design
    * policy integration
    * reasoning workflows
    * interoperability patterns

This repository is not intended to become a collection of unrelated applications.
Examples should demonstrate Bellfre concepts clearly and remain easy for new developers to understand.

---

# Types of Contributions

## New Examples

New examples are welcome when they demonstrate a useful Bellfre pattern.

Examples may include:

    * new agent types
    * new capability implementations
    * policy examples
    * integrations with external services
    * enterprise use cases
    * discovery and metadata examples

A new example should include:

    * clear purpose
    * README documentation
    * installation instructions
    * usage examples
    * explanation of the Bellfre concepts demonstrated

---

## Improvements to Existing Examples

Improvements are encouraged, including:

    * bug fixes
    * documentation improvements
    * clearer examples
    * improved test coverage
    * simplified workflows
    * better error handling

When modifying an existing example, maintain its original purpose and avoid unnecessary complexity.

---

# Code Guidelines

## Keep Examples Simple

Examples should prioritize understanding over optimization.

Prefer:

    * readable code
    * clear naming
    * explicit workflows
    * small focused components

Avoid:

    * unnecessary abstractions
    * complex frameworks
    * hidden behavior
    * provider-specific assumptions

---

## Maintain Bellfre Separation

Examples should preserve the separation between:

### Reasoning

Determines intent.

Examples:

    * interpreting user requests
    * selecting actions
    * planning workflows

### Policy

Determines permission.

Examples:

    * allowing or denying actions
    * enforcing restrictions
    * applying rules

### Capability

Performs the requested operation.

Examples:

    * calculations
    * data retrieval
    * external actions

Do not combine these layers unless the example specifically demonstrates why.

---

# External Services and API Keys

Examples requiring external services must not include:

    * API keys
    * credentials
    * secrets
    * personal configuration files

Contributors should use environment variables or documented configuration methods.

Example:

```text
    MODEL_API_KEY=your_key_here
```

Bellfre examples should demonstrate how developers connect their own services.
Bellfre does not provide shared API access or hosted model usage.

---

# Documentation Requirements

Every example should include a README explaining:

    * what the example demonstrates
    * required dependencies
    * how to run it
    * expected output
    * Bellfre concepts involved

Documentation should assume the reader is discovering Bellfre for the first time.

---

# Testing

Before submitting changes:

    1. Run the example locally
    2. Confirm installation instructions work
    3. Verify expected output
    4. Ensure tests pass if included

A contributor should be able to clone the repository and reproduce the documented workflow.

---

# Pull Requests

Pull requests should include:

    * description of the change
    * reason for the change
    * affected example(s)
    * testing performed

For larger additions, explain:

    * what Bellfre concept is demonstrated
    * why this example belongs in the repository
    * how it improves developer understanding

---

# Design Philosophy

Bellfre examples should communicate a simple idea:

Agents provide intelligence.

Capabilities provide action.

Policies provide control.

Bellfre provides the infrastructure that connects them.

Contributions should help make that model clearer for developers building the next generation of agent systems.
