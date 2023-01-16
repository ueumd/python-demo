from PIL import Image, ImageFilter
im = Image.open('../temp/images/test.jpg')
#im.show()

print(im)
#<PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=500x333 at 0x279B55D2F10>
print(im.width, im.height, im.size) #500 333 RGB (500, 333)
print("图像模式信息:",im.mode)
print('图片格式', im.format) #JPEG
print("图像是否为只读:",im.readonly)

## 包括了每英寸像素点大小和截图软件信息
print("图像信息：", im.info) #图像信息： {'jfif': 257, 'jfif_version': (1, 1), 'dpi': (100, 100), 'jfif_unit': 1, 'jfif_density': (100, 100)}

#返回为 0 或者 1，分别对应着是和否
print("图像是否为只读:",im.readonly)


new_img = Image.new('RGB', (300, 300),"red")
#new_img.show()

"""
save() 方法用于保存图像，当不指定文件格式时，它会以默认的图片格式来存储；如果指定图片格式，则会以指定的格式存储图片。save() 的语法格式如下：
Image.save(fp, format=None)
参数说明如下：
    fp：图片的存储路径，包含图片的名称，字符串格式；
    format：可选参数，可以指定图片的格式。
"""
new_img.save('./test.png')

"""
convert()+save()

并非所有的图片格式都可以用 save() 方法转换完成，比如将 PNG 格式的图片保存为 JPG 格式，如果直接使用 save() 方法就会出现以下错误：
引发错误的原因是由于 PNG 和 JPG 图像模式不一致导致的。
PNG 是四通道 RGBA 模式，即红色、绿色、蓝色、Alpha 透明色；
JPG 是三通道 RGB 模式。

因此要想实现图片格式的转换，就要将 PNG 转变为三通道 RGB 模式。

convert(mode,parms**)
    mode：指的是要转换成的图像模式；
    params：其他可选参数
"""

test_img = Image.open('./test.png')
c_img = test_img.convert('RGB')
c_img.save('./hello.jpg')

""""
图像缩放操作
resize(size, resample=image.BICUBIC, box=None, reducing_gap=None)

参数说明：
size：元组参数 (width,height)，图片缩放后的尺寸；
resample：可选参数，指图像重采样滤波器，与 thumbnail() 的 resample 参数类似，默认为 Image.BICUBIC；
box：对指定图片区域进行缩放，box 的参数值是长度为 4 的像素坐标元组，即 (左,上,右,下)。注意，被指定的区域必须在原图的范围内，如果超出范围就会报错。当不传该参数时，默认对整个原图进行缩放；
reducing_gap：可选参数，浮点参数值，用于优化图片的缩放效果，常用参数值有 3.0 和 5.0。
"""

try:
    new_c_img = c_img.resize((550,260))
    new_c_img.save('./n_img.jpg')
    print("查看新图像的尺寸", new_c_img.size)
except IOError:
    print("查看图像失败")


"""
mage 类提供了用于分离图像和合并图像的方法 split() 和 merge() 方法，通常情况下，这两个方法会一起使用。
split()
"""

butterfly = Image.open('../temp/images/butterfly.jpg')
r,g,b = butterfly.split()
# r.show()
# g.show()
# b.show()

#重新组合颜色通道，返回先的Image对象
image_merge = Image.merge('RGB', (b,g,r))
#image_merge.show()

panda = Image.open('../temp/images/panda.jpg')
#图像模糊处理
panda_blur=panda.filter(ImageFilter.BLUR)
panda_blur.show()

#浮雕图
panda2=panda.filter(ImageFilter.EMBOSS)
panda2.show()


