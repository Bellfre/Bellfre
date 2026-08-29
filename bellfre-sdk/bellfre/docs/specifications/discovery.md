# Bellfre Discovery Specification

## Purpose

Discovery locates Bellfre agents capable of performing a requested capability.

Discovery is intentionally capability-based rather than implementation-based.

---

# Workflow

```text
Capability Request
        │
        ▼
Registry Search
        │
        ▼
Matching Agent Records
```

---

# Capability Request

Minimum fields:

* capability id

Example:

```text
arithmetic.calculate
```

---

# Discovery Result

A discovery result returns one or more RegistryRecords.

The SDK does not prescribe ranking or routing policies.

---

# Design Principles

Discovery SHALL:

* remain provider agnostic
* remain protocol agnostic
* return AgentRecords
* avoid transport concerns

Transport is outside the scope of this specification.
