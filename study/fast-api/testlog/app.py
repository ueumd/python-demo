import sys

import uvicorn

from fastapi import FastAPI, Request
from loguru import logger
from starlette.routing import Match

logger.remove()
logger.add(sys.stdout, colorize=True, format="<green>{time:HH:mm:ss}</green> | {level} | <level>{message}</level>")
app = FastAPI()


@app.middleware("http")
async def log_middle(request: Request, call_next):
    logger.debug(f"{request.method} {request.url}")
    routes = request.app.router.routes
    logger.debug("Params:")
    for route in routes:
        match, scope = route.matches(request)
        if match == Match.FULL:
            for name, value in scope["path_params"].items():
                logger.debug(f"\t{name}: {value}")
    logger.debug("Headers:")
    for name, value in request.headers.items():
        logger.debug(f"\t{name}: {value}")

    response = await call_next(request)
    return response

@app.get("/")
def hello():
    return {"Hello": "World"}

@app.get("/json")
def hello():
    return {"Hello": "World"}


@app.get("/{param1}/{param2}")
async def path_operation(param1: str, param2: str):
    return {'param1': param1, 'param2': param2}


if __name__ == "__main__":
    uvicorn.run("app:app", host="localhost", port=8001)