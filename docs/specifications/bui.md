# Bellfre Unique Identifier (BUI) Specification

## Overview

The Bellfre Unique Identifier (BUI) provides a stable identity namespace for Bellfre-enabled agents.

A BUI identifies an agent instance while allowing future expansion for:
- categories
- locales
- publishers
- organizations
- deployment authorities

BUI is an identity primitive.

It does not define:
- discovery
- networking
- endpoints
- transports
- protocols

Those functions belong to registry and adapter layers.

---

# BUI Format (v1)

The default Bellfre BUI format is:


N.AAAA.AAAA.AAAAA.NNNN


Example:


1.0301.0304.00B42.0001


---

# Segment Definitions

| Segment | Format | Purpose | Example |
|---|---|---|---|
| Version | N | BUI namespace/version | `1` |
| Category | AAAA | Agent category or classification | `0301` |
| Locale | AAAA | Regional/language classification | `0304` |
| Authority | AAAAA | Publisher or organizational namespace | `00B42` |
| Instance | NNNN | Specific agent identity | `0001` |

---

# Examples

## Bellfre Example Namespace

Example agents use the reserved default namespace:


1.0000.0000.00000.0001


Meaning:


1 BUI version
0000 Example category
0000 Example locale
00000 Example authority
0001 First example agent


---

## Bellfre Calculator

The calculator example uses the Bellfre publisher namespace:


1.0301.0304.00B42.0001


Meaning:


1 BUI version
0301 Arithmetic agent category
0304 Locale allocation
00B42 Bellfre publisher authority
0001 Calculator agent instance


---

# Fixed Width Rules

BUI v1 uses fixed-width segments.

This provides:

- deterministic parsing
- database indexing
- registry interoperability
- future namespace expansion

Rules:


Version:
1 character numeric

Category:
4 characters alphanumeric

Locale:
4 characters alphanumeric

Authority:
5 characters alphanumeric

Instance:
4 characters numeric


---

# Validation

A valid BUI MUST match:


N.AAAA.AAAA.AAAAA.NNNN


Example valid:


1.0301.0304.00B42.0001


Invalid examples:


1.301.0304.B42.001


Reason:
- incorrect segment widths
- legacy format


1.0301.0304.00B42


Reason:
- missing instance segment

---

# Manifest Requirement

A Bellfre manifest MUST contain:

```yaml
agent:
  name:
  bui:
  version:

The bui field:

is REQUIRED
MUST follow the Bellfre BUI specification
MUST be validated when creating an AgentIdentity

Example:

agent:
  name: Bellfre Calculator
  bui: 1.0301.0304.00B42.0001
  version: 0.1.0
Architectural Ownership

BUI ownership:

Manifest
   |
   v
AgentIdentity
   |
   +-- BUI validation
   |
   v
AgentRecord
   |
   v
Registry / Discovery / Export

The following components MUST NOT interpret BUI structure:

Registry
Discovery
Well-known endpoints
Protocol adapters

They treat BUI as an opaque identity value.

Future registry services may index or query BUI segments, but parsing rules remain owned by the Identity layer.

Versioning

Changes to BUI structure require a new BUI version.

Example:

1.xxxx.xxxx.xxxxx.xxxx

is BUI v1.

Future incompatible formats must use:

2.xxxx.xxxx.xxxxx.xxxx
BUI v1 is the current Bellfre identity standard.