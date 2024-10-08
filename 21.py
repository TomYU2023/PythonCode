# 元组与字典拆包
# 元组拆包
def funcA():
    return 1, 2, 3
funcA()
a, b, c = funcA()
print(a, b, c)
print("=======================这个是元组拆包=======================")

# 字典拆包
def funcB():
    return {"name": "张三", "age": 18}
funcB()
d = funcB()
print(d["name"], d["age"])
print("=======================这个是字典拆包=======================")

# lambda 函数: 匿名函数,用于简化函数
# 语法: lambda 参数: 函数体

def funcC():
    return 100
print(funcC())

funcC = lambda: 100 # 匿名函数
print(funcC())

def fn1(x, y):
    return x + y
print(fn1(1, 2))

fn2 = lambda x, y: x + y
print(fn2(1, 2))

print("=======================这个是lambda函数=======================")

# sort 函数: 对列表进行排序
l = [1, 3, 2, 5, 4]
l.sort()
print(l)
l.sort(reverse=True)
print(l)

students = [
    {"name": "张三", "age": 18},
    {"name": "李四", "age": 20},
    {"name": "王五", "age": 22},
    {"name": "赵六", "age": 24},
]

students.sort(key=lambda x: x["age"]) # 按照年龄升序排序
print(students)
students.sort(key=lambda x: x["age"], reverse=True) # 按照年龄降序排序
print(students)

students.sort(key=lambda x: x["name"]) # 按照姓名的ASCII码升序排序
print(students)
students.sort(key=lambda x: x["name"], reverse=True) # 按照姓名的ASCII码降序排序
print(students)
print("=======================这个是sort函数=======================")

