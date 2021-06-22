#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@version:
author:fly
@time: 2021/02/20
@file: 18_[面向对象]获取对象信息.py
@function:
@modify:
"""
## 如何知道这个对象是什么类型、有哪些方法呢？

## 1.使用type()
type('123')
type(abs)

type(123) == type(456)    # True
type('abc') == type(123)  # False

# 判断一个函数是否为函数
import types
def fn():
    pass
type(fn) == types.FunctionType  # True
type(abs) == types.BuiltinFunctionType  # True
type(lambda x: x) == types.LambdaType   # True
type((x for x in range(10))) == types.GeneratorType     # True


## 2.使用isinstance()
# - 优先使用isinstance()判断类型
# - 能用type()判断的基本类型也可以用isinstance()判断
isinstance('abc', str)  # True
isinstance([1,2,3,4], (list, tuple))  # True # 或
isinstance((x for x in range(10)), types.GeneratorType)  # True


## 3.使用dir()
# 获得一个对象的所有属性和方法，可以使用dir()函数
dir('abc')

# 使用 getattr()、setattr()以及hasattr() 操作对象的状态：
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()

# 判断是否有属性'x', 'y'？注意是str类型
print(hasattr(obj, 'x'), hasattr(obj, 'y'))  # True False

# 设置属性'y'
# obj.y = 10
setattr(obj, 'y', 10)
print(hasattr(obj, 'y'))  # True

# 获取属性
# print(obj.x)  # 9
print(getattr(obj, 'y'))  # 10

# 试图获取不存在属性，将报错 "AttributeError: 'MyObject' object has no attribute 'z'"
print(getattr(obj, 'z', 404))  # 获取属性'z'，如果不存在，返回默认值404

# 获取对象方法
print(hasattr(obj, 'power'))  # 有属性'power'吗？
print(getattr(obj, 'power'))  # 获取属性'power'
fn = getattr(obj, 'power')    # 获取属性'power'并赋值到变量fn
# print(fn)
fn()    # 调用fn()与调用obj.power()是一样的


# 正确用法示例：
# 判断该fp对象是否存在read方法，如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。
def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None