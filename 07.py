# 07运算符
'''
算术运算符：
含义：
    用于计算两个值
    +   -   *   /   //   %   **
    运算符优先级：
        1. **
        2. *   /   //   %
        3. +   -
'''
a = 10
b = 20
print("a + b = " + str(a + b))
print("a - b = " + str(a - b))
print("a * b = " + str(a * b))
print("a / b = " + str(a / b))
print("a // b = " + str(a // b))
print("a ** b = " + str(a ** b))
print("a % b = " + str(a % b))
print('================这是算术运算符=====================')

'''
比较运算符：
含义：
    用于判断两个值是否相等
    ==   !=   >   <   >=   <=
    运算符优先级：
        1. ==   !=
        2. >   <   >=   <=
'''
c = 10
d = 20
print("c > d = " + str(c > d))
print("c < d = " + str(c < d))
print("c == d = " + str(c == d))
print("c != d = " + str(c != d))
print('================这是比较运算符=====================')

'''
逻辑运算符：
含义：
    用于判断两个条件是否成立
    and   or   not
    逻辑运算符优先级：
        1. not
        2. and   or
'''
e = 10
f = 20
print("e and f = " + str(e and f))
print("e or f = " + str(e or f))
print("not e = " + str(not e))
print('================这是逻辑运算符=====================')

'''
赋值运算符：
含义：
    用于给变量赋值
    =   +=   -=   *=   /=   //=   %=   **=
    运算符优先级：
        1. =
        2. +=   -=   *=   /=   //=   %=   **=
'''
g = 10
g += 10
print("g = " + str(g))
g -= 10
print("g = " + str(g))
g *= 10
print("g = " + str(g))
g /= 10
print("g = " + str(g))
g //= 10
print("g = " + str(g))
g **= 10
print("g = " + str(g))
g %= 10
print("g = " + str(g))
print('================这是赋值运算符=====================')

'''
身份运算符：
含义：
    用于判断两个对象是否为同一个对象
    is   is not
    运算符优先级：
        1. is   is not
'''
h = 10
i = 20
print("h is i = " + str(h is i))
print("h is not i = " + str(h is not i))
print('================这是身份运算符=====================')
'''
位运算符：
含义：
    用于对二进制进行运算
    &   |   ^   ~   <<   >>
    运算符优先级：
        1. ~
        2. &   |   ^
        3. <<   >>
'''
j = 10
k = 20
print("j & k = " + str(j & k))
print("j | k = " + str(j | k))
print("j ^ k = " + str(j ^ k))
print("~j = " + str(~j))
print("j << k = " + str(j << k))
print("j >> k = " + str(j >> k))
print('================这是位运算符=====================')
