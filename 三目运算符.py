"""
三目运算符
    - 三目运算符也叫三元运算符或三元表达式
    - 语法：条件成立执行的表达式 if 条件 else 条件不成立执行的表达式

"""

num1 = 99
num2 = 100
# 执行条件成立执行的表达式
new_number = num2 - num1 if num2 > num1 else num2 + num1
print(new_number)

# 执行条件不成立执行的表达式
new_number = num2 - num1 if num2 < num1 else num2 + num1
print(new_number)

