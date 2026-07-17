"""
Bellfre Manifest Validator

Validates the minimum required fields
for a Bellfre Manifest v1.0.
"""


class ManifestValidationError(Exception):
    """Raised when a manifest fails validation."""
    pass


def validate_manifest(manifest: dict) -> bool:
    """
    Validate a Bellfre manifest.

    Returns:
        True if valid

    Raises:
        ManifestValidationError if invalid
    """

    required_fields = [
        ("manifest", "version"),
        ("agent", "bui"),
        ("agent", "name"),
        ("agent", "version"),
        ("runtime", "language"),
        ("capabilities",),
        ("execution", "entrypoint"),
    ]

    for field in required_fields:
        if not _has_field(manifest, field):
            path = ".".join(field)
            raise ManifestValidationError(
                f"Missing required field: {path}"
            )

    return True


def _has_field(data: dict, path: tuple) -> bool:
    """
    Check whether a nested field exists.
    """

    current = data

    for key in path:
        if not isinstance(current, dict):
            return False

        if key not in current:
            return False

        current = current[key]

    return True