# 字典的相关操作
# 字典中的元素的类型是键值对，键是唯一的，值可以重复

dic = {'name': '小明', 'age': 18, 'sex': '男'}
print(dic) # 打印字典
print(type(dic))
print(dic['name']) # 打印字典中的键值，与get()的区别 dic['name']不存在，会报错
print(type(dic['name']))
print(dic['age']) # 打印字典中的键值
print(type(dic['age']))
print(dic['sex']) # 打印字典中的键值
print(type(dic['sex']))

print(dic.keys()) # 打印字典中的键
print(type(dic.keys()))
print(dic.values()) # 打印字典中的值
print(type(dic.values()))
print(dic.items()) # 打印字典中的键值对
print(type(dic.items()))

print(dic.get('name')) # 打印字典中的键值，与dic['name']不同，如果键不存在，返回None
print(type(dic.get('name')))
print(dic.get('age')) # 打印字典中的键值
print(type(dic.get('age')))
print(dic.get('sex')) # 打印字典中的键值
print(type(dic.get('sex')))
print("==================================这是字典的基本操作==================================")

# 字典的增删改查
dic = {'name': '小明', 'age': 18, 'sex': '男'}
dic['name'] = '小红' # 修改字典中的键值
print(dic)
dic['age'] = 19 # 修改字典中的键值
print(dic)
dic['address'] = '北京' # 增加字典中的键值
print(dic)
del dic['sex'] # 删除字典中的键值
print(dic)
dic.clear() # 清空字典
print(dic)
print("==================================这是字典的增删改查==================================")

# 字典的查询
dic = {'name': '小明', 'age': 18, 'sex': '男'}
print(dic.get('name')) # 查询字典中的键值，与dic['name']不同，如果键不存在，返回None
print(dic.get('age')) # 查询字典中的键值
print(dic.get('sex')) # 查询字典中的键值
print(dic.get('address')) # 查询字典中的键值，如果键不存在，返回None
print("==================================这是字典的查询==================================")

# 字典的遍历
dic = {'name': '小明', 'age': 18, 'sex': '男'}
for key in dic: # 遍历字典中的键
    print(key)

for value in dic.values(): # 遍历字典中的值
    print(value)
    
for item in dic.items(): # 遍历字典中的键值对
    print(item)
print("==================================这是字典的遍历==================================")

# 字典的合并
dic1 = {'name': '小明', 'age': 18, 'sex': '男'}
dic2 = {'address': '北京', 'phone': '1234567890'}
dic3 = dic1.copy() # 合并字典，copy()方法代表复制
print(dic3)
dic3.update(dic2) # 合并字典，update()方法代表更新
print(dic3)
print("==================================这是字典的合并==================================")

# 字典的enumerate()方法
dic = {'name': '小明', 'age': 18, 'sex': '男'}
for key, value in enumerate(dic): # 遍历字典中的键值对，并返回索引和值
    print(key, value)
    
print("==================================这是字典的enumerate()方法==================================")

