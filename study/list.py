bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[1])  #cannondale
print(bicycles[1].title()) #Cannondale 首字母大写

""""
通过将索引指定为-1，可让Python返回最后一个列表元素：
"""
print(bicycles[-1]) #specialized


motorcycles = ['honda', 'yamaha', 'suzuki']


# 修改列表元素
motorcycles[0] = 'ducati'
print(motorcycles)

# 在列表末尾添加元素
motorcycles.append('honda')

print(motorcycles) #['ducati', 'yamaha', 'suzuki', 'honda']


# 指定位置插入元素
motorcycles.insert(0, 'ducati')

print(motorcycles.count("ducati"))

print(motorcycles)

# del删除了列表motorcycles中的第一个元素
del motorcycles[0]

# 方法pop()可删除列表末尾的元素