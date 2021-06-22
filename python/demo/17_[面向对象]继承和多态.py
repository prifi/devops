#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@version:
author:fly
@time: 2021/02/20
@file: 17_[面向对象]继承和多态.py
@function:
@modify:
"""

## 继承与多态
# - 类class可以被继承，新的class称为子类，被继承的class称为基类、父类或超类（Base class, Super class）

class Animal(object):
    def run(self):
        print('Animal is running...')


## 子类直接继承父类 run() 方法，获得了父类的全部功能：
# class Dog(Animal):
#     pass
#
# class Cat(Animal):
#     pass
#
# dog = Dog()
# dog.run()
#
# cat = Cat()
# cat.run()
#
# 结果：
# Animal is running...
# Animal is running...


## 子类与父类有相同方法时，子类的run()覆盖了父类的run()，这样就获得了继承的另一个好处：多态
class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

dog = Dog()
dog.run()

cat = Cat()
cat.run()

# 结果：
# Dog is running...
# Cat is running...


## 定义一个class，实际上就是定义了一种数据类型，与python自带的数据类型比如str、list、dict没什么两样。
a = list()
b = Animal()
c = Dog()
print(isinstance(a, list))    # True  # a是list类型
print(isinstance(b, Animal))  # True  # b是Animal类型
print(isinstance(c, Dog))     # True  # c是Dog类型

## 子类属于父类，但父类不属于子类
print(isinstance(c, Animal))  # True
print(isinstance(b, Dog))     # False


## 由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法，这就是多态的意思：
def run_twice(animal):
    animal.run()
    animal.run()

print(run_twice(Animal()))
print(run_twice(Dog()))

## 鸭子类型 “file-like object”
# 并不一定要求子类继承Animal类，只要内部有 run() 方法都可以被传入
class Timer(object):
    def run(self):
        print('Start...')

print(run_twice(Timer()))


## 总结：
    # - 继承可以把父类的所有功能都直接拿过来，这样就不必从零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。
    # - 动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。