#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@version:
author:fly
@time: 2021/03/02
@file: 21_[面向对象]枚举类.py
@function:
@modify:
"""

## Enum枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例
from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# 直接使用Month.Jan来引用一个常量，或者枚举它的所有成员：
print(Month.Jan)  # Month.Jan
for name, member in Month._member_map_.items():
    print(name, '=>', member, ',', member.value)  # value属性则是自动赋给成员的int常量，默认从1开始计数。
# Jan => Month.Jan , 1
# Feb => Month.Feb , 2
# Mar => Month.Mar , 3
# ...

print('-' * 20)

## 更精确的控制枚举类型，使用Enum派生类
from enum import Enum, unique
# unique 装饰器帮我们检查保证没有重复值
@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon
print(day1)                 # Weekday.Mon
print(Weekday.Tue)          # Weekday.Tue
print(Weekday['Tue'])       # Weekday.Tue
print(Weekday.Tue.value)    # 2
print(day1 == Weekday.Mon)  # True
print(day1 == Weekday.Tue)  # False
print(Weekday(1))           # Weekday.Mon
print(day1 == Weekday(1))   # True
# print(Weekday(7))         # 越界，报错：ValueError: 7 is not a valid Weekday

# 遍历枚举类
for name, member in Weekday.__members__.items():
    print(name, '=>', member, member.value)
# Sun => Weekday.Sun 0
# Mon => Weekday.Mon 1
# Tue => Weekday.Tue 2
# ...



## 练习：把Student的gender属性改造为枚举类型，可以避免使用字符串：
@unique
class Gender(Enum):
    Male = 0
    Famle = 1
print(Gender.Male)

class Student(object):
    def __init__(self, name, Gender):
        self.name = name
        self.gender = Gender

s = Student('Bart', Gender.Male)
print(s.gender)