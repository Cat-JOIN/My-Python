"""
创建集合：创建集合使用{}或set(), 但是如果要创建空集合只能使用set(),因为{}用来创建空字典。
    1. 增加数据
        - add(): 因为集合有去重功能，所以，当向集合内追加的数据是当前集合已有数据的话，则不进行任何操作。
        - update(): 追加的数据是序列。
    2. 删除数据
        - remove(): 删除集合中的指定数据，如果数据不存在则报错
        - discard(): 删除集合中的指定数据，如果数据不存在也不会报错
        - pop(): 随即删除集合中的某个数据，并返回这个数据。
    3. 查找数 据
        - in: 判断数据在集合序列
        - not in: 判断数据不在集合序列


"""

# 集合
s1 = {10, 20, 30, 40}
print(s1)
print(type(s1))

s2 = set('hello')
print(type(s2))

# 空集合
s3 = set()
print(type(s3))
# 空字典
s4 = {}
print(type(s4))

# add()
s1.add(100)
print(s1)
# 去重
s1.add(10)
print(s1)

# s1.update(100)
s1.update([100, 200])
print(s1)
s1.update('aa')
print(s1)

# remove(): 删除集合中的指定数据，如果数据不存在则报错
s1.remove(100)
print(s1)
# s1.remove(1000)
# print(s1) # 报错

# discard(): 删除集合中的指定数据，如果数据不存在也不会报错
s1.discard(10)
print(s1)

# pop(): 随即删除集合中的某个数据，并返回这个数据。
del_num = s1.pop()
print(del_num)
print(s1)

# in: 判断数据在集合序列
print(20 in s1)
print(10 in s1)

# not in: 判断数据不在集合序列
print(10 not in s1)
print(30 not in s1)