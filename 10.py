# 10 循环结构
'''
while 条件:
    循环体
else:
    循环体
'''
i = 0
while i < 10:
    print(i)
    i += 1
else:
    print("循环结束")
print('=======================这是while循环=======================')

'''
for 变量 in 集合:
    循环体
else:
    循环体

'''
j = 0
for j in range(10):
    print(j)
else:
    print("循环结束")
print('=======================这是for循环=======================')

# break 跳出循环
for i in range(10):
    if i == 5:
        break
    print(i) # 不输出5，并跳出循环
print('=======================这是break跳出循环=======================')

# continue 跳过当前循环
for i in range(10):
    if i == 5:
        continue
    print(i) # 输出除了5
    
print('=======================这是continue跳过当前循环=======================')