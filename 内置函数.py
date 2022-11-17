"""
前置函数:
    - abs()函数可以完成对数字求绝对值计算。
    - round()函数可以完成对数字的四舍五入计算。
    - 需求：任意两个数字，按照指定要求整理数字后再进行求和
    计算。
高阶函数：把函数作为参数传入，这样的函数称为高阶函数，高阶函数是函数式编程的体现。函数式编程就是指这种高度抽象的编程范式。
    - map(func, lst): 将传入的函数变量func作用到lst变量的每个元素中，并将结果组成新的列表(Python2)/迭代器(Python3)返回
    - reduce(func, lst),其中func必须有两个参数。每次func计算的结果继续和序列的下一个元素做累积计算。reduce()传入的参数func必须接受2个参数
    - filter(func, lst)函数用于过滤序列，过滤掉不符合条件的元素，返回一个filter对象。如果要转换为列表，可以使用list()来转换。

"""
# abs(): 绝对值
print(abs(-10))

# round(): 四舍五入
print(round(1.3))
print(round(1.9))

# 高阶函数 需求：任意两个数字，按照指定要求整理后再进行求和计算。
# 方法1
def add_num(a, b):
    return abs(a) + abs(b)


result = add_num(-1, 2)
print(result)

# 方法2 任意两个数字，先进行数字处理(绝对值或四舍五入)再求和计算
def add_num2(a, b, f):
    return f(a) + f(b)


result1 = add_num2(-1, 5, abs)
print(result1)
result1 = add_num2(1.4, 1.7, round)
print(result1)
# 两种方法对比之后，发现，方法2的代码会更加简洁，函数灵活性更高。
# 函数式变成大量使用函数，减少了代码的重复，因此程序比较短，开发速度较快。

# 需求：计算list1序列中各个数字的2次方。
list1= [1, 2, 3, 4, 5]

def func(x):
    return x ** 2


result2 = map(func, list1)
print(result2)
print(list(result2))
print(type(result2))

# reduce(func, lst)
import functools
def func(a, b):
    return a + b


result3 = functools.reduce(func, list1)
print(result3)

# filter(func, lst): 过滤
list2 = []
for i in range(1, 11):
    list2.append(i)

def func(x):
    return x % 2 == 0


result4 = filter(func, list2)
print(result4)
print(list(result4))
