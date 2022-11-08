"""
for循环：
    1. 语法：
        for 临时变量 in 序列:
            重复执行的代码1
            重复执行的代码2
            .....
        2. break 和 continue: 循环中满足一定条件退出循环的两种不同的方式
            - break控制循环流程，即终止循环。
            - continue控制循环流程，即退出当前一次循环继而执行下一次循环代码。


"""

# for循环打印123456
num1 = str(123456)
for i in num1:
    print(i)

# break的使用
for i in num1:
    # 当某些条件成立退出终止 -- break： 条件i字符
    if i == '4':
        print('到4，终止打印')
        break
    print(i)
else:
    print('打印结束')

# continue

for i in num1:
    # 当某些条件成立退出终止 -- break： 条件i字符
    if i == '4':
        print('碰到4，跳过打印')
        continue
    print(i)
else:
    print('打印结束')

