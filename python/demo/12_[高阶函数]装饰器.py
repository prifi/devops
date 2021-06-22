#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@version:
author:fly
@time: 2021/02/19
@file: 12_[高阶函数]装饰器.py
@function:
@modify:
"""

## 装饰器
# 作用：增强函数功能
# 定义：
    # - 把要装饰的方法（函数）作为输入参数；
    # - 在函数体内可以进行任意的操作(可以想象其中会有很多应用场景)；
    # - 只要确保最后return返回一个可执行的函数即可（可以是原来的输入参数函数，也可以是一个新函数）

# 函数即对象，函数对象可以赋值给变量，通过变量可以调用该函数
def now():
    print('2020-02-19')
f = now
f()

# 通过 __name__ 属性可以获取函数名
print(now.__name__)
print(f.__name__)
# 结果：now


# 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator） -- 不改变原函数定义增加功能
# 返回函数的高阶函数 --装饰器
def log(func):
    def wrapper(*args, **kwargs):  # 接收任意参数，增加打印日志功能后，调用原始函数
        print('call %s' % func.__name__)
        return func(*args, **kwargs)
    return wrapper

# @log放到now()函数的定义处，相当于执行了语句：now1 = log(now1)
@log
def now1(n):
    print('2020-02-19, %s' % n)

now1('aaa')
# 结果：
    # call now1
    # 2020-02-19, aaa


# decorator传入参数，需要编写一个返回decorator的高阶函数，比如要自定义log文本：
def log1(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print('%s %s()' % (text, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator

# 和两层嵌套的decorator相比，3层嵌套效果：now2 = log1('execute')(now2)
@log1('execute')
def now2():
    print('2020-02-19')
now2()
# 结果：
    # execute now1()
    # 2020-02-19

print(now1.__name__)
print(now2.__name__)
# 结果：wrapper
# 问题：它们的__name__已经从原来的'now'变成了'wrapper'，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错

# Python内置的functools.wraps可以把原始函数的__name__等属性复制到wrapper()函数中
# 改造以上两个装饰器（log, log1）
import functools
def log2(func):
    @functools.wraps(func)
    def wapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        return func(*args, **kwargs)
    return wapper
@log2
def now2():
    print('2020-02-19')
print(now2.__name__)
# 结果：now2

import functools
def log3(text):
    def decorator(func):
        @functools.wraps(func)
        def wapper(*args, **kwargs):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kwargs)
        return wapper
    return decorator
@log3('execute')
def now3():
    print('2020-02-19')
print(now3.__name__)
# 结果：now3


## 装饰器和装饰器之间是独立的，每次使用装饰器时，被装饰的原有函数对象都会被初始化，例如：decorator装饰器中列表操作
# coding=utf-8
import functools
def deco(func):
    @functools.wraps(func)
    def _deco():
        lst = []
        func(lst)
        print(lst)
    return _deco

@deco
def myfunc(lst):
    lst.append(1)
    return 'ok'
@deco
def yourfunc(lst):
    lst.append(2)
    return 'ok'

myfunc()    # myfunc = deco(myfunc)() 结果：[1]
yourfunc()  # yourfunc = deco(yourfunc)() 结果：[2]


## 练习1：请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
# -*- coding: utf-8 -*-
import time, functools
# time.strftime('%Y-%m-%d %H:%M:%S')
# def metric(fn):
#     print('%s executed in %s ms' % (fn.__name__, 10.24))
#     return fn

def metric(fn):
    @functools.wraps(fn)
    def wapper(*args, **kw):
        a = time.time()
        result = fn(*args, **kw)
        b = time.time()
        c = b - a
        print('%s executed in %s ms' % (fn.__name__, c))
        return result
    return wapper

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print('测试成功')


# 练习2：编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志
import functools
def log(func):
    @functools.wraps(func)
    def wapper(*args, **kwargs):
            print('begin call')
            func(*args, **kwargs)
            print('end call')
            # return None  # 可以return原来的函数，也可以是新函数
    return wapper

@log
def now():
    print('2021')

now()
print(now.__name__)