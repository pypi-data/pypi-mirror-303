import io
import json
from fastapi import FastAPI, applications, Request
from fastapi.responses import StreamingResponse
from contextlib import asynccontextmanager
import asyncio
import uvicorn
from pg_common import log_info, log_error, start_coroutines, aes_decrypt, ResponseData, ResponseHeader, Container, \
    RequestData, GameException, GameErrorCode, aes_encrypt
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


@app.post("/game", description="游戏逻辑处理(m1,m2处理方案)", deprecated=True)
async def handle(*,
                 req: Request):
    _res = ResponseData(head=ResponseHeader(), body=dict())
    _c = Container(rep=_res)
    try:
        _req: RequestData = None
        try:
            _r = await req.body()
            _r = _r.decode()
            _r = aes_decrypt(_r)
            _req = RequestData.parse_raw(_r)
            _c.req = _req
        except Exception as e:
            raise GameException(GameErrorCode.RECEIVE_INPUT_ERROR, "")
        _c.log.update({
            'req': _req
        })
        from pg_common import FuncDecoratorManager
        _method = _req.head.method
        _handler = FuncDecoratorManager.get_func(_method)
        if not _handler:
            raise GameException(GameErrorCode.NO_MATCHED_METHOD_ERROR, "")
        await _handler(_req)
    except GameException as e:
        _c.log['g_exception'] = str(e)
        _res.head.retCode = e.state
    except Exception as e:
        _c.log['exception'] = str(e)
        _res.head.retCode = GameErrorCode.OTHER_EXCEPTION
    finally:
        _c.log.update({
            'res': _res
        })
        log_info(_c.log)
    _res = _res.json()
    _res = aes_encrypt(json.dumps(_res))
    _stream = io.BytesIO(_res.encode())
    return StreamingResponse(_stream, media_type="application/octet-stream")


@app.middleware("http")
async def http_inspector(request, call_next):
    response = await call_next(request)
    return response


def run():
    uvicorn.run(app="pg_httpserver.fapi:app", host=config.get_host(),
                port=config.get_port())