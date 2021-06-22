#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@version:
author:xiaopengfei
@time: 2021/01/24
@file: 07_[函数]函数参数.py
@function:
@modify:
"""

## 位置参数、默认参数、可变参数和关键字参数（命名关键字参数）

# 1.位置参数
# 计算x的n次方
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(2,16))


# 2.默认参数
# 默认参数规则：
    # 必选参数在前，可选参数在后
    # 设置默认参数时，变化大大在前，变化小的在后
    # 当不按顺序提供部分默认参数时，需要把参数名写上
    # 默认参数必须指向不变对象!!!

# 默认计算2次方，只需传入一个参数
def power1(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power1(5))
print(power1(2,8))

def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

enroll('小明','M',18)
enroll('小明','M',city='TAIWAN')  # 当不按顺序提供部分默认参数时，需要把参数名写上


## 3.可变参数
# 定义：Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n
    return sum
num = (1, 2, 3)
print(calc(*num))


## 4.关键字参数
# 定义：关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict

def person(name, age, **kw):
    print('name:', name)
    print('age:', age)
    print('other:', kw)
    # for i in kw.items():
    #     print(i)

person('Prifi', 18, city='beijing', gender='M')
# name: Prifi
# age: 18
# other: {'city': 'beijing', 'gender': 'M'}

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Prifi', 18, city=extra['city'], job=extra['job'])  # 更简单的写法如下 **extra
person('Prifi', 18, **extra)   # **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数


## 5.命名关键字参数
# 在函数内部通过kw检查参数
def person1(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

# 限制命名关键字参数，只接收city和job作为关键字参数，*后面的参数被视为命名关键字参数
def person2(name, age, *, city, job):
    print(name, age, city, job)
# person2('Prifi', 18, city='ShenZhen', job='IT')
# person2('Prifi',19, city='SZ')         # 不传命名关键字参数则报错：missing 1 required keyword-only argument: 'job'
person2('Prifi', 18, city='', job='IT')  # Prifi 18  IT

# 如果函数定义中已经有了一个可变参数，后面的命名关键字不需要特殊的*号
def person3(name, age, *args, city, job):
    print(name, age, args, city, job)
list=[1,2,3]
person3('zhangs', 20, *list, city='SZ', job='') # zhangs 20 (1, 2, 3) SZ # job不传则为空

def person(name, age, city, job):
    # 缺少 *，city和job被视为位置参数
    pass


## 参数组合
    # 数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
# a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)
# a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}


# 练习：允许计算两个数的乘积，可接收一个或多个数并计算乘积：
def product(x,*args):
    # if len(args) < 1:
    #     raise TypeError('give one argument')
    sum = 1
    sum = sum * x
    for n in args:
        if not isinstance(n, int):
            raise TypeError('bad operand type')
        else:
            sum = sum * n
    print(sum)
    return sum

# ======= 测试 =========
# product()

if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')