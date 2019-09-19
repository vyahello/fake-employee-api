import logging
import functools
from typing import Any, Callable, Union


class LoggerError(Exception):
    """The class represents a logger error."""

    pass


class Logger:
    """The class represents main console logger."""

    NONSET: int = logging.NOTSET
    INFO: int = logging.INFO
    ERROR: int = logging.ERROR
    WARNING: int = logging.WARNING
    DEBUG: int = logging.DEBUG

    def __init__(self, name: str) -> None:  # noqa: D202
        @functools.lru_cache()
        def client() -> logging.Logger:
            logger: logging.Logger = logging.getLogger(name)
            handler: logging.Handler = logging.StreamHandler()
            handler.setFormatter(
                logging.Formatter(fmt="[%(asctime)s %(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
            )
            logger.addHandler(handler)
            logger.setLevel(logging.INFO)
            return logger

        self._logger: Callable[[], logging.Logger] = client

    def info(self, message: str, *args: Any, **kwargs: Any) -> None:
        self._logger().info(message, *args, **kwargs)

    def debug(self, message: str, *args: Any, **kwargs: Any) -> None:
        self._logger().debug(message, *args, **kwargs)

    def warning(self, message: str, *args: Any, **kwargs: Any) -> None:
        self._logger().warning(message, *args, **kwargs)

    def error(self, message: str, *args: Any, **kwargs: Any) -> None:
        self._logger().error(message, *args, **kwargs)

    def level(self) -> int:
        return self._logger().level

    def set_level(self, level: Union[str, int]) -> None:
        if isinstance(level, (int, str)):
            self._logger().setLevel(level)
        else:
            raise LoggerError('Logger level must be an "int" or an "str"!')
