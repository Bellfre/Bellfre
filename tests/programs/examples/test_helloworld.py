import sys
from pathlib import Path

sys.path.append(
    str(
        Path(__file__)
        .parent.parent.parent.parent
        / "examples"
        / "helloworld"
    )
)

from capability import GreetingCapability


def test_hello_world_capability():

    capability = GreetingCapability()

    result = capability.execute(
        "hello"
    )

    assert result == (
        "Hello from Bellfre"
    )