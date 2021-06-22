#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@version:
author:fly
@time: 2021/03/03
@file: 24_[IO编程]文件读写.py
@function:
@modify:
"""


## 文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用，保证无论是否出错都能正确关闭文件，使用 try..finally实现
# try:
#     f = open('/path/to/file', 'r')
#     print(f.read())
# except FileNotFoundError as e:
#     print('FileNotFoundError')
# finally:
#     if f:
#         f.close()

## File对象方法
def reset_file():
    with open('hello.txt', 'w+') as f:
        f.write('1 aaa\n')
        f.write('2 bbb\n')
# reset_file()

##  几种模式区别
# with open('hello.txt', 'r+') as f:  # 从头覆盖写，无文件报错 : FileNotFoundError
# with open('hello.txt', 'w+') as f:  # 覆盖所有写，无文件新增
# with open('hello.txt', 'a+') as f:  # 末尾追加写，无文件新增
#     f.write('3 ccc')


## 文件定位 seek
with open('hello.txt', 'r+') as f:
    # f.write('123456789\n')
    # print(f.closed)  # 是否关闭 True
    # print(f.mode)    # 读取模式
    # print(f.name)    # 文件名称
    print(f.tell())    # 查看指针位置
    print(f.seek(5),f.read(), f.tell())  # 移动指针
    print(f.seek(0), f.read())

    # print(f.read())
    # print(f.read(10))    # 一次性读取多少字节
    # print(f.readline())
    # print(f.readlines())


## 读文件

## Python引入了with语句来自动帮我们调用close()方法：
with open('/path/to/file', 'r') as f:
    print(f.read())

## 读取方法
f.read()        # 一次性读取，如果文件太大容易撑爆内存
f.read(10)      # 分段读取
f.readline()    # 每次读取一行
f.readlines()   # 一次性读取所有内容并返回list
for line in f.readlines():
    print(line.strip())


## 读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：
'''
>>> f = open('/Users/michael/test.jpg', 'rb')
>>> f.read()
b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00...' # 十六进制表示的字节
'''

## 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：
'''
>>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
>>> f.read()
'测试'
'''

## 读取忽略错误
'''
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')
'''


## 写文件
# 类似读，写使用 'w' 或 'wb', 表示文本或二进制，覆盖写，追加模式使用 'a'；
# + 打开一个文件进行更新(可读可写), r+, w+, a+
'''
>>> f = open('/Users/michael/hello.txt', 'w')
>>> f.write('Hello, world!')
>>> f.close()
'''

# 写文件并不是实时写入，而是在内存缓存，空闲写，只有调用close()方法时，操作系统才会把数据全部写进磁盘，使用 with 避免忘记close();
with open('/Users/michael/hello.txt', 'w') as f:
    f.write('Hello, world!')


## StringIO：内存中读写str
from io import  StringIO
f = StringIO()
f.write('Hello')
print(f.getvalue())
print(f.closed)
f.close()
print(f.closed)


## BytesIO：内存中读写bytes
from io import BytesIO
fb = BytesIO()
fb.write('中文'.encode())      # 默认编码成utf-8
print(fb.getvalue().decode())