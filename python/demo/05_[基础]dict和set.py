#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@version:
author:xiaopengfei
@time: 2021/01/24
@file: 05_[基础]dict和set.py
@function:
@modify:
"""

## 字典 dict 键-值（key-value）存储
    # dict的key必须是不可变对象（字符串或者整数），使用hash key计算出value地址，key的对象不能改变。
    # dict用空间换取时间的一种方法

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Bob'])
print(len(d))  # 3

# d['Adm'] = 67     # 通过key放入
if 'Adm' not in d:  # 判断一个元素是否存在该字典
    print(d)
print(d.get('Adm','NewValue'))  # NewValue # get()方法，如果key不存在，返回None，或者自己指定的value

res = d.pop('Bob')  # 删除元素
print(res)          # 75

d.keys()   # 输出所有key
d.values() # 输出所有value

# 输出k,v
for k,v in d.items():
    print(k,v)



## 集合 set
    # 一组key集合，不包含value
    # 不允许有重复的key
    # 无序和无重复元素的集合
    # 不能放入可变对象，否则无法判断集合内元素是否重复

s = set([1, 1, 2, 2, 3, 3])
print(s)  # {1, 2, 3}

s.pop()      # 从头弹出一个元素
s.remove(3)  # 删除指定key,不存在报keyError
s.discard(3) # 删除指定key,不存在不会报错，返回None
print(s)     # {2}

s.add(4)
s.add(4)  # 可以重复添加，但生效只有一个
print(s)  # {2, 4}

s1 = set([1,2,3])
s2 = set([2,3,4])
s1 & s2  # {2, 3}  # 交集
s1 | s2  # {1, 2, 3, 4}  # 并集


## 可变对象和不可变对象
a = 'abc'
b = a.replace('a','A')  # a 本身不会替换，replace()方法会创建出新对象赋给b
print(a,b)              # abc Abc