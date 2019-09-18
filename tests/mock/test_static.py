import pytest
from mock.employees.static import Endpoint


@pytest.fixture(scope="module")
def endpoint() -> Endpoint:
    return Endpoint()


def test_address(endpoint: Endpoint) -> None:
    assert endpoint.address == "0.0.0.0"


def test_port(endpoint: Endpoint) -> None:
    assert endpoint.port == 7777


def test_debug(endpoint: Endpoint) -> None:
    assert not endpoint.debug
