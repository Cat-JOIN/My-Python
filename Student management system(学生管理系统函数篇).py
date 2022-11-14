# 系统简介
"""
需求：进入系统显示系统功能界面
    1.添加学员
        1.1 接受用户输入学员信息，并保持
        1.2 判断是否添加学员信息
            1.2.1 如果学员姓名已存在，则报错提示
            1.2.2 如果学员姓名不存在，则准备空字典，将用户输入的数据追加到字典数据
        1.3 对应的if条件成立的位置调用该函数

    2.删除学员
        2.1 用户输入目标的学员姓名进行删除
        2.2 检查这个学员是否存在
             2.2.1 如果存在，则列表删除这个数据
             2.2.2 如果不存在，则提示”该用户不存在“
        2.3 对应的if条件成立的位置调用该函数

    3.修改学员信息
        3.1 用户输入目标学员姓名
        3.2 检查这个学员是否存在
            3.2.1 如果存在，则修改这位学员的信息，例如手机号
            3.2.2 如果不存在，则报错
        3.3 对应的if条件成立的位置调用该函数

    4.查询学员信息
        4.1 用户输入目标学员姓名
        4.2 检查学员是否存在
            4.2.1 如果存在，则显示这个学员的信息
            4.2.2 如果不存在，则报错提示
        4.3 对应的if条件成立的位置调用该函数

    5.显示所有学员信息
    6.退出系统
"""
# 步骤分析
"""
1.显示功能界面
2.用户输入功能序号
3.根据用户输入的功能序号，执行不同的功能(函数)
    3.1 定义函数
    3.2 调用函数
"""


# 定义函数print_info, 负责显示系统功能
def print_info():
    print('1. 添加学员')
    print('2. 删除学员')
    print('3.修改学员信息')
    print('4.查询学员信息')
    print('5.显示所有学员信息')
    print('6.退出系统')
    print('-' * 20)


# 等待用户存储信息
info = []


def add_info():
    """ 添加学员信息"""
    # 学号、姓名、手机号
    new_id = input('请输入学号: ')
    new_name = input('请输入姓名: ')
    new_phone = input('请输入手机号: ')
    # 判断用户是否存在
    global info
    # 不允许姓名重复：判断用户输入的姓名 和 列表里面字典的name对应的值 相等提示
    for i in info:
        if new_name == i['name']:
            print('此用户已存在')
            return
    # 存储用户数据
    user_dict = {}
    
    # 字典新增数据
    user_dict['id'] = new_id
    user_dict['name'] = new_name
    user_dict['phone'] = new_phone

    # 列表追加数据
    info.append(user_dict)
    print(info)


def del_info():
    """删除函数"""
    # 用户输入删除的名字
    del_name = input('请输入您要删除的名字：')

    global info
    # 检查学员是否存在
    for i in info:
        if del_name == i['name']:
            info.remove(i)
            print('学员存在，已删除')
            break
    else:
        print('学员不存在')
    print(info)


# 修改
def modify_info():
    """修改函数"""
    # 学员输入要修改学员的信息
    modify_name = input('请输入您要修改的学员的名字进行验证:')

    global info
    # 检查这个学员是否存在
    for i in info:
        if modify_name == i['name']:
            print('用户存在')
            # 用户输入要修改信息的选项
            new_modify = input('请输入您要修改的手机号: ')
            i['phone'] = new_modify
            print('修改成功')

    print(info)


# 查询学员信息
def search_info():
    """查询函数"""
    # 学员输入姓名验证
    search_name = input('请输入要查找的姓名：')
    global info
    # 判断学员是否存在
    for i in info:
        if search_name == i['name']:
            print('用户存在' + '-' * 20)
            print(f"您要查找学员的学号{i['id']},姓名{i['name']},手机号{i['phone']}")
            break
    else:
        print('该学员不存在')


# 显示所有学员信息
def print_all():
    """显示所有学员函数"""
    print('学号\t姓名\t手机号')
    for i in info:
        print(f"{i['id']}\t{i['name']}\t{i['phone']}")


#
# 系统要循环使用，直到用户退出系统
while True:
    # 显示功能界面
    print_info()

    # 2. 用户输入功能序号
    user_num = int(input('请输入功能序号：'))

    # 3. 按照用户输入的功能序号，执行不同的功能(函数)
    # 如果用户输入1. 执行添加学员,.......
    if user_num == 1:
        add_info()
    elif user_num == 2:
        del_info()
    elif user_num == 3:
        modify_info()
    elif user_num == 4:
        search_info()
    elif user_num == 5:
        print_all()
    elif user_num == 6:
        # 程序要结束--终止while True 循环 --break
        exif_flag = input('确定要退出吗？yes or no: ')
        if exif_flag == 'yes':
            break
    else:
        print('您输入的序号有误')
