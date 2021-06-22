#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@version:
author:fly
@time: 2021/02/19
@file: 11_[高阶函数]匿名函数.py
@function:
@modify:
"""

## 传入函数时不需要显式定义函数，使用匿名函数
# - 限制：冒号前表示参数，冒号后只能有一个表达式，不需要return返回值为该表达式结果

list(map(lambda x: x * x, range(1,5)))
# 结果：[1, 4, 9, 16]

# lambda等同于：
def f(x):
    return x * x

# - 匿名函数赋值给一个变量，再利用变量来调用该函数：
f = lambda x: x * x
f(5)
# 结果：25

# - 匿名函数作为返回值返回：
def build(x, y):
    return lambda: x * x + y * y
f1 = build(1,2)  # 返回匿名函数对象：<function build.<locals>.<lambda> at 0x7fe7b67ff820>
f1()  # 执行匿名函数
# 结果：5

## 练习：匿名函数改造下面的代码：
def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))

list(filter(lambda n: n % 2 ==1, range(1,10)))
# 结果：[1, 3, 5, 7, 9]