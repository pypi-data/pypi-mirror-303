import asyncio

from fastapi import FastAPI, Query, Request, applications
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from contextlib import asynccontextmanager
from pg_common import log_info, aes_decrypt, aes_encrypt, uid_encode, uid_decode, \
    Container, GameException, GameErrorCode, RequestHeader, RequestData, ResponseData, \
    ResponseHeader, get_file_abs_path
from pg_environment import config
import io
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import get_swagger_ui_html
import json

__all__ = [
           "run", "app"
           ]
__auth__ = "baozilaji@gmail.com"


def swagger_ui_html_patch(*args, **kwargs):
    return get_swagger_ui_html(*args, **kwargs,
                               swagger_js_url="/static/swagger-ui/swagger-ui-bundle.js",
                               swagger_css_url="/static/swagger-ui/swagger-ui.css")
applications.get_swagger_ui_html = swagger_ui_html_patch

@asynccontextmanager
async def life_span(app: FastAPI):
    from pg_httpserver import httpserver_init
    httpserver_init()
    log_info("http server startup")
    yield
    log_info("http server shutdown")


app = FastAPI(docs_url=None if config.is_prod() else "/docs", lifespan=life_span)
_static_path = get_file_abs_path(__file__)
log_info(_static_path)
app.mount("/static", StaticFiles(directory=f"{_static_path}"), name="static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health():
    return "OK"


@app.post("/game")
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
        from pg_httpserver import HandlerManager
        _method = _req.head.method
        _handler = HandlerManager.get_handler(_method)
        if not _handler:
            raise GameException(GameErrorCode.NO_MATCHED_METHOD_ERROR, "")
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


# @app.on_event("startup")
# async def startup():
#     from pg_httpserver import httpserver_init
#     httpserver_init()
#     log_info("http server startup")
#
#
# @app.on_event("shutdown")
# async def shutdown():
#     log_info("http server shutdown")


def run():
    uvicorn.run(app="pg_httpserver.fapi:app", host=config.get_host(),
                port=config.get_port())