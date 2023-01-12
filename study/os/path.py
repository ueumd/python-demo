import os
'''
函数	                作用	            返回值
os.path.splitext()	分割文件名和扩展名	元组
os.path.split()	    分割路径和文件名	元组
'''

url = "http://file.iqilu.com/custom/new/v2016/images/logo.png"

file, ext = os.path.splitext(url)
print(file) #http://file.iqilu.com/custom/new/v2016/images/logo
print(ext)  # .png

print("\n-----------------------------------")

(path, filename) = os.path.split(url)
print(path)         # http://file.iqilu.com/custom/new/v2016/images
print(filename)     # logo.png


print("\n-----------------------------------")

"""
splitext 分割文件名和扩展名
"""

file, ext = os.path.splitext("../temp/images/test.jpg")
print(file) # ../temp/images/test
print(ext)  # .jpg


print("\n-----------------------------------")

"""
split 分割路径和文件名
"""

(path, filename) = os.path.split("../temp/images/test.jpg")
print(path)         # ../temp/images
print(filename)     # test.jpg