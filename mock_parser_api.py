"""Module contains API to work with `mock-parser-api` app."""
from abc import ABC, abstractmethod
from mock.employees import mock_api
from mock.employees.static import Endpoint


class Service(ABC):
    """The class represents abstract interface for service."""

    @abstractmethod
    def start(self) -> None:
        """Starts abstract service."""
        pass


class MockParser(Service):
    """The class represents mock parser service."""

    def __init__(self, endpoint: Endpoint) -> None:
        self._endpoint = endpoint

    def start(self) -> None:
        """Starts mock parser service."""
        mock_api.run(address=self._endpoint.address, port=self._endpoint.port, debug=self._endpoint.debug)


def main() -> None:
    """Runs an application."""
    mock_parser: Service = MockParser(Endpoint())
    mock_parser.start()


if __name__ == "__main__":
    main()
