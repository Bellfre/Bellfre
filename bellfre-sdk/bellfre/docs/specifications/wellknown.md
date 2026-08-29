# Bellfre Well-Known Specification

## Purpose

Bellfre agents expose a portable metadata document suitable for publication through:

```text
/.well-known/bellfre-agent.json
```

This document allows registries, discovery services, and external systems to inspect an agent without executing it.

---

# Required Fields

| Field        | Description                      |
| ------------ | -------------------------------- |
| bui          | Bellfre Unique Identifier        |
| name         | Agent name                       |
| version      | Agent version                    |
| capabilities | Supported capability identifiers |

---

# Example

```json
{
  "bui": "1.0301.0304.00B42.0001",
  "name": "Bellfre Calculator",
  "version": "1.0.0",
  "capabilities": [
    "arithmetic.calculate"
  ]
}
```

---

# Generation

The SDK provides:

```python
create_agent_document(record)
```

which generates the canonical document from an AgentRecord.

---

# Transport

The SDK generates the document only.

Hosting, HTTP routing, caching, authentication, and networking are outside the scope of this specification.
