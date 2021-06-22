#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@version:
author:fly
@time: 2021/03/04
@file: 26_[IO编程]序列化.py
@function:
@modify:
"""


## 序列化与反序列化

## 1.pickle

import pickle
d = dict(name='Bob', age=20, score=88)

# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
print(pickle.dumps(d))
# 结果：b'\x80\x04\x95$\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x04name\x94\x8c\x03Bob\x94\x8c\x03age\x94K\x14\x8c\x05score\x94KXu.'

# 或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

# pickle.loads进行反序列化
f1 = open('dump.txt', 'rb')
d1 = pickle.load(f1)
f1.close()
print(d1)
# 结果：{'name': 'Bob', 'age': 20, 'score': 88}



## 2.JSON
# 序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取;
# 可以直接在Web页面中读取;
import json
d2 = dict(name='Bob', age=20, score=88)
d3 = dict(name='Bob', age=20, score=88)

js = json.dumps({'data':[d2,d3]}, sort_keys=True, indent=4)
print(js)

# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法
# 由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str与JSON的字符串之间转换。



## 3.JSON进阶将一个类序列化成对象（先转换为字典）
import json
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
s = Student('Bob', 20, 88)

# 类序列化 方法1
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
print(json.dumps(s, default=student2dict))

# 类序列化 方法2
print(s.__dict__)  # 将属性通过字典方式输出
print(json.dumps(s, default=lambda s: s.__dict__))

# 将JSON实例反序列化一个Student实例，loads() => dict => Student实例(object_hook)
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
# print(json_str)
print(json.loads(json_str, object_hook=dict2student))  # 返回类实例