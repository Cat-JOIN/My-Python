"""
lambda函数：
    1. lambda的应用场景：如果一个函数有一个返回值，并且只有一句代码，可以使用lambda简化。
    2.lambda语法：lambda 参数列表 : 表达式
        - lambda表达式的参数可有可无，函数的参数在lmabda表达式中完全适用。
        - lambda表达式能接受任何数量的参数但只能返回一个表达式的值。

"""
# 需求：函数 返回值100
# 1.函数
def fn1():
    return 100


result = fn1()
print(result)
print(fn1)

# 2. lambda 匿名函数
# lambda 参数列表: 表达式
fn2 = lambda: 200
print(fn2) # lambda 内存地址
print(fn2()) # 100返回值 调用函数

# 需求：计算任意两个数字的累加和

# 1. 函数
def add(a, b):
    return a + b


result = add(1, 2)
print(result)

# 2. lambda
add1 = lambda a, b: a + b
print(add(1, 3))

# lambda 无参数
fn3 = lambda : 100
print(fn3())

# lambda 一个参数
fn4 = lambda a: a
print(fn4("hello"))

# 默认参数
fn5 = lambda a, b, c=100: a + b + c
print(fn5(20, 10))

# 可变参数： *args 这里的可变参数传入到lambda之后，返回值为元组
fn6 = lambda *args: args
print(fn6(100, "hi"))

# 可变参数：**kwargs
fn7 = lambda **kwargs: kwargs
print(fn7(name='lucy', age=19))

# 带判断的lambda
fn8 = lambda a, b: a if a > b else b
print(fn8(100, 50))

# 列表数据按字典key的值排序
students = [
    {'name': 'lucy', 'age': 18, 'gender': '女'},
    {'name': 'TOM', 'age': 19, 'gender': '男'},
    {'name': 'DV', 'age': 20, 'gender': '男'}
]
# sort(key=lambda...,reverse=bool数据
# 1. name key对应的值进行升序排序
students.sort(key=lambda x: x['name'])
print(students)

# 2.name key对应的值进行降序排序
students.sort(key=lambda x: x['name'], reverse=True)
print(students)

# 3. gae key对应的值进行升序排序
students.sort(key=lambda x: x['age'], reverse=False)
print(students)
