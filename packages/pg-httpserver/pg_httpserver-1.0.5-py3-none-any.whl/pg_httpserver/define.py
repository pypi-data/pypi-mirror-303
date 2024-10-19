import typing
from pg_httpserver import HandlerManager
from pg_resourceloader import LoaderManager


__all__ = [
                "handler", "ENV_HANDLER_DIR", "httpserver_init"
           ]
__auth__ = "baozilaji@gmail.com"


ENV_HANDLER_DIR = "handler_dir"


def handler(method_name: str) -> typing.Callable:
    def decorator(func: typing.Callable) -> typing.Callable:
        HandlerManager.register(method_name, func)
    return decorator


def httpserver_init():
    HandlerManager.scan_handlers()
    LoaderManager.scan_loaders()
