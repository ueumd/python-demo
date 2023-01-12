import random

""""
.util .来表示当前包的包名
"""
from .util import *

# 从当前包导入car
from .car import Car

def test_add():
    print("__init__模块函数")