from typing import List
from responder import Request, Response
from mock.employees import mock_api
from mock.employees.data.database import Employees, Employee
from mock.employees.static import Route
from mock.logging import Logger

_logger: Logger = Logger(__name__)
_route: Route = Route()


@mock_api.route(route=_route.search_by_keyword)
async def search_employees_by_keyword(_: Request, response: Response, keyword: str) -> None:
    employees = Employees(limit=10)
    hits: List[Employee] = employees.search_by_keyword(keyword)
    response.media = {
        "keyword": keyword,
        "truncated_results": employees.truncated,
        "hits": len(hits),
        "results": employees.to_dict(hits),
    }


@mock_api.route(route=_route.search_by_id)
async def search_employee_by_id(_: Request, response: Response, identifier: str) -> None:
    employees = Employees(limit=10)
    response.media = {
        "employee_id": identifier,
        "truncated_results": employees.truncated,
        "hits": 1,
        "results": employees.search_by_id(int(identifier)).to_dict(),
    }
