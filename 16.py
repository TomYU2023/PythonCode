# 元组
# 元组必须要用小括号括起来
# 元组必须以逗号分割
# 单个元素的元组，必须以逗号结尾

tuple1 = ('a', 'b', 'c')
tuple2 = (1, 2, 3)
print(tuple1)
print(type(tuple1))
print(tuple2)
print(type(tuple2))
print(tuple1[0])
print(tuple1[1:])
print(tuple1[0:2])
print("========================这里是元组的切片操作========================")

# 元组的相关操作
tuple2 = ('a', 'b', 'c')
print(tuple2)
print(len(tuple2)) # 元组长度
print(tuple2.count('a')) # 元组中某个元素的个数
print(tuple2.index('b')) # 元组中某个元素的索引
print("========================这里是元组的相关操作========================")

# 元组和列表的区别：元组不可变，列表可变
# tuple2 = ('a', 'b', 'c')
# print(tuple2)
# tuple2[0] = 'd' # TypeError: 'tuple' object does not support item assignment
# print(tuple2) # 报错
list1 = ['a', 'b', 'c']
print(list1)
list1[0] = 'd'
print(list1)
print("========================这里是元组和列表的区别========================")

# 元组和列表的转换
tuple3 = ('a', 'b', 'c')
print(tuple3)
list2 = list(tuple3) # 转换成列表
print(list2)
tuple4 = tuple(list2) # 转换成元组
print(tuple4)
print("========================这里是元组和列表的转换========================")

# 元组和字符串的转换
tuple5 = ('a', 'b', 'c')
print(tuple5)
str1 = ''.join(tuple5) # 转换成字符串
print(str1)
print(type(str1))
print("========================这里是元组和字符串的转换========================")
