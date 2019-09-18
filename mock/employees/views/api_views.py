from responder import Request, Response
from mock.employees import mock_api
from mock.employees.static import Route
from mock.logging import Logger

_logger: Logger = Logger(__name__)
_route: Route = Route()


@mock_api.route(route=_route.search_by_keyword)
async def search_employees_by_keyword(_: Request, response: Response, keyword: str) -> None:
    response.media = {"keyword": "empty"}


@mock_api.route(route=_route.search_by_id)
async def search_employee_by_id(_: Request, response: Response, id: str) -> None:
    response.media = {"id": "empty"}
