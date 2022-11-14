"""
列表:
    1. 引用场景、变量存储、列表一次性可以存储多个数据, 且可以为不同数据类型。
    2. 列表格式： 1[数据1, 数据2, 数据3, 数据4.....]
    3. 列表的常用操作 列表的作用是一次性存储多个数据，程序员可以对这些数据进行的操作有：增、删、改、查。
        3.1 查找
            3.1.1 下标
            3.1.2 函数
                - index(): 返回指定数据所在位置的下标。语法：列表序列.index(数据, 开始位置下标, 结束位置下标)
                - count(): 统计指定数据在当前列表中出现的次数。
                - len(): 访问列表长度，即列表中数据的个数。
            3.1.3 判断数据是否存在
                - in: 判断指定数据在某个列表序列，如果在返回True，否则返回False
                - not in: 判断指定数据不在某个列表序列，如果不在返回True, 否则返回False.
        3.2 增加：增加指定数据到列表中。
            3.2.1 append(): 列表结尾追加数据。
                - 语法： 列表序列.append(数据)
            3.2.2 extend(): 列表结尾追加数据，如果数据是一个序列，则将这个序列的数据逐一添加到列表。
                - 语法：列表序列.extend(数据)
            3.2.3 insert(): 指定位置新增数据。
                - 语法：列表序列.insert(位置下标, 数据)
        3.3 删除
            3.3.1 del
                - 语法：del 目标
            3.3.2 pop() 删除指定下标的数据，如果不指定下标，默认删除最后一个数据，无论是按照下表还是删除最后一个，pop函数都会返回这个被删除的数据
            3.3.3 remove(数据) -- 移除列表中某个数据的第一个匹配项
            3.3.4 clear() -- 清空列表
        3.4 修改
            - 修改指定下标数据
            - 逆置：reverse()
            - 排序：sort() -- 语法：列表序列.sort(key=None, reverse=False) 注：reverse表示排序规则，reverse = True降序， reverse = False升序(默认)
        3.5 复制
            - 函数：copy()
    4. 列表的循环遍历
        4.1 while循环遍历列表
        4.2 for循环遍历列表
    5. 列表嵌套 -- 所谓列表嵌套指的就是一个列表里面包含了其它的子列表








"""
# 下标
name_list = ["Lucy", "TOM", "DOM"]
print(name_list[0])
print(name_list[1])
# 查找函数
# index(): 返回指定数据所在位置的下标。语法：列表序列.index(数据, 开始位置下标, 结束位置下标)
print(name_list.index('Lucy'))
# print(name_list.index('Lucy', 1)) # 如果数据没有在列表，则报错

# count(): 统计指定数据在当前列表中出现的次数。
print(name_list.count('Lucy'))

# len(): 访问列表长度，即列表中数据的个数。语法：len(列表序列)
print(len(name_list))

# - in: 判断指定数据在某个列表序列，如果在返回True，否则返回False
print('Lucy' in name_list)
print('T' in name_list)

# not in: 判断指定数据不在某个列表序列，如果不在返回True, 否则返回False.
print("Lucy" not in name_list)
print("T" not in name_list)

# 判断用户是否存在
# name = input('请输入您要查找的用户名：')
# if name in name_list:
#     print(f"您好，用户{name}存在")
# else:
#     print(f"您好，用户{name}不存在")

# 增加
# append(): 列表结尾追加数据。
name_list.append("OBT")
print(name_list)
# 列表追加数据的时候，直接在原列表里面追加了指定数据，即修改了原列表，故列表为可变类型。

# extend(): 列表结尾追加数据，如果数据是一个序列，则将这个序列的数据逐一添加到列表。
name_list.extend('xiaoming')
print(name_list)
name_list.extend(['10', '20'])
print(name_list)

# insert(): 指定位置新增数据。
name_list.insert(0, 'Join')
print(name_list)

# 删除
# 语法： del 目标
# 删除列表
name_list1 = ['10', '20']
del name_list1
# print(name_list1) # 已删除，文件不存在打印报错
# 删除指定数据
del name_list[0]
print(name_list)

# pop():
new_del = name_list.pop(1)
print(new_del)
print(name_list)

# remove(数据)
name_list.remove('OBT')
print(name_list)

# clear() -- 清空
name_list.clear()
print(name_list)

# 修改指定下标的数据
new_list2 = ["Lucy", "TOM", "DEV"]
new_list2[2] = 'aaa'
print(new_list2)

# 逆置 reverse()
num_list = [1, 2, 3, 4, 5]

num_list.reverse()
print(num_list)

# sort(): 排序：升序 和 降序
num_list1 = [1, 2, 3, 4, 5]
num_list1.sort(reverse=False)
print(num_list1)
num_list1.sort(reverse=True)
print(num_list1)

# 复制 函数：copy()
new_list3 = num_list1.copy()
print(new_list3)


# 列表的循环遍历
# while循环遍历列表
new_list_1 = ['Lucy', 'TOM', 'DEV']

i = 0
while i < len(new_list_1):
    print(new_list_1[i])
    i += 1

# 遍历循环 -- for
for i in new_list_1:
    # 遍历序列中的数据
    print(i)

# 列表嵌套
new_demo = [['Tom', 'Lucy', 'DEV'], ['ty', 'tt', 'op'], ['aa', 'bb', 'cc']]
print(new_demo)

# 列表嵌套的时候的数据查询
print(new_demo[0])
print(new_demo[0][1])


# 需求：8位老师，3个办公室， 将8位老师随机分配到3个办公室
"""
步骤：
    1.准备数据
        1.1 8位老师 -- 列表
        1.2 3个办公室
        
    2.分配老师到办公室
        *** 随机分配
        就是把老师的名字写入到办公室列表 -- 办公室列表追加老师名字数据
        
    3.验证是否分配成功
        打印办公室详细信息：每个办公室的人数和对应的老师名字
"""

import random

# 准备数据
teachers = ["钟老师", "李老师", "杨老师", "王老师", "张老师", "夏老师", "叶老师", "吴老师"]
offices = [[], [], []]

# 分配老师到办公室
for name in teachers:
    # 列表追加数据 -- append(数据) -- extend() -- insert()
    # xx[0] -- 不能指定是具体某个下标 -- 随机
    num = random.randint(0, 2)
    offices[num].append(name)
print(offices)
