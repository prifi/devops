#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@version:
author:fly
@time: 2021/02/20
@file: 15_[面向对象]类和实例.py
@function:
@modify:
"""

## 面向对象
# - 数据封装、继承和多态是面向对象的三大特点


## 类和实例
# - 面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的模板，比如Student类，而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。

# 定义类使用class关键字：
class Student(object):
    pass

# 创建实例是通过类名+()实现的：
bart = Student()

# 给实例bart绑定一个name属性：
bart.name = 'Bart Simpson'
print(bart.name)

# 类可以起到模板的作用，创建实例时，可以将必须绑定的属性强制写进去，通过特殊的 __init__ 方法，把 name, score 等属性绑上去
class Student1(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

# self 执行实例本身，将属性绑定到self上
# 有了 __init__ 方法创建实例时不能传入空参数，必须传入与__init__方法匹配的参数
bart1 = Student1('Bart Simpson', 59)
print(bart1.name)

# 总结：类的方法和普通函数没有什么区别，仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。



## 数据封装
# 封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法
# 数据和逻辑被“封装”起来了，调用很容易，但却不用知道内部实现的细节
class Student2(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
lisa = Student2('Lisa', 99)
bart2 = Student2('Bart', 59)
print(lisa.name, lisa.get_grade())
print(bart2.name, bart2.get_grade())