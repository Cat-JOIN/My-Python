"""
字典(dict): 字典里面的数据是以键值对形式出现，字典数据和数据序列没有关系，即字典不支持下标，后期无论数据如何变化，只需要按照对应的键的名字查找数据即可。
    1. 字典特点:
        - 符号为大括号
        - 数据为键值对形式出现{key: value}
        - 各个键值对之间用逗号隔开
    2. 字典：新增数据
        - 写法：字典序列[key] = 值
        - 如果key存在则修改这个key对应的值；如果key不存在则新增此键值对。
        - 字典为可变类型。

    3. 删：del()/del:删除字典或删除字典中指定键值对。
        - clear(): 清空字典
    4. 改: 写法：字典序列[key] = 值
        - 如果key存在则修改这个key对应的值；如果key不存在则新增此键值对。
    5. 查
        - key值查找，如果当前查找的key存在，则返回对应的值；否则则报错
        - get() 语法：字典序列.get(key, 默认值) 如果当前查找的key不存在则返回第二个参数(默认值)，如果省略第二个参数，则返回None。
        - keys() 查找字典中所有的key，返回可迭代对象
        - values() 查找字典中的所有的value，返回可迭代对象
        - items() 查找字典中所有的键值对，返回可迭代对象，里面的数据是元组，元组数据1是key，元组数据2是value
    6.遍历字典
        - 遍历字典的key
        - 遍历字典的value
        - 遍历字典的键值对





"""
# 符号为大括号、数据为键值对形式出现{key: value}、各个键值对之间用逗号隔开
dict1 = {'name': 'Lucy', 'age': 20, 'gender': '男'}
print(dict1)
print(type(dict1))
# 空字典、注意：一般称冒号前面的为键(key)， 简称k：冒号后面的为值(value)，简称y
dict2 = {}
print(type(dict2))

# 增 字典序列[key] = 值
dict3 = {'name': 'Lucy', 'age': 18, 'gender': '女'}
dict3['phone'] = 123456
print(dict3)
# 对已存在的键值对修改
dict3['name'] = 'QUE'
print(dict3)

# 删除字典del()/del:
# del (dict1)
# print(dict1)

# 删除字典中的键值对
dict4 = {'name': 'Lucy', 'age': 19}
del dict4['name']
print(dict4)

# clear(): 清空字典
dict3.clear()
print(dict3)

# 改
dict3['name'] = 'Lucy'
print(dict3)
dict3['name'] = 'TOM'
print(dict3)


# 查找 key值查找
dict5 = {'name': 'Lucy', 'age': 20, 'gender': '女'}
print(dict5['name'])
# print(dict2['name']) # KeyError 不存在

# 字典序列.get(key, 默认值)
print(dict5.get('name', 'LiCha'))
print(dict5.get('names'))
print(dict5.get('names', 'LiCha'))

# keys() 查找字典中所有的key，返回可迭代对象
print(dict5.keys())

# values() 查找字典中的所有的value，返回可迭代对象
print(dict5.values())

# items() 查找字典中所有的键值对，返回可迭代对象，里面的数据是元组，元组数据1是key，元组数据2是value
print(dict5.items())

# 遍历字典的keys()
for key in dict5.keys():
    print(key)

# 遍历字典的values()
for value in dict5.values():
    print(value)

# 遍历字典的键值对 items()
for item in dict5.items():
    print(item)

# 遍历字典的键值对(拆包)
for key, value in dict5.items():
    print(f'{key} = {value}')