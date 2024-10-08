# 文件的操作
# 新建文件
f = open('new_file.txt', 'w') # 另一种方法是with open() as f:
f.close()
print(f.closed)
print("=======================这里是新建文件方法1=======================")
with open('new_file.txt', 'w') as f: # r, w, a,只能操作字符串类型的文件
    f.write('hello world')
    f.close()
    print(f.closed)
print("=======================这里是新建文件方法2=======================")

# 写入文件
f = open('new_file.txt', 'w') # rb, wb, ab,只能操作二进制类型的文件,比如音频，视频文件
f.write('hello world')
f.close()
print(f.closed)
print("=======================这里是写入文件=======================")

# 追加文件
f = open('new_file.txt', 'a') # a不清空文件写入，w清空文件写入
f.write('\nhello world')
f.close()
print(f.closed)
print("=======================这里是追加文件=======================")

# 读取文件
f = open('new_file.txt', 'r', encoding='utf-8') # encoding='utf-8' 解决中文乱码问题
print(f.read()) # 读取文件，可以（）设置读取多少个字符，默认读取所有字符
print(f.read(5)) # 读取5个字符
print(f.readline()) # 读取一行
print(f.readlines()) # 读取所有行
f.close()
print(f.closed)
print("=======================这里是读取文件=======================")

# 相对路径：相对于当前文件所在的目录
# 绝对路径：从根目录开始

# 文件重命名
import os
f = open('new_file1.txt', 'w') # 另一种方法是with open() as f:
f.close()
print(f.closed)
print("=======================这里是新建文件方法1=======================")
with open('new_file1.txt', 'w') as f: # r, w, a,只能操作字符串类型的文件
    f.write('hello world')
    f.close()
    print(f.closed)
print("=======================这里是新建文件方法2=======================")
os.mkdir('new_dir') # 新建文件夹
os.rmdir('new_dir') # 删除空文件夹
print(os.path.exists('new_dir'))
print("=======================这里是新建文件夹=======================")
os.rename('new_file1.txt', 'new_file2.txt') # 重命名
print(os.path.exists('new_file2.txt'))
print("=======================这里是文件重命名=======================")
os.remove('new_file2.txt') # 删除文件
print(os.path.exists('new_file2.txt'))
print("=======================这里是文件删除=======================")

