"""
Bellfre Manifest Validator

Validates a Bellfre Manifest against
the required manifest schema.
"""

from .schema import REQUIRED_FIELDS


class ManifestValidationError(Exception):
    """
    Raised when a Bellfre Manifest fails validation.
    """
    pass


def validate_manifest(manifest: dict) -> bool:
    """
    Validate a Bellfre Manifest.

    Args:
        manifest:
            Parsed manifest dictionary

    Returns:
        True if valid

    Raises:
        ManifestValidationError:
            If required fields are missing
    """

    for field in REQUIRED_FIELDS:
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