# 异常捕获：用于预判用户的错误，一般与input配合使用
'''
语法：
    try:
        代码
    except 异常类型: # 可选,预判异常
        代码
    else: # 可选, 没有异常才执行
        代码
    finally: # 可选, 无论是否有异常都会执行
'''
# 常见异常错误：
# ZeroDivisionError: 除0错误
try:
    print(1/0)
except ZeroDivisionError: 
    print("除数不能为0") # 捕获异常
    print("有异常就执行")
else:
    print("没有异常执行")
finally:
    print("不管有没有异常都会执行")
    # exit() 写上就退出程序
print("===========================除0错误===========================")
# NameError: 未定义变量
# SyntaxError: 语法错误
# IndexError: 索引错误
# TypeError: 类型错误
# ValueError: 值错误
# KeyError: 键错误
# FileNotFoundError: 文件不存在
# IOError: 读写错误
# ImportError: 导入错误
# AttributeError: 属性错误
# KeyboardInterrupt: 键盘中断


