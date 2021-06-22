#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@version:
author:fly
@time: 2021/02/18
@file: 10_[高阶函数]返回函数.py
@function:
@modify:
"""

## 把函数作为结果值返回

# 返回求和函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for i in args:  # 内部函数sum可以引用外部函数lazy_sum的参数和局部变量
            ax += i
        return ax
    return sum
f = lazy_sum(1,3,5,7)
print(f)   # 结果：<function lazy_sum.<locals>.sum at 0x7f19013f8940>
f()        # 真正执行求和函数，结果: 16


# 每次调用都会返回一个新的函数,f1()和f2()的调用结果互不影响。
# >>> f1 = lazy_sum(1, 3, 5, 7, 9)
# >>> f2 = lazy_sum(1, 3, 5, 7, 9)
# >>> f1==f2
# 结果：False


# 闭包（Closure）:相关参数和变量都保存在返回的函数中
def count():
    fs = []
    for i in range(1,4): # i=3
        def f():
            return i*i
        fs.append(f) # 三个函数返回时，i此时为3
    return fs
f1,f2,f3 = count()
print(f1(),f2(),f3())
#结果： 9 9 9

# 返回函数不要引用任何循环变量，或者后续会发生变化的变量。
# 如果一定要绑定，需要再创建一个函数，用该函数绑定循环变量当前值
def count1():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f4,f5,f6 = count1()
print(f4(),f5(),f6())
#结果：1 4 9


## 练习：利用闭包返回一个计数器函数，每次调用它返回递增整数

# 方法1：使用nonlocal
def createCounter():
    '''
    nonlocal关键字用来在函数或其他作用域中使用外层(非全局)变量。
    '''
    n = 0
    def counter():
        nonlocal n
        n += 1
        return n
    return counter

# 方法2：使用len()方法
def createCounter():
    L = []
    def counter():
        L.append(1)
        return len(L)
    return counter

# 方法3：使用生成器
def createCounter():
    def g():
        n = 0
        while True:
            n += 1
            yield n
    x = g()
    def counter():
        return next(x)
    return counter

# 方法4：利用list
def createCounter():
    l = [0]
    def counter():
        l[0] += 1
        return l[0]
    return counter

## 测试结果：
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
