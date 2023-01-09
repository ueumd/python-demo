from PIL import Image
import requests
from io import BytesIO

url = "https://img.zcool.cn/community/01gvtr8wdcviqahe6w3goi3533.jpg?x-oss-process=image/auto-orient,1/resize,m_lfit,w_1280,limit_1/sharpen,100/format,webp/quality,q_100"

img = Image.open(BytesIO(requests.get(url).content))
img.show()