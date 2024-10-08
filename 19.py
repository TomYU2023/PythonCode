# 数据容器的公共方法
'''
列表、元组、集合、字典的区别
列表：可变容器，元素可重复，元素可重复，元素可排序，元素可索引，元素可切片，元素可迭代，元素可嵌套
元组：不可变容器，元素可重复，元素可排序，元素可索引，元素可切片，元素可迭代，元素不可嵌套
集合：不可变容器，元素不可重复，元素不可排序，元素不可索引，元素不可切片，元素不可迭代，元素不可嵌套
字典：可变容器，元素不可重复，元素不可排序，元素不可索引，元素不可切片，元素不可迭代，元素不可嵌套
'''
'''
+ 合并容器
* 复制操作
in 判断元素
not in 判断元素
max() 获取最大值
min() 获取最小值
'''
str1 = 'abcdefg'
str2 = '1234567'
print(str1 + str2)
print(str1 * 3)
print('a' in str1)
print('a' not in str1)
print(max(str1))
print(min(str1))
print("==============================这是数据容器的公共方法==============================")

# 数据容器类型转换
'''
tuple() 转换为元组
list() 转换为列表
set() 转换为集合
'''
str1 = 'abcdefg'
print(tuple(str1))
print(type(tuple(str1)))
print(list(str1))
print(type(list(str1)))
print(set(str1))
print(type(set(str1)))
print("==============================这是数据容器类型转换==============================")

# 推导式
'''
list() 列表推导式
set() 集合推导式
dict() 字典推导式
'''
# 表达式 for 变量 in 列表
list1 = [i for i in range(10)] 
print(list1)
set1 = {i for i in range(10)} 
print(set1)
dict1 = {i: i for i in range(10)} # 自动以索引补键
print(dict1)

# 表达式 for 变量 in 列表 if 条件
list2 = [i for i in range(10) if i % 2 == 0]
print(list2) # [0, 2, 4, 6, 8]
set2 = {i for i in range(10) if i % 2 == 0}
print(set2) # {0, 2, 4, 6, 8}
dict2 = {i: i for i in range(10) if i % 2 == 0}
print(dict2) # {0: 0, 2: 2, 4: 4, 6: 6, 8: 8}

# 表达式 for 变量 in 列表 for 变量 in 列表
list3 = [i for i in range(10) for j in range(10)] # 一般不推荐使用
print(list3) 
set3 = {i for i in range(10) for j in range(10)}
print(set3)
dict3 = {i: i for i in range(10) for j in range(10)}
print(dict3)
print("==============================这是推导式==============================")
