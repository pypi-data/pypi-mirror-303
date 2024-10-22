import io
import json
from fastapi import FastAPI, applications
from fastapi.responses import StreamingResponse
from contextlib import asynccontextmanager
import asyncio
import uvicorn
from pg_common import log_info, log_error, start_coroutines, aes_decrypt, aes_encrypt
from pg_environment import config
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import get_swagger_ui_html
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

if config.is_prod():
    app.add_middleware(GZipMiddleware, minimum_size=1000, compresslevel=5)


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


@app.middleware("http")
async def http_inspector(request, call_next):
    if request.method == "POST":
        _body = await request.body()
        _body = _body.decode()
        _body = aes_decrypt(_body)
        request._body = _body
        response = await call_next(request)
        response_body = b""
        async for chunk in response.body_iterator:
            response_body += chunk
        _res = response_body.decode()
        _res = aes_encrypt(json.dumps(_res))
        _stream = io.BytesIO(_res.encode())
        return StreamingResponse(_stream, media_type="application/octet-stream")
    return await call_next(request)


def run():
    uvicorn.run(app="pg_httpserver.fapi:app", host=config.get_host(),
                port=config.get_port())