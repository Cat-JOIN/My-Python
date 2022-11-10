"""
    运算符： 描述  支持的容器类型
      +     合并  字符串、列表、元组
      *     复制  字符串、列表、元组
      in    元素是否存在  字符串、列表、元组、字典
      not in 元素是否不存在  字符串、列表、元组、字典

    - len(): 计算容器中元素个数
    - del或del(): 删除
    - max(): 返回元素中最大值
    - min(): 返回元素中最小值
    - range(start, end, stop): 生成从star到end的数据，步长为step，供for循环使用
    - enumerate(): 函数用于将一个可便利的数据对象(如列表、元组或字符串)组合

容器类型转换
    - tuple(): 将某个序列转换成元组
    - list(): 将某个序列转换成列表
    - set(): 将某个序列转换成集合
"""

new_str = "Lucy"
new_str1 = "TOM"
new_list = ['Lucy', 'TOM', 'DEV']
new_list1 = ['lucy', 'tom', 'dev']
new_tuple = (10, 20, 30)
new_tuple1 = (100, 200, 300)
new_dict = {'name': 'Lucy', 'age': 20, 'gender': '女'}
new_dict1 = {'name': 'TOM', 'age': 20, 'gender': '男'}
# +：合并
print(new_str + new_str1)
print(new_list + new_list1)
print(new_tuple + new_tuple1)
# print(new_dict + new_dict1) # 报错 合并不支持字典

# *：复制
print(new_str * 2)
print(new_list * 2)
print(new_tuple * 2)

# in: 判断数据是否在里面
print('Lucy' in new_str)
print('Lucy' in new_str1)

print('TOM' in new_list)

print('TOM' in new_list1)

print(10 in new_tuple)
print(10 in new_tuple1)

print('name' in new_dict)

# not in: 判断数据是否不存在里面
print('Lucy' not in new_str)
print('lucy' not in new_str)

print('TOM' not in new_list)
print('lucy' not in new_list)

print('name' not in new_dict)

# len(): 统计数据
print(len(new_str))
print(len(new_dict))
print(len(new_tuple))

del new_str1
# print(new_str1)

del(new_list[1])
print(new_list)

print(max(new_tuple))
print(min(new_tuple))

# range():  range()生成的序列不包含end数字。
for i in range(1, 10, 1):
    print(i)

for i in range(1, 10, 2):
    print(i)

for i in range(10):
    print(i)

# enumerate(): 语法：enumerate(可遍历对象, start=0)
# 注意： start参数用来设置遍历数据的下标的起始值，默认为0
for i in enumerate(new_list):
    print(i)

# tuple(): 将某个序列转换成元组
print(tuple(new_list))
print(new_list)

# list(): 将某个序列转换成列表
print(list(new_str))
print(new_str)

# set(): 将某个序列转换成集合
print(set(new_list))