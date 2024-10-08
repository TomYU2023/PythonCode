# 从自定义函数模块导入hello函数
# 注意，自定义函数文件不能以数字命名

from mypackage.Salute import * # 在___init__.py中写入了__all__

hello()
print("============================这是从自定义函数模块导入hello函数============================")

# 函数的返回值
def age():
    print(18)
    return 1, "haha"
age() # 18
print(age()) # age()得到18，print()得到1, haha

print("============================这是函数的返回值============================")

def age():
    print(18)
    return 
age() # 18
print(age()) # age()得到18，print()得到None

print("============================这是没有函数的返回值============================")

# 函数的说明文档
def age():
    '''这是一个函数的说明文档'''
    print(18)
    return
age()
print(age.__doc__) # age.__doc__得到函数的说明文档
help(age)
print("============================这是函数的说明文档============================")

# 函数嵌套
def funcA():
    print("funcA开始")
    print("funcA结束")
def funcB():
    print("funcB开始")
    print("funcB结束")
    funcA()
        
funcB()
print("============================这是函数嵌套============================")

# 全局变量
x = 10
def funcC():
    print(x)

funcC()
print("============================这是全局变量============================")

# 局部变量
def funcD():
    x = 20
    print(x)
funcD()
print("============================这是局部变量============================")

# global 关键字
def funcE():
    global x
    x = 30
    print(x)
funcE()
print(x)
print("============================这是global关键字============================")

# 函数的参数
# 函数的形式参数
def funcF(name):
    print(name) # 函数的形式参数
funcF("John") # 函数的实际参数
funcF("Jim")
print("============================这是函数的参数============================")

# 函数的实际参数
def funcH(name, age):
    print(name, age) # 函数的形式参数
funcH(age = 18, name = "John") # 函数的实际参数
print("============================这是函数的参数============================")

# 位置参数
def funcI(name, age):
    print(name, age)
    
funcI("John", 18)
print("============================这是位置参数============================")

# 关键字参数
def funcJ(name, age):
    print(name, age)
 
funcJ(age = 18, name = "John")
print("============================这是关键字参数============================")

# 默认值参数
def funcK(name, age = 18):
    print(name, age)
    
funcK("John")
funcK("Jim", 20)
print("============================这是默认值参数============================")

# 不定长参数：*args, **kwargs，当函数的参数不确定时使用
# 不定长位置参数
# 作用：将参数转换为元组
# 语法：*args
def funcL(*args): # 必须要用*，可以不用命名args
    print(args)
    print(type(args))
    for i in args:
        print(i)
funcL(1, 2, 3, 4, 5)
print("============================这是不定长位置参数============================")

# 不定长关键字参数
# 作用：将参数转换为字典
# 语法：**kwargs
def funcM(**kwargs): # 必须要用**，可以不用命名kwargs
    print(kwargs)
    print(type(kwargs))
    for i in kwargs:
        print(i, kwargs[i])
funcM(name = "John", age = 18)
print("============================这是不定长关键字参数============================")

# 参数混用的情况：def 函数名（普通参数，*args，默认参数，**kwargs）
def dung(name, *args, age = 18, **kwargs):
    print(name, args, age, kwargs)
dung("John", 1, 2, 3, 4, 5, address = "Beijing", age = 20)
print("============================这是参数混用的情况============================")
