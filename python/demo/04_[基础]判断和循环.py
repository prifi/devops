#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@version:
author:xiaopengfei
@time: 2021/01/24
@file: 04_[基础]判断和循环.py
@function:
@modify:
"""

## 条件判断

# 如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else
# if <条件判断1>:
#     <执行1>
# elif <条件判断2>:
#     <执行2>
# elif <条件判断3>:
#     <执行3>
# else:
#     <执行4>

# if简写：x是非零数值、非空字符串、非空list等，就判断为True，否则为False
x = 1
if x:
    print('True')  # True

# str 类型不能和 int 类型直接比较
s = str(111)
print(type(s))  # <class 'str'>
i = int(s)
print(type(i))  # <class 'int'>

# flot类型比较
height = 1.75
if height == 1:
    print('haha')
elif 1 <= height <= 2:
    print('hehe')
else:
    print('heihei')



## 循环

# for循环
# 计算0-100之间到和
sum1 = 0
for x in range(101):
    sum1 = sum1 + x
print(sum1)

# while 循环
# 计算100以内奇数的和
sum2 = 0
n = 100
while n > 0:
    sum2 = sum2 + n
    n = n - 2
print(sum2)

# break 条件满足，提前结束循环
n1 = 1
while n1 <= 100:
    if n1 > 10:
        break
    print(n1)
    n1 = n1 + 1
print('END')

# continue 条件满足，跳过本次循环，执行下一次循环


## 随机数
import random
lst = [1,2,3,2,4,5,6]
print(random.randint(1,2))    # 随机选择一个数
print(random.randrange(0,8))  # 随机区间，左闭右开不包括8
print(random.sample(lst,3))   # 随机选择三个（不重复的）值组成数组，如果数组内包含相同的元素，则结果会包含相同值 lst = [1,2,2]
print(random.choice(lst))     # 随机选择一个值，从可迭代对象中，可重复
random.shuffle(lst)           # 随机排序，返回None
print(lst)


## 练习1：打印1-10内所有奇数
n2 = 0
while n2 < 10:
    n2 = n2 + 1
    if n2 % 2 == 0:
        continue
    print(n2)
print('END')
# 更好的办法利用range步长直接每隔2个取奇数
for i in range(1, 10, 2):
    print(i)


##练习2：猜数字游戏
import random
answer = random.randint(1,100)  # 生成1-100之间的随机数
count = 0
while True:
    count += 1
    # print(count)
    number = int(input('请输入一个数字：'))
    if number < answer:
        print('猜小了')
    elif number > answer:
        print('猜大了')
    else:
        print('猜对了')
        break
    if count >= 7:
        print('智商不足！')
        break
print('共猜了%d次' % count)


## 练习3：9*9乘法表
for x in range(1, 10):
    for y in range(1, x + 1):
        print('%d*%d=%d' % (x, y, x * y), end='\t')
    print()


## 练习4：输入一个正整数判断是不是素数
# 素数：只能被1和自身整除的大于1的整数
from math import sqrt
num = int(input('输入正整数：'))
is_prime = True
if num <= 0  or num == 1:
    is_prime = False
end = int(sqrt(num))
for x in range(2, end+1):
    if num % x == 0:
        is_prime = False
        break
if is_prime:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)


# 练习5：输入两个正整数计算它们的最大公约数和最小公倍数
x = int(input('输入x：'))
y = int(input('输入y：'))
if x > y:
    x, y = y, x
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d 和 %d 最大公约数: %d' % (x, y, factor))
        print('%d 和 %d 最小公倍数: %d' % (x, y, x * y // factor))
        break


## 练习6：打印三角形
raw=5
for i in range(raw):
    for _ in range(i + 1):
        print('*',end='')
    print()
# =======
# *
# **
# ***
# ****
# *****

for i in range(raw):   # 1
    for j in range(raw):  # 1
        # print(raw, i, j)
        if j < raw - i - 1:
            print(' ',end='')
        else:
            print('*',end='')
    print()
# ==========
#     *
#    **
#   ***
#  ****
# *****

for i in range(raw):
    for _ in range(raw - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()
# ==========
#     *
#    ***
#   *****
#  *******
# *********

## 扩展题： 打印菱形
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
# 伪代码
# 1 5 1
# 2 4 3
# 3 3 5
# 4 2 7
# 5 1 9
# -----
# 6 2 7
# 7 3 5
# 8 4 3
# 9 5 1
# =====
raw = 5
for i in range(raw): # 0-4
    for _ in range(raw - i): # 5-0, 5-1, 5-2, ...
        print(' ', end='')
        # print(_)
    for _ in range(2 * i + 1): # 2*0+1 1, 1*2+1 3, 2*2+1 5, 7, 9
        print('*', end='')
    print()
for j in range(raw + 1, raw * 2): # 6,10
    for _ in range(j - raw + 1):  # 6-5+1 2，7-5+1 3, 8-5+1 4, ...
        print(' ', end='')
    for _ in range(j - raw + 1, 2 * raw - (j - raw)): # 2,3,4,5 | 10-(6-5, 7-5, 8-5) 9, 8, 7, 6
        print('*', end='')
    print()



## 练习7：二分法输出数值位数（万以内）
num = int(input('num >>> '))
# 1 10 100 1000 10000
if num >= 1000:
    if num >= 10000:
        print('5位')
    else:
        print('4位')
else:
    if num >= 100:
        print('3位')
    elif num >= 10:
        print('2位')
    else:
        print('1位')


## 练习8：打印斐波那契数列 0、1、1、2、3、5、8、13、21、34 .. 100以内
a,b = 1,0
lenth = 100
while lenth:
    a,b = b,a+b  # 如果分开写需要借助临时变量
    # temp = b
    # b = a + b
    # a = temp
    print(a, end=" ")
    lenth -= 1


## 打印斐波那契数列101项
for x in range(102):
    a,b = b,a+b
    if x == 101:
        print(x,a)


## 练习9：打印100以内素数，大于1的自然数中，除了1和它本身以外不再有其他因数的数称为素数
# else子句：正常执行完循环执行else,中断则不执行
nums = 100
for num in range(2, nums):
    for i in range(2, num):
        if (num % i == 0):
            break
    else:                         # 注意 else 子句位置，否则会打印重复项
        print(num, end=' ')


## 练习10：将数字12345按位反转
num = 12345
reversed_num = 0
while num:
    reversed_num = reversed_num * 10 + num % 10  # 0+5, 50+4, 54+3, ..
    num //= 10 # 1234, 123, 12 ..
print(reversed_num)