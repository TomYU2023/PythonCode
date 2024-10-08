# 字符串操作
# 字符串切片

str = 'abcdefghijklmnopqrstuvwxyz'

print(str[:]) # abcdefghijklmnopqrstuvwxyz
print(str[1:]) # bcdefghijklmnopqrstuvwxyz
print(str[1:9]) # bcdefgh
print(str[1:5:2]) # bd
print(str[::2]) # acegikmoqsuwy
print(str[::-1]) # zyxwvutsrqponmlkjihgfedcba
print("=============================字符串切片=============================")

# 字符串连接
str1 = 'abc'
str2 = 'def'
str3 = " ".join(str1) # a b c
print(str3)
join = str1.join(str2) # 把abc插入到d和ef之间
print(join)
print(str1 + str2)
print("str1 + str2 = " + str1 + str2)
print("str1 + str2 = %s" % (str1 + str2)) # %s格式化字符串
print(f"str1 + str2 = {str1 + str2}") # f字符串格式化字符串
print("str1 + str2 = {}".format(str1 + str2)) # {}格式化字符串

print("=============================字符串连接=============================")

# 字符串重复
print(str1 * 3)
print("=============================字符串重复=============================")

# 字符串查找
print(str.find('c')) # 从0开始查找，find 找不到会返回-1
print(str.find('5')) 
print(str.find('c', 1)) # 从1开始查找
print(str.find('c', 1, 3)) # 从1开始查找,查找到3
print(str.index('c')) # 从0开始查找, index 查找不到，会报错 

print("=============================字符串查找=============================")

# 字符串统计
print(str.count('a')) # 统计字符串中a出现的次数
print(str.count('a', 1)) # 从1开始查找
print(str.count('a', 1, 3)) # 从1开始查找,查找到3
print("=============================字符串统计=============================")

#   字符串替换
print(str.replace('a', 'A')) # 替换字符串中a为A
print(str.replace('a', 'A', 2)) # 替换字符串中a为A,替换2次
print("=============================字符串替换=============================")

#   字符串分割
print(str.split('e')) # 分割字符串，以e分割
print(str.split('e', 2)) # 分割字符串，以e分割,分割2次
print("=============================字符串分割=============================")

#   字符串大小写转换
print(str.upper())
print(str.lower())
print("=============================字符串大小写转换=============================")

#   字符串首字母大写
print(str.capitalize())
print("=============================字符串首字母大写=============================")

# 字符串居中
print(str.center(30)) # 30宽度，居中
print(str.center(30, '*')) # 居中，以*填充
print("=============================字符串居中=============================")

# 字符串居左
print(str.ljust(30)) # 30宽度，居中
print(str.ljust(30, '*')) # 居中，以*填充
print("=============================字符串居左=============================")   

# 字符串居右
print(str.rjust(30)) # 30宽度，居右
print(str.rjust(30, '*')) # 居右，以*填充
print("=============================字符串居右=============================")

# 字符串判断
print(str.isalnum()) # 判断是否是字母或数字
print(str.isalpha()) # 判断是否是字母
print(str.isdigit()) # 判断是否是数字
print(str.islower()) # 判断是否是小写字母
print(str.isupper()) # 判断是否是大写字母
print(str.istitle()) # 判断是否是首字母大写
print(str.isspace()) # 判断是否是空格
print("=============================字符串判断=============================")
