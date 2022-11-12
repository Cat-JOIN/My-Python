"""
函数：函数就是讲一段具有独立功能的代码块整合到一个整体并命名，在需要的位置调用这个名称即可完成对应的需求。
    1.函数的作用
        - 函数在开发过程中，可以更高效地实现代码重用。

    2.函数的使用步骤
        2.1不同的需求，参数可有可无。
            - def 函数名(参数):
                代码1
                代码2
                ......
        2.2在Python中，函数必须先定义后使用。
            - 函数名(参数)
            - 如果没有点用函数，函数里面的代码不会执行

    3.函数的参数作用
        - 用户要在调用函数的时候指定具体数字，那么在定义函数的时候就需要接受用户指定的数字。函数调用的时候指定的数字和定义函数时候接受的数字即是函数的参数。
        - 定义函数时同时定义了接受用户数据的参数a和b，a和b时形参
        - 形参：函数定义时书写的参数(非真实数据)
        - 实参：函数调用时书写的参数(真实数据)
            def add_num2(a, b):
                result = a + b
                print(result)
        - 调用函数时传入了真实的数据a 和 b，真实数据为实参
            add_num2(a, b)

    4.函数的返回值作用
        - return -- 返回值作用: 1. 负责函数返回值  2. 退出当前函数：导致return下方的所有代码(函数体内部)不执行
        - def buy():
            return '值'
        - 使用变量保存函数返回值
            goods = buy()
            print(goods)

    5.函数的说明文档也叫函数的文档说明。
        - 定义函数的说明文档
        def 函数名(参数):
            ''' #说明文档的位置 '''
            代码
            ....
        - 查看函数的说明文档
        help(函数名)

        - 定义函数的说明文档(高级使用)
        def sum_num1(a, b):
        '''
        求和函数sum_num1
        :param a: 参数1
        :param b: 参数2
        :return: 返回值
        '''
        return a + b
        - 查看函数的说明文档
        help(sum_num1(1, 2))

    6.函数嵌套
        - 所谓函数嵌套调用指的是一个函数里面又调用了另外一个函数。

"""


# 函数嵌套调用
def testB():
    print('B函数开始')
    print('这是B函数')
    print('B函数结束')


def testA():
    print('A函数开始')
    # 嵌套调用B
    testB()
    print('A函数结束')


testA()


# 打印图形
# 1.打印一条横线
def print_line():
    print('-' * 20)


print_line()


# 打印多条横线
def print_lines(num):
    i = 0
    while i < num:
        print_line()
        i += 1


print_lines(5)


# 三个数求和
def sum_num(a, b, c):
    return a + b + c


result = sum_num(1, 2, 3)


# print(result)

# 求平均值
def average():
    # 先求和 再除3
    sumResult = sum_num(1, 2, 3)
    return sumResult / 3


averageResult = average()
print(averageResult)


# 需求：复现ATM取钱功能。
# 先定义函数、在调用
# 3.封装函数
def sel_func():
    # 2.确定选择功能界面：显示余额 存款 取款
    print('显示余额')
    print('存款')
    print('显示余额')


# 1.搭建整体框架
"""
输入密码登陆后显示功能；查询余额后显示功能；取完钱后显示功能
"""
print('恭喜您登陆成功')
# 显示功能界面
sel_func()

print('您的余额是1000000')
# 显示功能界面
sel_func()

print('取了100元钱')
# 显示功能界面
sel_func()

# 4.在需要的位置调用函数
