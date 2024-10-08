# 13死循环案例---猜数字
import random

random_num = random.randint(1, 100)

while True:
    num = int(input("请输入一个数字："))
    if num > random_num:
        print("猜大了")
    elif num < random_num:
        print("猜小了")
    else:
        print("猜对了")
        break
