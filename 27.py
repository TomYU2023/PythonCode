# 面向对象编程
'''
对象=属性（变量）+方法（函数）

1.分析有哪些实体类
2.定义实体，增加属性和功能
3.创建对象
'''
class Student(object):
    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    # 谁调用这个方法，self就是谁
    def __init__(self, name, age): # self代表创建的实例本身，不需要传参
        self.name = name
        self.age = age

    def study(self, course):
        print('%s正在学习%s.' % (self.name, course))

    # PEP 8要求标识符的名字用全小写方式，单词之间用下

    def __str__(self):
        return '姓名:%s,年龄:%d' % (self.name, self.age)
    
    def __del__(self):
        print('销毁对象') # 文件执行完毕则销毁对象，释放占用的内存

if __name__ == '__main__':
    # 创建对象
    stu1 = Student('骆昊', 38)
    stu2 = Student('王大锤', 15)
    # 打印对象的类型
    print(type(stu1))
    print(type(stu2))
    print("=================这是打印对象类型=====================")
    # 打印对象的属性
    print('%s的年龄是%d' % (stu1.name, stu1.age))
    print('%s的年龄是%d' % (stu2.name, stu2.age))
    print('=======================这是打印属性============================')
    stu1.study('Python程序设计')
    stu2.study('思想品德')
    print("=================这是调用study方法=====================")
    print(stu1)
    print(stu2)
    print("================这是str方法=====================")
    
    
