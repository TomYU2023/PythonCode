# 魔术方法__name__
# 所有魔术方法都以双下划线开头和结尾
# 作用：测试代码
# 将多个自定义模块存在一起交package，包

def fn1(x, y):
    return x + y

if __name__ == '__main__': # 运行时执行，不会被调用到其他程序中
    print('__name__ is __main__')
    print(fn1(1, 2)) 
        
