import sys

import uvicorn

from fastapi import FastAPI, Request, APIRouter, Depends
from loguru import logger
import os

logger.remove()

app = FastAPI()

router = APIRouter()

async def logging_dependency(request: Request):
    logger.info(f"{request.method} {request.url}")
    logger.info("Params:")
    for name, value in request.path_params.items():
        logger.info(f"\t{name}: {value}")
    logger.info("Headers:")
    for name, value in request.headers.items():
        logger.info(f"\t{name}: {value}")

@router.get("/")
def hello():
    return {"Hello": "World"}

@router.get("/json")
def hello():
    return {"Hello": "World"}

@router.post("/jsontest")
def hello():
    return {"Hello": "World"}

@router.get("/{param1}/{param2}")
async def path_operation(param1: str, param2: str):
    return {'param1': param1, 'param2': param2}



if __name__ == "__main__":
    # 日志设置
    dir_log = "logs"
    path_log = os.path.join(dir_log, './日志文件.log')
    #logger.add(path_log, colorize=True, format="<green>{time:HH:mm:ss}</green> | {level} | <level>{message}</level>")
    logger.add(path_log, rotation='0:00', enqueue=True, serialize=False, encoding="utf-8", retention="10 days")
    #logger.debug("服务器重启！")

    app.include_router(router, dependencies=[Depends(logging_dependency)])

    uvicorn.run("app:app", host="localhost", port=8001)