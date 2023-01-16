import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr) # [1 2 3 4]
print(arr[2]) # 3
print(type(arr))  # <class 'numpy.ndarray'>

# 多维数组

arr2 = np.array([[1, 3, 3], ['A', 'B', 'C']])
print(arr2)
"""
[['1' '3' '3']
 ['A' 'B' 'C']]

"""

# ndim查看数组维数

print(arr.ndim) # 1
print(arr2.ndim) # 2

# 使用 ndmin 参数创建不同维度的数组：
arr3 = np.array([1, 2, 3], ndmin=2)
print(arr3) # [[1 2 3]]
print(arr3.ndim) # 12

# reshape数组变维 数组的形状指的是多维数组的行数和列数。

e = np.array([[1,2],[3,4],[5,6]])  # 3行2列
print(e)
""""
[[1 2]
 [3 4]
 [5 6]]
"""

e = e.reshape(2, 3) # 2行3列
print(e)
"""
[[1 2 3]
 [4 5 6]]
"""


# 数组的属性

# ndarray.shape
# shape 属性的返回值一个由数组维度构成的元组，比如 2 行 3 列的二维数组可以表示为(2,3)，该属性可以用来调整数组维度的大小。

print(e.shape) # (2, 3)

# 数据类型为int8，代表1字节
x = np.array([1,2,3,4,5], dtype = np.int8)
print (x.itemsize) # 1

# 数据类型为int64，代表8字节
x = np.array([1,2,3,4,5], dtype = np.int64)
print (x.itemsize) # 8

#  empty 并非创建空数组
arr4 = np.empty((3, 2), dtype=int)
print(arr4)
"""
[[ 2080666631  1778416640]
 [-1593401339  1678140416]
 [ 2080607495 -1610605817]]
"""

# NumPy遍历数组
# NumPy 提供了一个 nditer 迭代器对象，它可以配合 for 循环完成对数组元素的遍历。

arr5 = np.arange(0, 60, 5)
arr5 = arr5.reshape(3, 4)

for x in np.nditer(arr5):
    print(x)


# arr5的转置数组

c_arr = arr5.T
print(c_arr)
"""
[[ 0 20 40]
 [ 5 25 45]
 [10 30 50]
 [15 35 55]]
"""

for x in np.nditer(c_arr):
   print(x, end=",") #0,5,10,15,20,25,30,35,40,45,50,55,