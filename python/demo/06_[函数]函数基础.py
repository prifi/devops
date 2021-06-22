#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@version:
author:xiaopengfei
@time: 2021/01/24
@file: 06_[函数]函数基础.py
@function:
@modify:
"""

## 内置函数
abs(-2)         # 求绝对值
max(1,2,45,-2)  # 求最大值
min(1,2,3,-5)   # 求最小值


## 定义函数
    # 函数遇到return返回，执行完毕
    # 函数没有return，默认返回return None, return None可以简写为return

def myabs(x):
    # 参数判断
    # if type(x) != int:
    #     print('error')
    #     exit(1)
    # 参数类型判断，返回类型错误
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x > 0:
        return x
    else:
        return -x
print(myabs(-3.5))


# 空函数
def nop():
    pass # 占位符，让程序先运行起来


# 返回多个值
    # Python的函数返回多值其实就是返回一个tuple
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x,y)  # 151.96152422706632 70.0

r = move(100, 100, 60, math.pi / 6)  # 函数多值返回tuple
print(type(r))  # <class 'tuple'>