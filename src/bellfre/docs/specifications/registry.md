# Bellfre Registry Specification

## Purpose

The Bellfre Registry stores canonical agent records and provides capability-based discovery.

The Registry is the authoritative source for registered Bellfre agents.

---

# Responsibilities

A registry SHALL:

* register agents
* validate agent identity
* store metadata
* support capability lookup
* expose discovery APIs

---

# Registration

Registration requires:

* valid AgentRecord
* valid BUI
* optional endpoint
* registration status

---

# Search

Discovery is capability driven.

Example:

```text
arithmetic.calculate
```

Returns:

* AgentRecord
* endpoint
* status

---

# Registry Record

A RegistryRecord wraps:

* AgentRecord
* endpoint
* status

The registry does not modify the underlying AgentRecord.

---

# Future Work

Future versions may support:

* distributed registries
* federation
* trust verification
* reputation
* digital signatures
