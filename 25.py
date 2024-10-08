# 获取目录名称 F:\AI学习\Python基础\pypypy
import os
# os.getcwd() 获取当前目录
print(os.getcwd()) # cwd:current working directory
print("============================这是获取当前目录============================")

# os.chdir() 切换目录
os.chdir("F:\AI学习\Python基础\pypypy")
print(os.getcwd())
print("============================这是切换目录============================")

# os.listdir() 获取目录下所有文件名称
print(os.listdir())
print("============================这是获取目录下所有文件名称============================")

# python也能控制删除文件和文件夹，本课不教授，怕误操作删掉重要的东西