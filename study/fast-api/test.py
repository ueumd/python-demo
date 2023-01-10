import matplotlib.pyplot as plt
from starlette.responses import StreamingResponse

from colorizers import *
from fastapi import FastAPI, File, UploadFile

from typing import Union

from PIL import Image, ImageFilter
from io import BytesIO
import uvicorn
import uuid

app = FastAPI()


def change(img_path, file_name):
    use_gpu = False
    save_prefix = "saved"

    # load colorizers
    colorizer_eccv16 = eccv16(pretrained=True).eval()
    colorizer_siggraph17 = siggraph17(pretrained=True).eval()
    if (use_gpu):
        colorizer_eccv16.cuda()
        colorizer_siggraph17.cuda()

    # default size to process images is 256x256
    # grab L channel in both original ("orig") and resized ("rs") resolutions
    img = load_img(img_path)
    (tens_l_orig, tens_l_rs) = preprocess_img(img, HW=(256, 256))
    if (use_gpu):
        tens_l_rs = tens_l_rs.cuda()

    # colorizer outputs 256x256 ab map
    # resize and concatenate to original L channel
    img_bw = postprocess_tens(tens_l_orig, torch.cat((0 * tens_l_orig, 0 * tens_l_orig), dim=1))
    out_img_eccv16 = postprocess_tens(tens_l_orig, colorizer_eccv16(tens_l_rs).cpu())
    out_img_siggraph17 = postprocess_tens(tens_l_orig, colorizer_siggraph17(tens_l_rs).cpu())

    plt.imsave('%s_eccv16.png' % file_name, out_img_eccv16)
    plt.imsave('%s_siggraph17.png' % file_name, out_img_siggraph17)

    plt.figure(figsize=(12, 8))
    plt.subplot(2, 2, 1)
    plt.imshow(img)
    plt.title('Original')
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.imshow(img_bw)
    plt.title('Input')
    plt.axis('off')

    plt.subplot(2, 2, 3)
    plt.imshow(out_img_eccv16)
    plt.title('Output (ECCV 16)')
    plt.axis('off')

    plt.subplot(2, 2, 4)
    plt.imshow(out_img_siggraph17)
    plt.title('Output (SIGGRAPH 17)')
    plt.axis('off')

    plt.savefig('./imgs_out/' + file_name + '.jpg')

    #plt.show()


@app.post("/test4")
def image_filter(img: UploadFile = File(...)):
    original_image = Image.open(img.file)
    original_image = original_image.filter(ImageFilter.BLUR)

    filtered_image = BytesIO()
    original_image.save(filtered_image, "JPEG")
    filtered_image.seek(0)

    return StreamingResponse(filtered_image, media_type="image/jpeg")


@app.post("/uploadfile/")
def upload_file(file: UploadFile = File(...)):
    img_bytes = file.file.read()
    id = uuid.uuid4()
    uuidString = str(id).replace("-", "")
    file_name = uuidString + '-' + file.filename

    with open("./upload/" + file_name, 'wb') as f:
        f.write(img_bytes)

    # img = Image.open("./test.jpg")
    # img.show()
    change("./upload/" + file_name, uuidString)

    original_image = Image.open('./imgs_out/' + file_name + '.jpg')
    original_image = original_image.filter(ImageFilter.BLUR)

    filtered_image = BytesIO()
    original_image.save(filtered_image, "JPEG")
    filtered_image.seek(0)
    return StreamingResponse(filtered_image, media_type="image/jpeg")

    #return {"filename": file.filename}


# uvicorn main:app --reload

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="192.168.1.11", port=8000, reload=True)
