#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@version:
author:fly
@time: 2021/01/29
@file: 08_[高阶特性]切片和迭代.py
@function:
@modify:
"""

## 1.切片

## list切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# L[0:3] # = L[:3] # 左闭右开，不包含 3
# L[1:3]
print(L[-2:])   # ['Bob', 'Jack'] 包含最后结尾
print(L[-2:-1]) # ['Bob'], 不包含 -1（倒数最后是-1）

# 生成列表
L1 = list(range(100))
# L1[:10]       # 取前10内，不包含10
# L1[-10:]      # 包含最后一个值：99
# L1[10:20]
# L1[:10:2]     # [0, 2, 4, 6, 8] 每隔2位取值
# L1[::5]       # 每隔5位
# L1[:]         # 原样复制一个list

## set切片
# (1,2,3,4,5)[:3]  # (1, 2, 3) set切片仍是set

## 字符串切片
s = 'abcdefg'
print(s[:3])    # 'abc' 字符串切片仍然是字符串


## 练习1：利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法
def trim(s):
    if s[:1] == ' ':
        return trim(s[1:])   # 使用到了递归函数
    elif s[-1:] == ' ':
        return trim(s[:-1])
    else:
        return s
print(trim('   hello world   '))  # hello world 前后无空格



## 2.跌代
# 判断一个对象是否是可迭代对象
from collections.abc import Iterable
isinstance('abc', Iterable)     # True  str是否可迭代
isinstance([1,2,3], Iterable)   # True  list是否可迭代
isinstance(123, Iterable)       # False 整数是否可迭代

# list实现下标循环
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
# === 输出 ===
# 0 A
# 1 B
# 2 C

# for循环同时引用两个变量
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
# === 输出 ===
# 1 1
# 2 4
# 3 9

## 练习：使用迭代查找一个list中最小和最大值，并返回一个tuple
def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    a = L[0] # 1
    b = L[0] # 1
    for x in L:
        while a > x: # 1 > 34
            a = x
        while b < x: # 2 < 34
            b = x
    return (a, b)

print(findMinAndMax([1,2,34,4,22]))  # (1, 34)



## 3.列表生成式
# 生成 [1x1, 2x2, 3x3 ...] 结果集合
L = []
for x in range(1, 11):
    L.append(x * x)
# === 等同于 ===
L1 = [x * x for x in range(1,11)]   # 列表生成式

# 加判断
L2 = [x for x in range(1,11) if x % 2 == 0]  # [2, 4, 6, 8, 10]

# 两层循环
L3 = [m + n for m in 'ABC' for n in 'XYZ']   # ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

# 列出当前目录下所有目录和文件
import os
L4 = [d for d in os.listdir('.')]

# 遍历字典k,v
d = {'x': 'A', 'y': 'B', 'z': 'C' }
# for i,j in d.items():
#     print(i,j, end=' ')
# print()
L5 = [k + '=' + v for k,v in d.items()]

# 将字符串大写变小写
L6 = ['Aaa', 'Bbb', 'Ccc']
[s.lower() for s in L6]  # ['aaa', 'bbb', 'ccc']

# 列表生成式加else 注意else位置
# L7 = [x for x in range(1,11) if x % 2 == 0 else -x]  # 错误
L7 = [x if x % 2 == 0 else -x for x in range(1,11)]    # 正确  [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]

# 练习：排除数字将英文转成小写
L_temp = ['Hello', 'World', 18, 'Apple', None]
L8 = [s.lower() for s in L_temp if isinstance(s, str)]
print(L8)  # ['hello', 'world', 'apple']



## 4.生成器
# 在Python中，这种一边循环一边计算的机制，称为生成器：generator
g = (x * x for x in range(10))
print(g)
print(next(g))
print(next(g))
# === 输出 ===
# <generator object <genexpr> at 0x7f2625d4db30>
# 0
# 1
# 越界：抛出StopIteration的错误

# 使用for循环迭代生成器
for x in g:
    print(x)

# 使用生成器生成：斐波拉契数列（Fibonacci）
def fib(max):
    n, a, b, = 0, 0, 1
    while n < max:
        # print(b)
        yield b         # 变成generator
        a, b = b, a+b
        n += 1
    return 'done'

# 在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
g1 = fib(5)
while True:
    try:
        x = next(g1)
        print('g:',x)
    except StopIteration as e:   # 捕获异常拿到return返回值
        print('Generator turn value: ', e.value)
        break
# === 输出 ===
# g: 1
# g: 1
# g: 2
# g: 3
# g: 5
# Generator turn value:  done

## 练习：打印杨辉三角
def triangles():
    L=[1]
    while True:
        yield L[:]
        L.insert(0,0) # L [0, 1, 1]
        L.append(0)   # L [0, 1, 1, 0]
        L = [L[i] + L[i+1] for i in range(len(L)) if i+1<len(L)]  # i:0,1,2, 3 | len(L) 4 | 0+1 1 1+1 2 1+0 1

n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 5:
        break
for t in results:
    print(t)
# === 输出 ===
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]


## 4.迭代器
# 被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
# 可迭代对象Iterable不一定是迭代器，Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算
from collections.abc import Iterable,Iterator
isinstance([], Iterable)   # True
isinstance([], Iterator)   # False

# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：
isinstance(iter([]), Iterable)  # True


# for循环本质上就是通过不断调用next()函数实现
for x in range(1,5):
    pass

# 首先获得Iterator对象:
it = iter(range(5))
# 循环
while True:
    try:
        # 获取下一个值
        x = next(it)
    except StopIteration:
        # 遇到StopIteration退出循环
        break