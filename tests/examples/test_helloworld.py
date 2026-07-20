from pathlib import Path
import sys


EXAMPLE_PATH = (
    Path(__file__)
    .parents[2]
    / "examples"
    / "helloworld"
)

sys.path.insert(
    0,
    str(EXAMPLE_PATH)
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