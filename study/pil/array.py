
from PIL import Image
import numpy as np

my_panda = Image.open('../temp/images/panda.jpg')

# Image图像转换为ndarray数组
panda_arr = np.array(my_panda)

print(panda_arr)

#ndarray转换为Image图像
arr_panda = Image.fromarray(panda_arr)
arr_panda.show()