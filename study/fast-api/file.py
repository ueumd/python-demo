from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/files/")
def create(file: bytes = File(...)):
    return {"file_size": len(file)}

@app.post("/uploadfile/")
def upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}