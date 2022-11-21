"""
推导式：简化代码
    1. 列表推导式: 让代码更简洁、少量。
        - 作用：用一个表达式创建一个有规律的列表或控制一个有规律列表。
        - 列表推导式又叫列表生成式。
        - 带if列表推导式
    2. 字典推导式: 快速合并列表为字典或提取字典中目标数据。
        总结：
            1. 如果两个列表数据个数相同，len统计任何一个列表的长度都可以
            2.如果两个列表数据个数相同，len统计数据多的列表数据个数会报错，len统计数据少的列表个数不会报错
    3. 集合推导式
        集合有去重功能
    

"""

# 列表推导式
# while循环的实现 (原始)

list1 = []

i = 0
while i < 10:
    list1.append(i)
    i += 1


print(list1)

# for循环的实现(原始)
list2 = []
for i in range(10):
    list2.append(i)


print(list2)

# 列表推导式for
list3 = [i for i in range(10)]
print(list3)

# 需求：0-10偶数数据的列表
# 原始实现
new_list4_ = []
for i in range(0, 10):
    if i % 2 == 0:
        new_list4_.append(i)


print(new_list4_)
# 带if列表推导式
list4 = [i for i in range(0, 10, 2)]
print(list4)
# 或 这种
new_list4 = [i for i in range(10) if i % 2 == 0]
print(new_list4)

# 多个for循环实现列表推导式
# 原始实现方法，代码量多
list5 = []
for i in range(1, 3):
    for j in range(0, 3):
        list5.append((i, j))

print(list5)

# 列表推导式添加数据
new_list5 = [(i, j) for i in range(1, 3) for j in range(3)]
print(new_list5)

# 字典推导式：
# 创建字典 key是1-5的数字，v是这个数字的平方
dict1 = {i: i ** 2 for i in range(1, 5)}
print(dict1)

# 合并两个字典的数据
list6 = ['name', 'age', 'gender', 'id']
list7 = ['Lucy', 20, '女']
dict2 = {list6[i]: list7[i] for i in range(len(list7))}
print(dict2)
# 总结：1. 如果两个列表数据个数相同，len统计任何一个列表的长度都可以
# 2.如果两个列表数据个数相同，len统计数据多的列表数据个数会报错，len统计数据少的列表个数不会报错

# 提取字典中目标的信息
counts = {'Map': 200, 'HP': 199, 'XI': 188, 'WX': 201, 'YY': 300}
# 需求：提取上述v:为200以上的值
count1 = {key: value for key, value in counts.items() if value >= 200}
print(count1)

list8 = [1, 1, 2]
set1 = {i ** 2 for i in list8}
print(set1)

# 嵌套推导式
list9 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
list10 = [[[row[i] for row in list9] for i in range(4)]
print(list10)
"""
总结：
    1.列表推导式
    [xx for xx in range()]
    2.字典推导式
    {xx1: xx2 for ... in ...}
    3.集合推导式
    {xx for xx in ...}
"""
