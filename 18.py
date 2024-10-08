# 集合的基本操作
# 集合不能存储重复的元素
# 集合的创建
s = set() # 创建一个空的集合
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)
print(s) # {1, 2, 3, 4}

print(len(s)) # 4

print(1 in s)
print(5 in s)
print(4 in s)
print("===========================这是集合的创建===========================")

# 集合的增删
s = {1, 2, 3, 4, 5}
s.add(6)
s.remove(3)
print(s)
print("===========================这是集合的增删===========================")

# 集合的交集、并集、差集、对称差集
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
print(s1 & s2) # {4, 5}，与intersection()区别在于不改变s1和s2本身
print(s1.intersection(s2)) # {4, 5}，与&的区别在于会改变s1和s2本身
print(s1 | s2) # {1, 2, 3, 4, 5, 6, 7, 8}
print(s1.union(s2)) # {1, 2, 3, 4, 5, 6, 7, 8}
print(s1 - s2) # 差集表示s1中有而s2中没有的元素
print(s1.difference(s2))
print(s2 - s1) # 差集表示s2中有而s1中没有的元素
print(s2.difference(s1)) 
print(s1 ^ s2) # 对称差集表示s1中有而s2中没有的元素，或者s2中有而s1中没有的元素
print(s1.symmetric_difference(s2))
print("===========================这是集合的交集 并集 差集 对称差集===========================")

# 集合的子集、超集、相等集
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
print(s1 <= s2) # False
print(s1 < s2) # False
print(s1 >= s2) # False
print(s1 > s2) # False
print(s1 == s2) # False
print("===========================这是集合的子集 超集 相等集===========================")

