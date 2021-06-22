#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@version:
author:fly
@time: 2021/02/24
@file: 19_[面向对象]__slots__和@property.py
@function:
@modify:
"""

## 使用__slots
## __slots__ 限制class实例允许添加的属性

## 实例和类动态绑定属性
# 创建class，可以动态绑定属性和方法
class Student(object):
    pass

# 绑定属性
s = Student()
s.name = 'Michael'

# （给实例）绑定方法
def set_age(self, age):
    self.age = age
from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)  # 25

# 给一个实例绑定的方法，对另一个实例是不起作用：
s2 = Student()
# s2.set_age(25)  #报错： AttributeError: 'Student' object has no attribute 'set_age'

# 使所有实例都绑定方法，则需要给class绑定方法：
def set_score(self, score):
    self.score = score
Student.set_score = set_score

# 给class绑定方法后，所有实例均可调用：
s.set_score(100)
print(s.score)   # 100
s2.set_score(99)
print(s2.score)  # 99


## 使用__slots__
# 只允许对Student绑定name和age属性：
class Student1(object):
    __slots__ = ('name', 'age')
s3 = Student1()
s3.name = 'Xiao'
# s3.score = 99  #报错：AttributeError: 'Student1' object has no attribute 'score'

# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
class GraduateStudent(Student1):
    __slots__ = ('grade',)  # 此时子类允许绑定的属性为('name', 'age', 'grade')，注意是元祖形式
g = GraduateStudent()
g.name = 'Xiao1'
g.grade = 'man'
# g.score = 99  #报错：AttributeError: 'GraduateStudent' object has no attribute 'score'


## 总结：使用 __slots__ 限制class实例添加的属性。
    # 1.__slots__ 定义的属性仅对当前类实例起作用，对继承的子类不起作用；
    # 2.如果要在子类中起作用，需要在子类中定义 __slots__ ，子类允许定义属性等于: 自身__slots__ + 父类__slots__；





## 使用@property
## @property作用把一个方法变成属性调用

class Screen(object):

    @property
    def width(self):
        return self._width

    '''
    只读属性，仅定义get方法，不定义set方法
    '''
    @property
    def hight(self):
        return self._hight

    '''
    @property本身又创建了另一个装饰器@width.setter，把一个setter方法变成属性赋值
    '''
    @width.setter
    def width(self, value):
        if not isinstance(value,int):
            raise ValueError('width must be an integer!')
        self._width = value

s = Screen()
s.width = 1     # 实际转化为s.set_width(1)
s.width         # 实际转发为s.get_score()


## 总结：
    # 1.精简代码，保证对参数进行检查，减少出错。