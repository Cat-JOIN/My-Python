"""
认识字符串：字符串是Python中最常用的数据类型。我们一般使用引号来创建字符串。创建字符串很简单，只要用变量分配一个值即可。
    - 字符串特征；单引号、双引号、三 引号
    - 字符串输出print()
    - 字符串输入input()
"""
# 单引号
a = 'hello'
print(a)
print(type(a))

# 双引号
b = "TOM"
print(b)
print(type(b))

# 三 引号
c = """Lucy"""
print(c)
print(type(c))

"""
下标：又叫“索引”，就是编号。下标的作用就是通过下标快速找到对应的数据。
切片：切片是指对操作的对象截取其中一部分的操作。字符串、列表、元组都支持切片操作。
    - 语法：序列[开始位置下标: 结束位置下标: 步长]
    1. 不包括结束位置下标对应的数据，正负整数均可。
    2. 步长是选取间隔，正负整数均可，默认步长为1。
字符串：字符串的常用操作方法有查找、修改和判断三大类。
    1. 查找 -- 所谓字符串查找方法即是查找子串在字符串中的位置或出现的次数。
        1.1 find(): 检测某个子串是否包含这个字符串中，如果在返回这个子串开始的位置下标，否则则返回-1
            - 语法：字符串序列.find(子串, 开始位置下标, 结束位置下标)
            - rfind(): 和find()功能相同，但查找方向为"右侧"开始
        1.2 index(): 检测某个子串是否包含在这个字符串中，如果在返回这个子串开始的位置下标，否则则报异常。
            - 字符串序列.index(子串, 开始位置下标, 结束位置下标)
            - rindex():和index()功能相同，但查找方向为"右侧"开始
        1.3 .count(): 返回某个子串在字符串中出现的次数。
            - 字符串序列.count(子串, 开始位置下标, 结束位置下标)
    2. 修改： 所谓的修改字符串，指的就是通过函数的形式修改字符串中的数据。
        2.1 replace(): 替换
            - 语法：字符串序列.replace(旧子串, 新子串, 替换次数)
            - 替换次数如果查出子串出现次数，则替换次数为该子串出现次数。
            - 数据按照是否能直接修改分为“可变类型”和"不可变类型"两种，字符串类型的数据修改的时候不能改变原有字符串，不能改变原有字符串，属于不能直接修改数据的类型即是不可变类型。
        2.2 split(): 按照指定字符分割字符串
            - 语法：字符串序列.split(分割字符, num)
            - num表示的是分割字符出现的次数，即将来返回数据个数为num+1个
            - 如果分割字符是原有字符串中的字符，分割后则丢失该子串。
        2.3 join(): 用一个字符或子串合并字符串，即是将多个字符串合并为一个新的字符串
            - 语法：字符串或子串.join(多字符串组成的序列)
    3. 转换大小写
        3.1 capitalize(): 将字符串第一个字符转换成大写
            - 语法：序列.capitalize()
            - capitalize()函数转换后，只字符串第一个字符大写，其他的字符全都小写。
        3.2 title(): 将字符串每个单词首字母转换成大写。
        3.3 lower(): 将字符串中大写转小写。
        3.4 upper(): 将字符串中小写转大写。
    4. 删除
        - lstrip(): 删除字符串左侧空白字符。
        - rstrip(): 删除字符串右侧空白字符。
        - strip(): 删除字符串两侧空白字符。
    5. 对齐
        5.1. ljust(): 返回一个原字符串左对齐，并使用指定字符(默认空格)填充至对应长度的新字符串。
            - 语法：字符串序列.ljust(长度, 填充字符)
        5.2. rjust(): 返回一个原字符串右对齐，并使用指定字符(默认空格)填充至对应长度的字符串，语法和ljust()相同。
        5.3 center(): 返回一个原字符串居中对齐,并使用指定字符(默认空格)填充至对应长度的新字符串，语法和ljust()相同。
    6. 判断：所谓判断即是判断真假，返回的结果是布尔型数据类型: True 或 False。
        6.1 startswith(): 检查字符串是否已指定字串开头，是则返回True，否则返回False。如果设置开始和结束位置下标，则在指定范围内检查。
            - 语法: 字符串序列.startswith(子串，开始位置下标, 结束位置下标)
        6.2 endswith(): 检查字符串是否是以指定子串结尾，是则返回True，否则返回False。如果未设置开头和结束位置下标，则在指定范围内检查。
            - 语法: 字符串序列.endswitth(子串，开始位置下标, 结束位置下标)
        6.3 isalpha(): 如果字符串至少有一个字符并且所有字符都是字母返回True，否则返回False
        6.4 isdigit(): 如果字符串只包含数字则返回True否则返回False。
        6.5 isalnum(): 如果字符串至少有一个字符并且所有字符都是字母或数字则返回True，否则返回False。
        6.6 isspace(): 如果字符串中只包含空白，则返回True，否则返回False。
        



"""

