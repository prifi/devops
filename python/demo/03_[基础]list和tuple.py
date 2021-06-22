#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@version:
author:xiaopengfei
@time: 2021/01/24
@file: 03_[基础]list和tuple.py
@function:
@modify:
"""

# 集合 list（可变）
classmates = ['Michael', 'Bob', 'Tracy']
print(len(classmates))  # 3
print(classmates[1], classmates[-1]) # 用下标取元素，注意越界错误

classmates.append('adm')      # 追加到末尾
classmates.insert(1, 'Jack')  # 插入指定位置
classmates.pop()              # 删除末尾元素，会输出删除元素，删除指定位置元素使用：popvalue = list.pop(i)
classmates[1] = 'Sarah'       # 替换

s = ['python', 'java', ['asp', 'php'], 'scheme'] # list可以包含list（二维数组） len(s) = 4
print(s[2][1]) # php # 获取嵌套list元素

l = [2,3,1]
l.reverse() # [1,3,2] # 逆序
l.sort()    # [1,2,3] # 排序


## 列表时间复杂度
lst = [1, 4, 9, 16, 25, 36, 49]
lst.count(1)    # O(n)
lst.index(1)    # O(n) 越界则报错：ValueError: 100 is not in list
lst.append(100) # O(1)
lst.insert(1,1) # O(n) 引起位置挪动，插入末尾（100，1）则无


## 列表空间复杂度
l1 = [1,2,3]
lst.extend(l1)      # O(1) 原地修改返回None
new_list = lst + l1 # O(n) 返回新列表，旧列表不会垃圾回收，占用内存


## 列表深浅拷贝
l = [1,2,3]      # 一维数组拷贝不影响

l1 = [1,[1,2],3] # 二维数组浅拷贝，仅拷贝房间号
l2 = l1.copy()
l1[1][1] = 100
print(l1, l2)   # 浅拷贝l1修改后l2会同步修改：[1, [1, 100], 3]
print(l1 == l2) # True

import copy
l3 = copy.deepcopy(l1)
l1[1][1] = 200
print(l3)        # 深拷贝l1修改结果影响l3：[1, [1, 100], 3]
print(l1 == l3)  # False

## 二维数组相乘相当于浅拷贝，这里多维数组相乘的坑需注意
l4 = l1 * 3
print(l4)  # [1, [1, 200], 3, 1, [1, 200], 3, 1, [1, 200], 3]
l4[1][1] = 300
print(l4)  # [1, [1, 300], 3, 1, [1, 300], 3, 1, [1, 300], 3]  所有位置值同步修改


## 列表删除元素效率
l.remove(222)  # 效率低，元素挪动，O(n)，删除一个不存在的值，报错：ValueError: list.remove(x): x not in list
l.pop()        # 效率高，直接弹出 O(1)




# 元组 tuple（不可变）
# 与lsit区别一旦初始化不能改变
classset = ('Michael', 'Bob', 'Tracy')
print(classset[1])

t = ()    # 空tuple
t = (1,)  # 只有1个元素的tuple定义
print(t)

t = ('a', 'b', ['A', 'B'])  # tuple内对象不可改变，list本身可变



