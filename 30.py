# 闭包：用于创建一个函数，该函数可以记住上一次调用的位置
def outter(func):
    # *args意思是函数可以接受任意个参数， **kwargs意思是函数可以接受任意个关键字参数
    # 区别是*args和**kwargs，*args是元组，**kwargs是字典
    def inner(*args, **kwargs): 
        print("这个是闭包")
        func(*args, **kwargs)
    return inner

def test(name, age):
    print("test", name, age)
    return "test"

test("zhangsan", 18)
outter(test)("zhangsan", 18) # 这里两个括号都是调用函数

print("===========================这是闭包的一种写法==========================")

# 装饰器：用于添加一些额外的功能
def outter(func):
    def inner(*args, **kwargs):
        print("这个是装饰器")
        func(*args, **kwargs)
    return inner
@outter
def test(name, age):
    print("test", name, age)
    return "test"

test("zhangsan", 18)

print("===========================这是装饰器的一种写法==========================")

# 迭代器：用于遍历
class MyIter:
    def __init__(self, num): # 初始化
        self.num = num
        self.index = 0
    def __iter__(self): # 迭代器
        return self
    def __next__(self): # 下一个，代表遍历
        if self.index < self.num:
            self.index += 1
            return self.index
        else:
            raise StopIteration

for i in MyIter(10):
    print(i)
    if i == 5:
        break
print("==========================这是迭代器的一种写法==========================")

# 生成器：用于生成数据
def my_generator(num):
    for i in range(num):
        yield i
        print("yield", i)

for i in my_generator(10):
    print(i)
    if i == 5:
        break

print("==========================这是生成器的一种写法==========================")
