from pg_common import SingletonBase, log_info
import typing
from pg_environment import config
import importlib
import os


__all__ = [
                "HandlerManager"
           ]
__auth__ = "baozilaji@gmail.com"


class _HandlerManager(SingletonBase):
    def __init__(self):
        self._handlers: dict[str, typing.Callable] = {}

    def register(self, method: str, handler: typing.Callable):
        self._handlers[method] = handler
        log_info(f"register handler: {method}")

    def get_handler(self, method: str) -> typing.Callable:
        return self._handlers[method]

    @staticmethod
    def scan_handlers():
        from pg_httpserver import ENV_HANDLER_DIR
        _handler_dir = config.get_conf(ENV_HANDLER_DIR, "handlers")
        log_info(f"handler dirs: {_handler_dir}")

        for _root, _dirs, _files in os.walk(_handler_dir):
            for _file in _files:
                if _file.endswith(".py"):
                    _module_name = _root.replace("/", ".")
                    _module_name = f"{_module_name}.{_file[:-3]}"
                    _module = importlib.import_module(_module_name)
                    log_info(f"load handler {_module_name}")


HandlerManager = _HandlerManager()