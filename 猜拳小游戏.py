"""
需求：
    1. 出拳
        玩家: 手动输入
        电脑：1.固定：剪刀；2. 随机
    2.判断输赢
        2.1 玩家获胜
        2.2 平局
        2.3 电脑获胜

让电脑出拳随机
    - 导入模块
    import random
    - 使用这个模块的功能
    random.randint()
"""
import random
# 1. 出拳 注：出拳只用0，1，2
# 玩家
player = int(input('请出拳：0--石头；1--剪刀；2--布: '))
# 电脑
computer = random.randint(0, 2)
# 判断输赢；玩家能赢得结果都列出来
if ((player == 0) and (computer == 1)) or ((player == 1) and (computer == 2)) or ((player == 2) and (computer == 0)):
    print(f'玩家出拳{player},电脑出拳{computer},玩家获胜')
# 平局
elif player == computer:
    print(f'玩家出拳{player},电脑出拳{computer},平局')
else:
    print(f'玩家出拳{player},电脑出拳{computer},电脑获胜')