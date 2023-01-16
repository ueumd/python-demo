"""
关键字with在不再需要访问文件后将其关闭，不需要去调用close()
Python自会在合适的时候自动将其关闭。

打开文件的函数为open('filename',mode='r',encode='None')

f=open('filename',mode='r',encode='utf-8') 或者 with open('filename') as f
"""

""" 含有中文的以encoding='utf-8'方式来读取 """
with open('./zh.txt', encoding='utf-8') as file:
    contents = file.read()
    print(contents)

print("--------------逐行读取------------------\n")
with open('./zh.txt', encoding='utf-8') as file:
   for line in file:
       """
        在这个文件中，每行的末尾都有一个看不见的换行符，而
        print语句也会加上一个换行符，因此每行末尾都有两个换行符：一个来自文件，另一个来自print
        语句。要消除这些多余的空白行，可在print语句中使用rstrip()：
       """
       print(line.rstrip())


print("--------------------------------\n")
with open('./file.txt') as file:
    contents = file.read()
    print(contents)


print("--------------------------------\n")
filename = 'pi_digits.txt'
with open('./zh.txt', encoding='utf-8') as file:
    lines = file.readlines()

for line in lines:
    print(line.rstrip())