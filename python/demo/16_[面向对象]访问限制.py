#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@version:
author:fly
@time: 2021/02/20
@file: 16_[面向对象]访问限制.py
@function:
@modify:
"""

## 私有变量（private）以双下划线开头的变量 __name
    # - 只有内部可以访问，外部不能访问
    # - 如果需要获取或修改私有变量，可以给Student类增加 get_gender 和 set_gender 这样的方法
    # - 私有变量可以通过 func._Student__name 获取，但不建议这样做，因为不同的解释器不同
    # - _单下划线变量定义表示，此变量尽量不要外部访问，即使外部可以访问到

class Student(object):

    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):   # 在方法中，可以对参数做检查，避免传入无效的参数
        if not isinstance(gender, int) or gender <= 0 or gender >= 100:
            raise ValueError('bad value')
        self.__gender = gender

lisa = Student('lisa',59)
print(lisa.name)
# print(lisa._Student__gender)

print(lisa.get_gender())
lisa.set_gender(60)
print(lisa.get_gender())

#结果:
# lisa
# 59
# 60