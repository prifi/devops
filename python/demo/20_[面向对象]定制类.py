#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@version:
author:fly
@time: 2021/03/02
@file: 20_[面向对象]定制类.py
@function:
@modify:
"""

## 定制类

## __str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串(用于调试)
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__  # __repr__ 和 __str__ 一样，偷懒写法

print(Student('xiaom'))
s = Student('xiaom')
print(s)



## __iter__ 返回迭代对象，可使用__next__循环获取下一个值
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始两个计数器a,b
    def __iter__(self):
        return self  # 实例本身迭代对象，返回自己
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b   # 计算下一个值
        if self.a > 100: #  退出循环条件
            raise StopIteration
        return self.a    # 返回下一个值

# 将Fib实例作用于for循环
for n in Fib():
    print(n,end=', ')



## __getitem__ 通过下标取出元素
class Fib1(object):
    def __getitem__(self, item):
        a, b = 1, 1
        for x in range(item):
            a, b = b, a + b
        return a
f = Fib1()
print('')
print(f[1])  # 1

# __getitem__ 支持切片[:5], [5:7]
class Fib2(object):
    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
f1 = Fib2()
print(f1[:5])
print(f1[5:7])



## __getattr__返回不存在的类方法或属性不报错
class Student1(object):
    def __init__(self):
        self.name = 'Xiaom'
    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

s1 = Student1()
print(s1.name)
print(s1.score)  # 99 # 没有score属性时，尝试调用__getattr__(self, 'score')来尝试获得属性
print(s1.age())
# print(s1.gender)  # 获取不存在属性时默认返回None，需要按照约定返回：AttributeError: 'Student' object has no attribute 'gender'



## __call__ 在实例本身调用类方法
class Student2(object):
    def __init__(self, name):
        self.name = name
    def __call__(self, *args, **kwargs):
        print('Hello %s' % self.name)
s2 = Student2('Xiaom')
print(s2())  # Hello Xiaom # self参数不需要传入



## 通过callable()函数判断是否是可调用对象
print(callable(Student1))   # True
print(callable(Student1())) # False
print(callable((max)))      # True
print(callable(None))       # False
print(callable('str'))      # False