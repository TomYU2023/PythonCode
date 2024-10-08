# 11循环嵌套

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()
print('===================这是for嵌套的代码===================')

a = 1
while a < 10:
    b = 1
    while b < a + 1:
        print('%d*%d=%d' % (a, b, a * b), end='\t')
        b += 1
    print()
    a += 1
print('===================这是while嵌套的代码===================')

# 死循环
while True:
    print('死循环')
    input('请按回车键退出')
    break # 跳出离他最近的循环
print('===================这是break之后的代码===================')

while True:
    print('开始执行') # 跳过一次
    input('请按回车键退出')
    print('这一条执行')
    continue # 跳过本次循环
print('===================这是continue之后的代码===================')
