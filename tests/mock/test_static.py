import pytest
from mock.employees.static import Endpoint, Route


@pytest.fixture(scope="module")
def endpoint() -> Endpoint:
    return Endpoint()


@pytest.fixture(scope="module")
def route() -> Route:
    return Route()


def test_address(endpoint: Endpoint) -> None:
    assert endpoint.address == "0.0.0.0"


def test_port(endpoint: Endpoint) -> None:
    assert endpoint.port == 7777


def test_debug(endpoint: Endpoint) -> None:
    assert not endpoint.debug


def test_route_home(route: Route) -> None:
    assert route.home == "/"
