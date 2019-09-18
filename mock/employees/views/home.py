from responder import Request, Response
from mock.employees import mock_api
from mock.employees.static import Route

_route: Route = Route()


@mock_api.route(route=_route.home)
async def index(_: Request, response: Response) -> None:
    response.content = mock_api.template("home/index.html")
