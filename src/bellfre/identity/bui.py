"""
Bellfre Unique Identifier (BUI)

Validation for BUI v1 format:

N.AAAA.AAAA.AAAAA.NNNN
"""


import re


BUI_PATTERN = re.compile(
    r"^\d\.[A-Za-z0-9]{4}\.[A-Za-z0-9]{4}\.[A-Za-z0-9]{5}\.\d{4}$"
)


def validate_bui(
    bui: str,
) -> bool:
    """
    Validate a Bellfre Unique Identifier.

    Format:
        N.AAAA.AAAA.AAAAA.NNNN

    Example:
        1.0301.0304.00B42.0001
    """

    return bool(
        BUI_PATTERN.match(
            bui
        )
    )