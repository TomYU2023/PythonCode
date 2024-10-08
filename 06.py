# 06输入
'''
输入的7种数据类型：
1.字符串
2.数字
3.布尔值
4.列表
5.元组
6.字典
7.集合
'''
data1 = input("请第一次输入：") # 输入只返回字符串类型
print(data1)
print(type(data1))
print('======================这是字符串类型======================')

# 数据类型转换
'''
数据类型转换：
1.字符串类型转换：str()
2.数值类型转换：int()
3.布尔值类型转换：bool()
4.列表类型转换：list()
5.元组类型转换：tuple()
6.字典类型转换：dict()
7.集合类型转换：set()
'''

data2 = input("请第二次输入：") # 输入只返回字符串类型
int_data = int(data2)
print(type(int_data))
print('======================这是数值类型======================')

data3 = bool(1)
print(data3)
print('======================这是布尔类型======================')

# eval()可以将字符串转换成对应的数据类型
str_data1 = '10'
num_data = eval(str_data1)
print(num_data)
print(type(num_data))
print('======================这是数值类型======================')

str_data2 = '10.1'
float_data = eval(str_data2)
print(float_data)
print(type(float_data))
print('======================这是浮点数类型======================')