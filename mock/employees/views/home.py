from responder import Request, Response
from mock.employees.initializer import mock_api


@mock_api.route("/")
async def index(_: Request, response: Response) -> None:
    response.content = mock_api.template("home/index.html")
