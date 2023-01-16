from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI, File, UploadFile, Response
from fastapi.responses import StreamingResponse
import base64

import uvicorn

from PIL import Image, ImageFilter

from io import BytesIO
from loguru import logger

import os

from typing import Optional

"""
https://cloud.tencent.com/developer/article/1883204?from=15425
"""

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def hello():
    return {"Hello": "World"}

@app.get("/json")
def hello():
    return {"Hello": "World"}


class Userinfo(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(userinfo: Userinfo):
    return {
        "username": userinfo.username,
        "password": userinfo.password
    }

@app.get("/login")
def login(username: str, password: str):
    return {
        "username": username,
        "password": password
    }


@app.get("/items/{item_id}")
def getItem(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


"""
可选参数
http://127.0.0.1:8080/items/110?q=hello


http://127.0.0.1:8080/items/110
{
    item_id: 110,
    q: null
}
"""

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

@app.put("/items/{item_id}")
def getItem(item_id: int, item: Item):
    return {"name": item.name, "id": item_id, "price": item.price}


@app.post("/files/")
def create(file: bytes = File(...)):
    return {"file_size": len(file)}


# file 参数类型是 UploadFile
@app.post("/uploadfile/")
def upload(file: UploadFile = File(...)):
    img_bytes = file.file.read()

    with open("/upload/test.jpg", 'wb') as f:
        f.write(img_bytes)

    img = Image.open("./upload/test.jpg")
    img.show()
    return {"filename": file.filename}

    return {"filename": file.filename}


# file 参数类型是 UploadFile
@app.post("/upload/")
async def upload_img(file: UploadFile = File(...)):
    result = {
        "filename": file.filename,
        "content-type": file.content_type,
        "read": await file.read()
    }

    return result


@app.get("/test")
def show():
    with open("E:\\coding\\python\\pyhton-demo\\study\\fast-api\\test.jpg") as fp:
        res_body = fp.read()
    res = Response(res_body)
    return res

#  返回图片
@app.post("/test2/")
async def download_files_stream():
    with open("./test.jpg", "rb") as fp:
        encoded_image_string = base64.b64encode(fp.read())
    payload = {
        "mime": "image/png",
        "image": encoded_image_string,
        "some_other_data": None
    }
    return payload
    #return StreamingResponse(file_like, media_type="image/jpg")


#  返回图片
@app.get("/test3/")
async def download_files_stream():
    file_like = open('./test.jpg.', mode="rb")
    return StreamingResponse(file_like, media_type="image/jpg")

@app.post("/test4")
def image_filter(img: UploadFile = File(...)):
    original_image = Image.open(img.file)
    original_image = original_image.filter(ImageFilter.BLUR)

    filtered_image = BytesIO()
    original_image.save(filtered_image, "JPEG")
    filtered_image.seek(0)

    return StreamingResponse(filtered_image, media_type="image/jpeg")


# uvicorn main:app --reload

if __name__ == "__main__":
    # 日志设置
    dir_log = "logs"
    path_log = os.path.join(dir_log, './日志文件.log')
    # 路径，每日分割时间，是否异步记录，日志是否序列化，编码格式，最长保存日志时间
    logger.add(path_log, rotation='0:00', enqueue=True, serialize=False, encoding="utf-8", retention="10 days")
    logger.debug("服务器重启！")

    uvicorn.run(app="main:app", host="127.0.0.1", port=8080, reload=True)
