from dataclasses import dataclass


@dataclass(frozen=True)
class Endpoint:
    """The class represents WEB endpoint for API."""

    address: str = "0.0.0.0"
    port: int = 7777
    debug: bool = False
