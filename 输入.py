"""
1. 输入 在Python中，程序接受用户输入的数据的功能即是输入。
2. 输入的语法
    - input("提示信息")
3. 输入的特点
    - 当程序执行到input,等待用户输入，输入完成之后才继续向下执行。
    - 在Python中，input接受用户输入后，一般存储变量，方便使用。
    - 在Python中，input会把接收到的任意输入的数据都当做字符串处理。
4. 数据类型的转换
    int(x, [base]) 将x转换为一个整数
    float(x) 将x转换为一个浮点数
    complex(real, [imag]) 创建一个复数，real为实部，imag为虚数
    str(x) 将对象x转换为字符串
    repr(x) 将对象x转换为表达式字符串
    eval(str) 用来计算在字符串中的有效Python表达式，并返回一个对象
    tuple(s) 将序列s转换为一个元组
    list(s) 将序列s转换为一个列表
    chr(x) 将一个整数转换为一个Unicode字符
    ord(x) 将一个字符串转换为它的ASCII整数值
    hex(x) 将一个整数转换为一个十六进制字符串

5. 运算符的分类
    5.1 算术运算符
        + 加 1 + 1输出结果为2
        - 减 1 - 1输出结果为0
        * 乘 2 * 2输出结果为4
        / 除 10 / 2输出结果为5
        // 整除 9 // 4输出结果为2
        % 取余 9 % 4输出结果为1
        ** 指数 2 ** 4输出结果为16, 即 2*2*2*2
        () 小括号 小括号用来提高运算优先级， 即(1+2) *3输出结果为9
        注意：混合运算优先级顺序：()高于 ** 高于 * / // % 高于+ -

    5.2 赋值运算符  将 = 右侧的结果赋值给等号左侧的变量
        5.2.1 单个变量赋值
        5.2.2 多个变量赋值
        5.2.3 多变量赋相同值

    5.3 复合赋值运算符 先算复合运算符值右边的表达式： 算复合赋值运算
        += 加法赋值运算符 c += a 等价于 c = c + a
        -= 减法赋值运算符 c -= a 等价于 c = c - a
        *= 乘法赋值运算符 c *= a 等价于 c = c * a
        /= 除法法赋值运算符 c /= a 等价于 c = c / a
        //= 整除法赋值运算符 c //= a 等价于 c = c // a
        %= 取余赋值运算符 c %= a 等价于 c = c % a
        **= 幂赋值运算符 c **= a 等价于 c = c ** a

    5.4 比较运算符
        == 判断相等。如果两个操作数的结果相等，则条件结果为真(True)，否则条件结果为假(False)。
        != 不等于。如果两个操作数的结果不相等，则条件为真(True)，否则条件结果为假(False)。
        > 运算符左侧操作数结果是否大于右侧操作数结果，如果大于，则条件为则真，否则为假。
        < 运算符左侧操作数结果是否小于右侧操作数结果，如果小于，则条件为则真，否则为假。
        >= 运算符左侧操作数结果是否大于等于右侧操作数结果，如果大于，则条件为真，否则为假。
        <= 运算符左侧操作数结果是否小于等于右侧操作数结果，如果小于，则条件为真，否则为假。

    5.5 逻辑运算符
        and x and y 布尔“与”：如果x为False，x and y 返回False，否则它返回y的值。
        or x or y 布尔“或”：如果x是True，否则它返回y的值
        not not x 布尔“非”：如果x为True，返回False。如果x为False，它返回True。


"""

"""
1. 书写input
    input("提示信息")
    
2. 观察特点
    2.1 遇到input，等待用户输入
    2.2 接受input存变量
    2.3 input接收到的数据类型都是字符串
"""
 password = input('请输入您的密码：')
 print(f"您输入的密码是{password}")

 print(type(password))
  # 转换为int(x) -- 整型
 print(type(int(password)))


# float() -- 将数据转换为浮点型
num1 = 1
str1 = '10'
print(num1)
print(type(num1))
print(type(float(num1)))
print(type(str1))
print(type(float(str1)))

# str() -- 将数据转换为字符串
print(type(str(num1)))

# tuple() -- 将一个序列转为成为元组
list1 = [10, 20, 30]
print(tuple(list1))

# list() -- 将一个序列转换为列表
t1 = (100, 200, 300)
print(list(t1))

# eval() -- 计算在字符串中的有效Python表达式，并返回一个对象
str2 = '1'
str3 = '1.1'
str4 = '(1000, 2000, 3000)'
str5 = '[1000, 2000, 3000]'
print(type(eval(str2)))
print(type(eval(str3)))
print(type(eval(str4)))
print(type(eval(str5)))

# 单个变量赋值
a = 1
print(a)

# 多个变量赋值
a, b, c = 1, 2, 3
print(a, b, c)

# 多变量赋相同的值
d = e = 10
print(d)
print(e)

# += 加法赋值运算符
a = 10
a += 1 # a = a + 1
print(a)

# -= 减法赋值运算符
b = 10
b -= 1 # b = b - 1
print(b)

# *= 乘法赋值运算符
c = 3
c *= 3 # c = c * 3
print(c)

# /= 除法赋值运算符
d = 9
d /= 3 # d = d / 3
print(d)
print(type(d))
print(int(d))

# //= 整除法赋值运算符
e = 9
e //= 2 # e = e // 2
print(e)

# %= 取余赋值运算符
f = 9
f %= 2 # f = f % 2 取余1
print(f)

# **= 幂赋值运算符
j = 3
j **= 2 # j = 3 * 3 二次方
print(j)

# == 判断相等。
a = 10
print(a == 10)
print(a == 9)
if a == 10:
    print(f'{a} 等于{a}为True')
else:
    print(f'{a} 不等于12 为False')

# != 不相等
print(a != 10)
print(a != 9)
if a != 9:
    print(f'{a} 不等于9，Ture')
else:
    print(f'{a}等于{a}为False')

# >
print(a > 9)
print(a > 10)
if a > 9:
    print(f'{a} 大于 9 ，为True' )
else:
    print(f'{a} 大于 {a} ，为False')

# <
print(a < 9)
print(a < 11)
if a < 12:
    print(f'{a} 小于 12 ，为True' )
else:
    print(f'{a} 小于 9 ，为False')

# >=
print(a >= 10)
print(a >= 11)
if a >= 12:
    print(f'{a} >= {a} 为True')
else:
    print(f'{a} >= 12 为假')

# <=
print(a <= 10)
print(a <= 9)
if a <= 10:
    print(f'{a} <= 11 为True')
else:
    print(f'{a} <= 9,为False')

a = 0
b = 1
c = 2
# 1. and: 与：都真才真
print((a < b) and (c > b))
print((a < b) and (b > c))

# 2. or: 或：一真则真，都假才假
print((a < b) or (b < c))
print((a > b) or (b < c))
print((a > b) or (b > c))

# not: 非：取反
print(not False)
print(not True)
print(not (a > b))

