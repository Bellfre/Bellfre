"""
Bellfre Unique Identifier (BUI)

Format:

N.AAAA.AAAA.AAAAA.NNNN

Example:

1.0301.0304.00B42.0001
"""


import re


BUI_PATTERN = re.compile(
    r"^(\d)\.([A-Za-z0-9]{4})\.([A-Za-z0-9]{4})\.([A-Za-z0-9]{5})\.(\d{4})$"
)


class BellfreBUI:
    """
    Parsed Bellfre Unique Identifier.
    """

    def __init__(
        self,
        value: str,
    ):

        match = BUI_PATTERN.match(
            value
        )

        if not match:
            raise ValueError(
                f"Invalid BUI format: {value}"
            )

        (
            self.version,
            self.category,
            self.locale,
            self.authority,
            self.entity,
        ) = match.groups()


    @property
    def value(self) -> str:
        return (
            f"{self.version}."
            f"{self.category}."
            f"{self.locale}."
            f"{self.authority}."
            f"{self.entity}"
        )


    def to_dict(self) -> dict:

        return {
            "version": self.version,
            "category": self.category,
            "locale": self.locale,
            "authority": self.authority,
            "entity": self.entity,
        }


    def __str__(self):

        return self.value



def validate_bui(
    value: str,
) -> bool:

    try:
        BellfreBUI(value)
        return True

    except ValueError:
        return False