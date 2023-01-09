from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI, File, UploadFile

import uvicorn

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
def upload_file(file: UploadFile = File(...)):
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


#uvicorn main:app --reload

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8080, reload=True)



