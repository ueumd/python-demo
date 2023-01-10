from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI, File, UploadFile, Response
from fastapi.responses import StreamingResponse
import base64

import uvicorn

from PIL import Image, ImageFilter

from io import BytesIO

# 文件上传
# https://cloud.tencent.com/developer/article/1883204?from=15425

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def hello():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def getItem(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


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
    uvicorn.run(app="main:app", host="127.0.0.1", port=8080, reload=True)
