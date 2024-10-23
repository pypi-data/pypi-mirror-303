import io
import json
from fastapi import FastAPI, applications
from fastapi.responses import StreamingResponse
from contextlib import asynccontextmanager
import asyncio
from pg_objectserialization import loads, dumps
import uvicorn
from pg_common import log_info, log_error, start_coroutines, base64_decode, base64_encode
from pg_environment import config
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import get_swagger_ui_html
from .define import ENV_NEEDS_BODY_MIDDLEWARE, ENV_NEEDS_GZIP_BODY, ENV_GZIP_BODY_LENGTH, ENV_GZIP_COMPRESS_LEVEL
from pg_redis import GameConfigManager
CODE_VERSION = 0

__all__ = [
           "run", "app", "CODE_VERSION"
           ]
__auth__ = "baozilaji@gmail.com"


def swagger_ui_html_patch(*args, **kwargs):
    return get_swagger_ui_html(*args, **kwargs,
                               swagger_js_url="/static/swagger-ui/swagger-ui-bundle.js",
                               swagger_css_url="/static/swagger-ui/swagger-ui.css")

applications.get_swagger_ui_html = swagger_ui_html_patch

@asynccontextmanager
async def life_span(_app: FastAPI):
    from pg_httpserver import httpserver_init
    httpserver_init()
    start_coroutines(reload_config())
    log_info("http server startup")
    yield
    global _RUNNING
    _RUNNING = False
    log_info("http server shutdown")


app = FastAPI(docs_url=None if config.is_prod() else "/docs", lifespan=life_span)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if config.get_conf(ENV_NEEDS_GZIP_BODY, default=True):
    l = config.get_conf(ENV_GZIP_BODY_LENGTH, default=1000)
    c = config.get_conf(ENV_GZIP_COMPRESS_LEVEL, default=5)
    log_info(f"gzip config, size: {l}, level: {c}")
    app.add_middleware(GZipMiddleware, minimum_size=l, compresslevel=c)


_RUNNING = True


def reload_code_version():
    global CODE_VERSION
    if not CODE_VERSION:
        with open("VERSION") as _f:
            CODE_VERSION = int(_f.read())
            log_info(f"code version is: {CODE_VERSION}")


async def reload_config():
    while _RUNNING:
        try:
            reload_code_version()
            await GameConfigManager.reload()
        except Exception as e:
            log_error(e)
        await asyncio.sleep(60)
    log_info(f"server stopped")


@app.get("/health", description="健康检查接口", response_description="返回代码版本号")
async def health():
    return {
        "status": 0,
        "info": "OK",
        "code_version": CODE_VERSION
    }


class CustomBodyMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http" or scope["method"] != "POST":
            await self.app(scope, receive, send)
            return

        async def modify_req_body():
            message = await receive()
            _body: bytes = message.get("body", b"")
            _body = base64_decode(_body)
            _body = loads(_body)
            _body = json.dumps(_body)
            _body = _body.encode()
            message["body"] = _body
            return message
        await self.app(scope, modify_req_body, send)

if config.get_conf(ENV_NEEDS_BODY_MIDDLEWARE, default=True):
    log_info(f"add custom middleware to encrypt response and decrypt request")
    app.add_middleware(CustomBodyMiddleware)

    @app.middleware("http")
    async def http_inspector(request, call_next):
        if request.method == "POST":
            response = await call_next(request)
            response_body = b""
            async for chunk in response.body_iterator:
                response_body += chunk
            response_body = response_body.decode()
            response_body = base64_encode(dumps(response_body))
            _stream = io.BytesIO(response_body)
            return StreamingResponse(_stream, media_type="application/octet-stream")
        return await call_next(request)


def run(port=None):
    uvicorn.run(app="pg_httpserver.fapi:app", host=config.get_host(),
                port=config.get_port() if port is None else port)