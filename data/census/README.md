# Bellfre Agent Census (BAC)

The **Bellfre Agent Census (BAC)** is a curated research catalog of publicly known AI agents, organizations, and communication protocols.

The census is **not** the Bellfre Registry and does not assign Bellfre Unique Identifiers (BUIs). Its purpose is to understand the emerging AI agent ecosystem, identify common metadata, validate Bellfre Agent Tag (BAT) requirements, and provide the foundation for future registry development.

## Objectives

* Catalog publicly available AI agents.
* Record organizations developing or maintaining agents.
* Track communication protocols and standards.
* Study ecosystem trends before designing the production registry.
* Seed the future Bellfre Registry with known public agents.

## Repository Structure

```text
data/
└── census/
    ├── README.md
    ├── agents.csv
    ├── organizations.csv
    └── protocols.csv
```

## Data Files

### agents.csv

Contains one record for each known AI agent.

Typical information includes:

* Agent name
* Organization
* Framework
* Communication protocol
* Current status
* Agent Card URL (when available)
* Source repository
* Discovery source
* Research notes

### organizations.csv

Catalog of organizations responsible for developing or maintaining AI agents.

Examples include:

* Open source projects
* Commercial organizations
* Research institutions
* Community projects

### protocols.csv

Catalog of communication protocols used by AI agents.

Examples include:

* A2A
* MCP
* HTTP APIs
* Future protocol standards

## Agent Status

The following status values are currently defined:

| Status     | Description                                                  |
| ---------- | ------------------------------------------------------------ |
| CATALOGED  | Agent has been identified but not validated.                 |
| REGISTERED | Reserved for future Bellfre Registry integration.            |
| VERIFIED   | Agent has been successfully validated by Bellfre.            |
| OFFLINE    | Agent was previously reachable but is currently unavailable. |
| UNKNOWN    | Current state has not yet been determined.                   |

## Current Scope

During Milestone 8.5, the census serves as a research dataset only.

It does **not**:

* Assign BUIs
* Generate BAT records
* Verify ownership
* Perform cryptographic validation
* Act as a production registry

Those capabilities are planned for future Bellfre milestones.

## Long-Term Vision

The Bellfre Agent Census represents the first stage of the Bellfre ecosystem.

```text
Discover Agent
       │
       ▼
Bellfre Agent Census (BAC)
       │
       ▼
Assign Bellfre Unique Identifier (BUI)
       │
       ▼
Generate Bellfre Agent Tag (BAT)
       │
       ▼
Publish to Bellfre Registry
```

As Bellfre evolves, information collected in the census will inform the design of the Bellfre Registry while remaining a valuable historical and research resource.
