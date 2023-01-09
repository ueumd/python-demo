import argparse
from PIL import Image


# argparse定义四个步骤
# 导入argparse包 ——import argparse
# 创建一个命令行解析器对象 ——创建 ArgumentParser() 对象
# 给解析器添加命令行参数 ——调用add_argument() 方法添加参数
# 解析命令行的参数 ——使用 parse_args() 解析添加的参数

# 1. 定义命令行解析器对象
parser = argparse.ArgumentParser(description="Demo of argparse")

# 2. 添加命令行参数
parser.add_argument('-i','--img_path', type=str, default='imgs/test.jpg')
parser.add_argument('--epochs', type=int, default=30)
parser.add_argument('--batch', type=int, default=4)

# 3. 从命令行中结构构解析参数
opt = parser.parse_args()

print('opt:', opt)

epochs = opt.epochs
batch = opt.batch

img = Image.open(opt.img_path)
img.show()

print('show {}  {}'.format(epochs, batch, img))


#python demo1.py -i imgs/test.jpg --epochs 30 --batch 4