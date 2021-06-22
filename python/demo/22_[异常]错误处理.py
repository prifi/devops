#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@version:
author:fly
@time: 2021/03/03
@file: 22_[异常]错误处理.py
@function:
@modify:
"""

## 异常处理 try...except...finally...

## 1.执行出错后续代码不会执行，跳转至 except..finally
try:
    print('try...')
    r = 10 / 0                 # 此处异常捕获错误
    print('result:', r)        # 则此处代码将不执行，直接跳转至 except..finally
except ZeroDivisionError as e:
    print('except:', e)
finally:                       # finally如果有，则一定会被执行（可以没有finally语句）
    print('finally')
print('END')
# 结果：
# try...
# except: division by zero
# finally
# END



print('-'*30)
## 2.不同类型错误使用多个except来捕获处理
try:
    print('try ..')
    r = 10 / int('a')
    # r = 10 / 2
    print('result: ',r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError', e)
else:                                # 可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句
    print('no error')
finally:
    print('finally...')
print('END')



print('-'*30)
## 3.Python的错误其实也是class，注意except捕获的错误子类与父类继承关系，捕获父类错误会忽略子类，常见错误类型继承关系：
# https://docs.python.org/3/library/exceptions.html#exception-hierarchy
# BaseException
# - Exception
#    - AttributeError
#    - ...
try:
    foo()
except ValueError as e:
    print('ValueError')
except UnicodeError as e:
    print('UnicodeError')
except NameError as e:
    print('NameError')
# 第二个except永远也捕获不到UnicodeError，因为UnicodeError是ValueError的子类，如果有，也被第一个except给捕获了。



print('-'*30)
## 4.跨越多层调用
# 函数main()调用bar()，bar()调用foo()，结果foo()出错了, main()就可以捕获到然后处理
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')
main()
# Error: division by zero
# finally...



## 5.调用栈(异常栈)
# $ python3 err.py
# Traceback (most recent call last):     # 从上往下可以看到整个错误的调用函数链
#   File "err.py", line 11, in <module>
#     main()
#   File "err.py", line 9, in main
#     bar('0')
#   File "err.py", line 6, in bar
#     return foo(s) * 2
#   File "err.py", line 3, in foo
#     return 10 / int(s)
# ZeroDivisionError: division by zero



print('-'*30)
## 6.记录错误日志，使程序继续运行
import logging
def foo1(s):
    return 10 / int(s)
def bar1(s):
    return foo1(s) * 2
def main1():
    try:
        bar1('0')
    except Exception as e:
        logging.exception(e)
main1()
print('END')
# 同样是出错，但程序打印完错误信息后会继续执行，并正常退出：
# ERROR:root:division by zero
# ...
# END



print('-'*30)
## 7.自定义抛出异常
# 定义一个错误的class，选择好继承关系，使用raise语句抛出错误实例
class FooError(ValueError):
    pass
def foo2(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n
# foo2('0')
print('END')  # 抛出异常后退出，不会执行后面代码
# raise FooError('invalid value: %s' % s)  # 尽量使用python内置错误类型（比如：ValueError, TypeError）


print('-'*30)
# 捕获错误目的只是记录一下并向上抛出，便于后续追踪调试
def foo3(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n
def bar2():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError')
        raise                  # rasie不带参数表示原样抛出错误
# bar2()


# except中rasie一个Error可以把一种类型错误转换位另一种类型
try:
    10 / 0
except ZeroDivisionError as e:
    raise ValueError('input error')



## 练习：捕获异常
import logging
from functools import reduce

# def str2num(s):
#     return int(s)

def calc(exp):
    ss = exp.split('+')
    try:
        ns = map(int, ss)
        return reduce(lambda acc, x: acc + x, ns)
    except ValueError as e:
        # logging.exception(e)
        print('ValueError')

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()
print('END')