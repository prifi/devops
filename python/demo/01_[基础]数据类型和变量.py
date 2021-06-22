#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@version:
author:xiaopengfei
@time: 2021/01/24
@file: 01_[基础]数据类型和变量.py
@function:
@modify:
"""

## 输入输出
print('hello world')
print('100 + 200 = ', 100 + 200)

# 输出打印
# name = input()
# print(name)


## 数据类型
# 包括：整数、浮点数、字符串、布尔值、空值、变量、常量

# 字符串
# 转义
print('I\'m \"OK\"!')  # I'm "OK"

# r'xx' 表示默认不转义
print(r'\\\t')  # \\\t

# ''' 打印多行内容, 加 r''' 表示默认不转义\n会原样输出
print(r''' \n
line1
line2
''')

# 布尔值 True False
# and or not
print(5 > 3 and 3 > 1)  # True

# 空值 None or 0
# None不能理解为 0
print(None)

# 变量
# 大小写英文（大小写敏感）、数字和_的组合，且不能用数字开头
a = 'low'
A = 'high'
print(a, A) # low high

# 常量
    # 在Python中，通常用全部大写的变量名表示常量
PI = 3.1415926
print("除法运算： ",10 / 3)          # 3.3333333333333335
print("板除运算（取整）：", 10 // 3)  # 3
print("余数运算（取余）：", 10 % 3)   # 1  # 无论整数做//除法还是取余数，结果永远是整数 10 % 3 = 9 .. 1