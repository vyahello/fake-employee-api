from mock.employees import mock_api
from mock.employees.static import Endpoint


def main() -> None:
    """Runs an application."""
    endpoint: Endpoint = Endpoint()
    mock_api.run(address=endpoint.address, port=endpoint.port, debug=endpoint.debug)


if __name__ == "__main__":
    main()
