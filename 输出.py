"""
输出:作用：程序输出内容给用户
1. 格式化输出：所谓的格式化输出即按照一定的格式输出内容。
    1.1 格式化符合
        - %s -- 转换 -- 字符串
        - %d -- 转换 -- 有符号的十进制整数
        - %f -- 转换 -- 浮点数
    1.2 技巧
        - %06d,表示输出的整数显示位数，不足以0补全，超出当前位数原样输出
        - %.2f, 表示小数点后显示的小数位数

    1.3 格式化字符串除了%s,还可以写为f'{表达式}'

    1.4 转义字符
        - \n:换行。
        - \t:制表符，一个tab键(4个空格)的距离。
    1.5 结束符
        - 在Python中，print(),默认自带end="\n"这个换行结束符，所以导致两个print直接会换行展示，用户可以按需求你更改结束符。



"""

"""
1. 准备数据
2.格式化符号输出数据
"""
age = 18
name = 'TOM'
weight = 75.5
stu_id = 1
stu_id2 = 1000

# 1. 今年我的年龄是x岁 -- 整数 %d
print('今年我的年龄是%d' % age)

# 2.我的名字是x -- 字符串 %s
print('我的名字是%s' % name)

# 3. 我的体重是x公斤
print('我的体重是%f公斤' % weight)

# 4. 我的学号是x
print('我的学号是%d' % stu_id)

# 4.1 我的学号是001
print('我的学号是%03d' % stu_id)
print('我的学号是%03d' % stu_id2)

# 5.我的名字是x，今年%d岁了
print('我的名字是%s，今年%d岁了' % (name, age))
# 5.1我的名字是x，明年%d岁了
print('我的名字是%s，今年%d岁了' % (name, age + 1))

# 6.我的名字是x，今年x岁了，体重x公斤，学号是x
print('我的名字是%s，今年%d岁了，体重%.2f公斤，学号是%.6d' % (name, age, weight, stu_id ))

# 语法 f'{表达式}'
# f-格式化字符串是Python3.6中新增的格式化方法，该方法更简单易读。
print(f'我的名字是{name}，今年{age}岁了')

# 转义字符
print('hello Python')
# \n:换行。
print('hello\nPython')

print('您好！')
# \t:制表符，一个tab键(4个空格)的距离。
print('\t您好！')

# 在Python中，print(),默认自带end="\n"这个换行结束符，所以导致两个print直接会换行展示，用户可以按需求你更改结束符。
print('hello', end="\n")
print('world', end="\t")
print(end="\n")
print('hello', end="...")
print('Python')
