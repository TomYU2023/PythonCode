# 选择结构
'''
    if 条件:
        执行语句1
    else:
        执行语句2
'''
if True:
    print("True")
else: # 可以不写
    print("False")
    
print("===============这里是if else语句==============")
    
'''
    if 条件1:
        执行语句1
    elif 条件2:
        执行语句2
    elif 条件3:
        执行语句3
    else: 
        执行语句4
'''

if True:
    print("True")
elif False:
    print("False")
elif False: # 可以多个条件
    print("None")
else: # 可以不写
    print("None")
print("===============这里是if elif else语句==============")

if True:
    print("True")
    pass
else:
    print("False")
    pass
print("===============这里是pass语句==============")