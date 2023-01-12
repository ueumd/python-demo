"""
https://www.cnblogs.com/wj-1314/p/8421724.html
"""
info ={'name':'Tom','age':'1','work':'Love Jack'}
info['sex'] = 'cat'
print(info)

# pop()：删除指定key的键值对
info.pop('work')

#setdefault()：删除指定的元素，如果没有，则返回none， 并在列表添加son：None
# res = info.setdefault('son')
# print(res) #None

# get():通过给定的key，查找对应的value，如果给定的可以在字典中无，则返回None

res = info.get("name")
print(res) #Tom

'''
返回键，值，键值对

　　keys():以列表（list）返回字典中的所有键（key），字典是无序的，所以这个list返回的不是定义字典的顺序

　　values():以列表（list）返回字典中的所有值，这个list的顺序跟keys()返回的list顺序是一一对应的

　　items():以列表（list）返回可遍历的(键, 值) 元组数组，这个tuple的list包含了dictionary的所有数据
'''

#1,请循环遍历除所有的key
for keys in info.keys():
    print(keys)
    """"
    name
    age
    sex
    son
    """

#遍历出所有的value
for value in info.values():
    print(value)
    """
    Tom
    1
    cat
    None
    """

for key, value in info.items():
    print(key + ":" + value)
    """
    name:Tom
    age:1
    sex:cat
    """


"""
根据字典的键值进行排序　　
反序： reverse = True
"""
mylist = ['学习', '工作', '玩耍', '学习', '工作', '工作']

print(mylist)

# 去重
my_set = set(mylist)
print(my_set)

my_dict = {}

for item in my_set:
    # 指定的元素出现的次数
    res = mylist.count(item)
    #print(res)

    sample = {
        item: res
    }
    print(sample)

    """
    {'玩耍': 1}
    {'工作': 3}
    {'学习': 2}
    """

    my_dict.update(sample)

print(my_dict)

print(sorted(my_dict.items(), key=lambda my_dict:my_dict[1], reverse=True))