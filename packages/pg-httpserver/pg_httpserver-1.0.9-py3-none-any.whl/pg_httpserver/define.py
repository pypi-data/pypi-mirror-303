from pg_resourceloader import LoaderManager
from pg_common import FuncDecoratorManager
from pg_environment import config


__all__ = [
                "ENV_HANDLER_DIR", "httpserver_init"
           ]
__auth__ = "baozilaji@gmail.com"


ENV_HANDLER_DIR = "handler_dir"


def httpserver_init():
    FuncDecoratorManager.scan_decorators(config.get_conf(ENV_HANDLER_DIR, "handlers"))
    LoaderManager.scan_loaders()
