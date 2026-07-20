
import pytest

from bellfre.identity import (
    validate_bui,
    AgentIdentity,
    BellfreBUI
)


def test_valid_bui():

    assert validate_bui(
        "1.0301.0304.00B42.0001"
    )


def test_valid_example_bui():

    assert validate_bui(
        "1.0000.0000.00000.0001"
    )


def test_invalid_old_format():

    assert not validate_bui(
        "1.301.0304.B42.001"
    )


def test_invalid_missing_segment():

    assert not validate_bui(
        "1.0301.0304.00B42"
    )


def test_old_bui_rejected_by_identity():

    manifest = {
        "agent": {
            "bui": "1.301.0304.B42.001",
            "name": "Old Agent",
        }
    }


    with pytest.raises(ValueError):
        AgentIdentity(manifest)

def test_parse_bui():

    bui = BellfreBUI(
        "1.0301.0304.00B42.0001"
    )

    assert bui.version == "1"
    assert bui.category == "0301"
    assert bui.locale == "0304"
    assert bui.authority == "00B42"
    assert bui.entity == "0001"


def test_bui_roundtrip():

    value = (
        "1.0301.0304.00B42.0001"
    )

    bui = BellfreBUI(value)

    assert str(bui) == value

