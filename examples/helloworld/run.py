"""
Bellfre HelloWorld Example

Demonstrates:
- Loading a Bellfre manifest
- Creating an AgentDescription
- Exporting agent metadata
"""

from pathlib import Path

from bellfre.manifest import load_manifest
from bellfre.agent.description import AgentDescription


MANIFEST = (
    Path(__file__).parent
    / "bellfre.yaml"
)


def main():

    manifest = load_manifest(
        MANIFEST
    )

    description = (
        AgentDescription
        .from_manifest(manifest)
    )

    print(
        description.to_json()
    )


if __name__ == "__main__":
    main()