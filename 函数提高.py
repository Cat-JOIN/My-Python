"""
函数：
    1.变量作用域：变量作用域指的是变量生效的范围，主要分为两类：局部变量和全局变量。
        1.1 局部变量：所谓局部变量是定义在函数体内的变量，即只在函数体内部生效。
            - 局部变量的作用：在函数内部，临时保存数据，即当函数调用完成后，则销毁局部变量。
        1.2 全局变量：所谓全局变量，指的是在函数体内、外都能生效的变量。
            - global 关键字声明a是全局变量

    2.多函数程序执行流程
        - 函数、变量的执行流程是从上往下执行

    3.函数的返回值
        - 返回值作用参数传递
        - return a, b写法，返回多个数据的时候，默认是元组类型。
        - return后面可以连接列表、元组或字典，以返回多个值。

    4.函数的参数
        4.1 位置参数：调用函数时根据函数定义的参数位置来传递参数。
            - 传递和定义参数的顺序及个数必须一致。
        4.2 关键字参数：函数调用，通过"键=值"形式加以指定。可以让函数更加清晰、容易使用，同时也清除了参数的顺序需求。
            - 函数调用时，如果有位置参数时，位置参数必须在关键字参数的前面，但关键字参数之间不存在先后顺序。
        4.3 缺省参数: 缺省参数也叫默认参数，用于定义函数，为参数提供默认值，调用函数时可不传该默认的值
            - 注意：所有位置参数必须出现在默认参数前，包括函数定义和调用。
            - 函数调用时，如果为缺省参数传值则修改默认参数值；否则使用这个默认值。
        4.4 不定长参数：不定长参数也叫可变参数，用于不确定调用的时候会传递多少个参数(不传参也可以)的场景。此时，可用包裹(packing)位置参数，或者包裹关键字，来进行参数传递，会显得非常方便。
            - 包裹位置传递 -- 传进的所有参数都会被args变量收集，它会根据传进参数的位置合并为一个元组(tuple), args是元组类型，这就是包裹位置传递。
            - 包裹关键字传递
            - 无论是包裹位置传递还是包裹关键字传递，都是一个组包的过程。

    5.拆包和交换两个变量的值
        5.1 拆包
            - 拆包：元组
            - 拆包：字典
        5.2 交换变量值
            - 借助第三 变量存储数据

    6.引用：在Python中，值是靠引用来传递的。
        - 我们可以用id()来判断两个变量是否为同一个值的引用。我们可以将id值理解为那块内存的地址标识。
        - 引用当做实参

    7.可变和不可变类型: 所谓可变类型与不可变类型是指：数据能够直接进行修改，如果能直接修改那么就是可变，否则是不可变。
        - 可变类型
            - 列表(list)
            - 字典(dict)
            - 集合(set)
        - 不可变类型
            - 整形(int)
            - 浮点型(float)
            - 字符串(str)
            - 元组(tuple)

"""


# 定义一个函数，声明一个变量：函数体内部访问、函数体外面访问。
def test1():
    a = 100
    print(a)


test1()
# print(a) # 报错：a变量是局部变量，外部无法访问

# 定义全局变量
b = 1000


def test2():
    print(b)


def test3():
    global b  # 关键字声明b是全局变量
    b = 2000
    print(b)


test2()
test3()
print(b)  # 变量已被修改


# 返回值作为参数传递
def test4():
    return 50


def test5(num):
    print(num)


# 保存函数test4的返回值
result = test4()

# 将函数返回值所在变量作为参数传递到test5函数
test5(result)


# return多个返回值写法
def num1():
    # return 1, 2 #int数值
    # return [10, 20, 30] #列表
    # return (100, 200, 300) # 元组
    return {'name': 'Lucy'}  # 字典


result1 = num1()
print(result1)


# 位置参数: 调用函数时根据函数定义的参数位置来传递参数。
def user_info(name, age, gender):
    print(f'您的姓名是{name},年龄是{age}, 性别是{gender}')


user_info('Lucy', 18, '女')


# user_info('Lucy', '女', 18) # 顺序不一致不报错，但语义没意义
# user_info('Lucy', 18) # 报错：传递和定义参数的顺序及个数必须一致。


def user_info1(name, age, gender):
    print(f'您的姓名是{name},年龄是{age}, 性别是{gender}')


user_info1('TOM', 20, gender='男')
user_info1('小明', gender='男', age=16)


# 函数调用时，如果有位置参数时，位置参数必须在关键字参数的前面，但关键字参数之间不存在先后顺序。
# user_info1(age=17, gender='男', 'TOM')

# 缺省参数
def user_info2(name, age=17, gender='女'):
    print(f'您的姓名是{name},年龄是{age}, 性别是{gender}')


user_info2('lucy')
user_info2('lucy', age=19)
user_info2('lucy', age=18, gender='女')
# user_info2(age=18, gender='女', 'lucy') 报错


# 包裹位置传递
def user_info3(*args):
    print(args)


# ('TOM')
user_info3('TOM')
user_info3('Lucy', 18)


def user_info4(**kwargs):
    print(kwargs)


# {'name': 'TOM', 'age': 19, 'id': 9527}
user_info4(name='TOM', age=19, id=9527)


# 拆包：元组
def return_num():
    return 100, 200


num1, num2 = return_num()
print(num1)
print(num2)


# 拆包：字典
dict1 = {'name': 'Lucy', 'age': 18, 'gender': '女'}
a, b, c = dict1
# 对字典进行拆包，取出来的是字典的key
print(a)
print(b)
print(c)
# 取value值
print(dict1[a])
print(dict1[b])
print(dict1[c])

# 交换变量的值
"""
方法1
    1.1 定义中间的第三变量，为了临时存储a或b的数据
    1.2 把a的数据存储到c，做保存
    1.3 把b的数据赋值到a, a = 20
    1.4 把c的数据赋值到b, b = 10
"""
a = 10
b = 20

c = 0
c = a
a = b
b = c
print(a)
print(b)
# 方法2
a, b = 1, 2
a, b = b, a

print(a)
print(b)

# 数据引用传递
a = 1
b = a
print(a)
print(b)
print(id(a))
print(id(b))

# 可变数据类型:列表 传递方式引用
aa = [10, 20]
bb = aa
print(bb)
print(id(aa))
print(id(bb))

aa.append(30)
print(aa)
print(bb)  # 列表是可变类型
print(id(aa))
print(id(bb))


# 引用当做实参
def test7(a):
    print(a)
    print(id(a))

    a += a
    print(a)
    print(id(a))

b = 100
test7(b)

c = [1000, 2000]
test7(c)