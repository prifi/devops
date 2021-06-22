#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@version:
author:fly
@time: 2021/03/09
@file: 30_3[内置模块]base64.py
@function:
@modify:
"""
### Base64是一种用64个字符来表示任意二进制数据的方法。
import base64

# Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉。
print(base64.b64encode(b'binary\x00string'))  # base64编码  # b'YmluYXJ5AHN0cmluZw=='
print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))  # base64解码 # b'binary\x00string'

# 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：
print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))  # b'abcd++//'
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))  # b'abcd--__'

# 由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉：
print(base64.b64encode(b'abcd'))
print(base64.b64decode(b'YWJjZA=='))
# 在还原时再把 = 加上，还原为4的倍数解码

## 练习：请写一个能处理去掉=的base64解码函数：
import base64
def safe_base64_decode(s):
    ## 方法1：
    # n = len(s)
    # while n % 4 != 0:
    #     s += b'='
    #     n = len(s)
    ## 方法2：
    s += b'='*(4-len(s)%4)
    return base64.b64decode(s)

# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')

## 总结：
# Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。
