"""
循环：
    1.1 循环的作用：让代码更高效的重复执行。
    1.2循环的分类
        while循环 和 for循环

while循环：
    1.while的语法
        while 条件:
            条件成立重复执行的代码1
            条件成立重复执行的代码2
            ......
    2. break 和 continue: 循环中满足一定条件退出循环的两种不同的方式
            - break控制循环流程，即终止循环。
        - continue控制循环流程，即退出当前一次循环继而执行下一次循环代码。
    3. while循环嵌套
        while 条件1:
            条件1成立执行的代码
            ......
            while 条件2:
                条件2成立执行的代码
                .....


"""

# 需求：抽奖要一枚硬币，假设盒子里有20个物品号码球，其中6个号码是娃娃、10个号码是谢谢惠顾、4个号码是Iphone14 Pro Max
# 物品分配的数字(娃娃(1,4,7,9,13,17), 谢谢惠顾(3,5,8,10,12,13,14,15,16,18,0), Iphone14 Pro Max(2，6，11，19))
# 每抽完一次又把号码放回盒子中，手中有5枚硬币，抽5次随机数

# 导入随机数模块
import random
# 硬币
num1 = 5

while (num1 <= 5) and (num1 >= 1):
    # 定义所有物品(随机数)
    new_id = random.randint(0, 19)
    if new_id == (1 or 4 or 7 or 9 or 13 or 17):
        print(f'恭喜您抽中娃娃,幸运数字是{new_id}')
    elif new_id == (2 or 6 or 11 or 19):
        print(f'恭喜您抽中Iphone14 Pro Max,幸运数字是{new_id}')
    else:
        print(f'谢谢惠顾，您抽到的数字是{new_id}')
    num1 -= 1


print(f'您手中的硬币：{num1},没硬币了，充值再来吧！')


# break的使用终止循环：喝热水，每天喝2升开水，喝够了就不喝了(单位ml)
num1 = 500
while num1 <= 2000:
    if num1 == 2000:
        print(f'今天喝了{num1}ml水，够了不喝了')
        break
    print(f'喝了{num1}ml水')
    num1 += 500

# continue的使用退出当前一次循环继而执行下一次循环代码：吃苹果，吃到第六个苹果有虫子，换一个吃
i = 1
while i <= 10:
    if i == 6:
        print(f'吃到第{i}个苹果，有虫子，换一个吃')
        i += 1
        continue
    print(f'吃到{i}个苹果')
    i += 1


# while 嵌套循环使用
i = 1
while i <= 10:
    j = 1
    while j <= 5:
        j += 1
        print(f'j当前数字{j}')
    i += 1
    print(f'i当前的数字{i}')

