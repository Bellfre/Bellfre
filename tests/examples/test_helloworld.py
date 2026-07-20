from pathlib import Path
import sys


sys.path.insert(
    0,
    str(
        Path(__file__)
        .parents[2]
        / "examples"
        / "helloworld"
    ),
)


from capability import GreetingCapability  # noqa: E402


def test_hello_world_capability():

    capability = GreetingCapability()

    result = capability.execute(
        "hello"
    )

    assert result == (
        "Hello from Bellfre"
    )