# 下标： str1[下标]
str1 = "Python"
print(str1)
print(str1[0])
print(str1[1])

# 切片 序列名[开始位置的下标: 结束位置的下标: 步长]
str2 = '012345678'
print(str2)
print(str2[2: 5: 1])
print(str2[0: 10: 2])
print(str2[0: 10: 3])
print(str2[1: 10]) # 补偿不写默认为1
print(str2[:6]) # 开始不写默认为0
print(str2[2:]) # 结束不写默认选取到最后
print(str2[::-1]) # 负数步长，选取倒叙开始
print(str2[-4:-1])

# 字符串查找 find()
str3 = "hello world and itcast and itheima and Python"
print(str3.find('and')) # 查到位置12
# 查下标
print(str3[12])
print(str3.find('and', 13, 30))
print(str3.find('ands')) # 子串不存在返回-1
# 字符串: .rfind()
print(str3.rfind("and"))

# 字符串: .index()
print(str3.index('and'))
print(str3.index('and', 15, 30))
# print(str3.index("inde")) # 子串不存在则报错

# 字符串: .rindex()
print(str3.rindex('and'))

# 字符串: .count()
print(str3.count("and"))
print(str3.count("and", 15, 40))
print(str3.count("ands", 15, 40)) # 如果子串不存在返回0

# 替换：replace():
print(str3.replace("and", "or", 1))
print(str3.replace("and", "or", 2))
print(str3.replace("ands", "or", 1)) # 如果子串不存在修改无效
new_str = str3.replace("and", "or", 1) # 修改后的子串需要一个新的变量接受，原有的变量不会改变，说明字符串是不可修改类型，可变类型可直接修改
print(new_str)

# .split(): 分割，返回一个列表
list1 = str3.split('and')
print(list1)
list1 = str3.split('and', 1)
print(list1)

# join(): 合并列表里面的字符串数据为一个大字符串
mylist = ["aa", "bb", "cc"]
new_str = '***'.join(mylist)
print(new_str)


# 转换大小写：capitalize(): 将字符串第一个字符转换成大写
print(str3.capitalize())
# title(): 将字符串每个单词首字母转换成大写。
new_str = str3.title()
print(new_str)
# lower(): 将字符串中大写转小写。
print(new_str.lower())
# upper(): 将字符串中小写转大写。
print(str3.upper())

mystr = "   hello world and itcast and itheima and python    "
print(mystr)
# lstrip(): 删除字符串左侧空白字符。
print(mystr.lstrip())
# rstrip(): 删除字符串右侧空白字符。
print(mystr.rstrip())
# strip(): 删除字符串两侧空白字符。
print(mystr.strip())

# 字符串序列.ljust(长度, 填充字符)
str4 = 'hello'
print(str4.ljust(10, '.'))

# 字符串序列.rjust(长度, 填充字符)
print(str4.rjust(10, '*'))
# 字符串序列.center(长度, 填充字符)
print(str4.center(10, '&'))


# startswith():
print(str3.startswith("hello"))
print(str3.startswith("and"))
print(str3.startswith("and", 12, 40))

# endswith(): 判断字符串是否以某个子串结尾
print(str3.endswith("Python"))
print(str3.endswith("python"))
print(str3.endswith("Python", 39))
print(str3.find('Python'))