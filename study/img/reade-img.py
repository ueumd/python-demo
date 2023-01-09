import requests
from PIL import Image
from io import BytesIO

response = requests.get('https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png')
response = response.content

BytesIOObj = BytesIO()
BytesIOObj.write(response)

img = Image.open(BytesIOObj)
img.show()