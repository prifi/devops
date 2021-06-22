#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@version:
author:fly
@time: 2021/02/19
@file: 13_[高阶函数]偏函数.py
@function:
@modify:
"""

## 偏函数（Partial function）
# 意义：当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。

int('10010', base=2) # str转int，转换成二进制 base=10/16 转换位十/十六进制

def int2(x, base=2):
    '''
    默认转为二进制
    '''
    return int(x, base)

int2('10010')
# 结果: 18


# 创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
import functools
int22 = functools.partial(int, base=2)  # base也可以为其他值：10,16
int22('10010')
# 结果：18


# 创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数:
int22 = functools.partial(int, base=2)
# 相当于：
kw = {'base':2}
int('10010', **kw)

max2 = functools.partial(max, 10)
max2(5, 6, 7)
# 相当于：
args = (10, 5, 6, 7)  # 把10作为*args的一部分自动加到左边
max(*args)