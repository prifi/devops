#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@version:
author:fly
@time: 2021/03/03
@file: 23_[异常]调试.py
@function:
@modify:
"""

## 断言
# 类似于三目表达式 if a?pass:false 为真则pass，假则执行
# 断言的开关“-O”是英文大写字母O关闭，所有assert当成pass，例如：python -O error.py
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n
def main():
    foo('0')
# main()
# print('END') # 执行错误后退出，不会执行后续代码
# 结果：AssertionError: n is zero!


## logging
# 使用logging好处，允许你指定记录信息的级别，有debug，info，warning，error等几个级别，当我们指定level=INFO时，logging.debug就不起作用了
# 和assert比，logging不会抛出错误，而且可以输出到文件：
import logging
logging.basicConfig(level=logging.INFO)  # 指定输出日志级别，生产环境设置为error级别
def foo1(s):
    n = int(s)
    logging.info('n = %d' % n)
    return 10 / n
foo1('0')