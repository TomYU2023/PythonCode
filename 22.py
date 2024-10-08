# 模块
'''
模块：
    1.模块：一个.py文件，可以包含多个函数，类，变量，常量
    2.模块化：将一个大程序，拆分成多个模块，每个模块只做一件事情
    3.模块化：提高代码的复用率，提高代码的维护性
    4.模块化：提高代码的扩展性，提高代码的维护性
    5.模块化：提高代码的维护性，提高代码的扩展性
基本语法：
    1.导入模块：import 模块名
    2.导入模块中的函数：from 模块名 import 函数名
    3.导入模块中的类：from 模块名 import 类名
    4.导入模块中的变量：from 模块名 import 变量名
    5.导入模块中的常量：from 模块名 import 常量名
    6.导入模块中的所有内容：from 模块名 import *
'''
# import math as m # 导入模块
# import random as r
import math, random
print(math.sqrt(9))
print(random.randint(1, 10))

print("================================这是导入的模块=====================================")

# time模块
import time
print(time.time()) # 获取当从1970年1月1日0时0分0秒到现在的时间戳
print(time.localtime()) # 获取当前时间
print(type(time.localtime()))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) # 表示将时间戳转换为指定的格式


Start = time.time() # 获取当前时间戳

list = []
for i in range(5000000):
    list.append(i)

Stop = time.time() # 获取当前时间戳
print(f'列表生成耗时：{Stop - Start}s')

print("=================================这是导入的time模块=====================================")

# .sleep模块
import time
for i in range(10):
    print(i)
    time.sleep(1)

print("=================================这是导入的sleep模块=====================================")
