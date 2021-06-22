#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@version:
author:fly
@time: 2021/03/09
@file: 29_[正则]正则表达式.py
@function:
@modify:
"""
#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@version:
author:fly
@time: 2021/03/09
@file: 29_[正则]正则表达式.py
@function:
@modify:
"""
## 正则表达式
'''
\d \D   # 数字
\w \W   # 字母数字汉字
\s \S   # 任意空字符 \n \t \v
^ $     # 锚定行首行尾
. + *   # 0or1 1or多 0or多
() [] {} # 分组 或 次数
? (非贪婪)

# [a-zA-Z\_][0-9a-zA-Z\_]{0, 19} # 精确地限制了变量的长度是1-20个字符
'''

## re模块
import re

'''
# 匹配上返回，无匹配返回None
re.match()     # 开头匹配
re.search()    # 全文匹配
'''

# 判断正则是否匹配
test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print('ok')
else:
    print('failed')
# 结果：failed


## 正则切分字符串更灵活
x = re.split(r'\s+', 'a b  c')  # 忽略连续空格 ['a', 'b', 'c']
y = re.split(r'[\s\,\;]+', 'a,b c; d')  # 忽略空格逗号分好 ['a', 'b', 'c', 'd']

## 分组 group()
# 比如：^(\d{3})-(\d{3,8})$分别定义了两个组
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m)
print(m.groups())  # ('010', '12345')
print(m.group())  # 010-12345         # 默认group(0) 本身
print(m.group(1))  # 010

## 提取时间
'''
>>> t = '19:05:30'
>>> m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
>>> m.groups()
('19', '05', '30')
'''

## 贪婪匹配 +? *? 尽可能少的匹配
# 需求匹配'102300'数字后面的0
r = re.match(r'^(\d+)(0*)$', '102300').groups()
print(r)  # ('102300', '')

# 非贪婪模式
r1 = re.match(r'^(\d+?)(0*)$', '102300').groups()
print(r1)  # ('1023', '00')

## 编译 *
# 使用编译后的正则表达式去匹配字符串，效率更高（预编译 re.compile()）
import re

re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-12345').groups())
print(re_telephone.match('010-123'))
# 不匹配返回None


## 练习1：尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email
import re


def is_valid_email(addr):
    re_email = re.compile(r'(^([a-zA-Z0-9\.]+)@([a-zA-Z0-9]+)\.com)')
    return re_email.match(addr)


assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

## 练习2：提取出带名字的Email地址
import re
def name_of_email(addr):
    re_name = re.compile(r'<(\w+\s\w+)>|\w+')
    if re_name.match(addr).groups()[0]:
        return re_name.match(addr).group(1)
    return re_name.match(addr).group(0)
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')

# re_name = re.compile(r'<(\w+\s\w+)>|\w+')
# print(re_name.match('<Tom Paris> tom@voyager.org').groups()[0])
# print(re_name.match('tom@voyager.org').groups()[0])

# 方法2：
print([x for x in re.split(r'[\<\>\@]+', '<Tom Paris> tom@voyager.org') if x][0])
print([x for x in re.split(r'[\<\>\@]+', 'tom@voyager.org')][0])
