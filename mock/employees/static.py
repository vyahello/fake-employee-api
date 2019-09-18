from dataclasses import dataclass


@dataclass(frozen=True)
class Endpoint:
    """The class represents WEB endpoint for API."""

    address: str = "0.0.0.0"
    port: int = 7777
    debug: bool = False


@dataclass(frozen=True)
class Route:
    """The class represents API routes."""

    home: str = "/"
    search_by_keyword: str = "/api/search/{keyword}"
    search_by_id: str = "/api/employee/{id}"
