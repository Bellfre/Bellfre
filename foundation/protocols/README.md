# Bellfre Foundation Protocols

## Purpose

The `foundation/protocols` directory contains the protocol definitions that form the core standards of the Bellfre ecosystem.

These are Bellfre-owned specifications that define how agents identify themselves, describe capabilities, publish manifests, and participate in the Bellfre network.

Files prefixed with `proto-` are architectural markers indicating that the item represents a Bellfre standard.

Example:

```
proto-identity.py
proto-manifest.py
proto-capabilities.py
```

These files are design anchors and should be reviewed before implementation changes are made elsewhere in the SDK.

---

## Foundation vs Adapters

Bellfre distinguishes between protocols it defines and protocols it integrates with.

### Bellfre Protocols

Location:

```
foundation/protocols/
```

These define:

* Agent identity
* Capability naming
* Manifest structure
* Discovery records
* Registry interactions
* Governance rules

Bellfre owns the specification.

---

### External Protocol Adapters

Location:

```
adapters/protocols/
```

These provide compatibility with external ecosystems.

Examples:

```
adapters/protocols/
├── a2a/
└── mcp/
```

External protocols define communication methods or interoperability standards.

Bellfre does not replace these protocols. Bellfre provides identity, discovery, and translation layers that allow Bellfre agents to participate in them.

---

## Current Protocol Specifications

### Identity Protocol

File:

```
proto-identity.py
```

Defines:

* Agent identity model
* Unique identifiers
* Ownership metadata
* Verification concepts
* Naming conventions

Future work may include the Bellfre Agent Identifier and Bellfre Naming Authority concepts.

---

### Manifest Protocol

File:

```
proto-manifest.py
```

Defines:

* Agent manifest structure
* Required metadata
* Capability declarations
* Versioning
* Discovery information

The manifest is the source representation of a Bellfre agent.

---

### Capability Protocol

File:

```
proto-capabilities.py
```

Defines:

* Capability naming conventions
* Capability identifiers
* Capability metadata
* Versioning rules

Capabilities allow agents to advertise what they can do in a consistent manner.

---

## Design Philosophy

Bellfre follows the principle:

```
Define once.
Adapt everywhere.
```

Bellfre standards provide a common identity and discovery layer.

Adapters allow Bellfre agents to communicate with external protocols and platforms.

Example:

```
Bellfre Manifest
        |
        |
        v
Bellfre Protocol Definition
        |
        |
        v
A2A Adapter
        |
        |
        v
A2A Agent Card
```

The Bellfre model remains stable while integrations evolve.

---

## Future Protocol Areas

Potential future protocol specifications:

```
proto-registry.py
proto-discovery.py
proto-trust.py
proto-governance.py
proto-namespace.py
```

These should only be created when the underlying standard is mature enough to require a formal definition.

---

## Status

This directory represents the evolving standards layer of Bellfre.

Current files are placeholders for specification development and architectural alignment.

Implementation should follow the protocol definitions, not define them accidentally.
