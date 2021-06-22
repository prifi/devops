#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@version:
author:fly
@time: 2021/02/20
@file: 14-1_使用模块.py
@function:
@modify:
"""

## 模块（Module）：
## 在Python中，一个.py文件就称之为一个模块（Module）
    # - 模块名要遵循Python变量命名规范，不要使用中文、特殊字符；
    # - 使用模块可避免函数名与变量名冲突，但要注意不要与内置函数名冲突（内置函数：https://docs.python.org/3/library/functions.html）


## 包（Package）：
## 为了避免模块名冲突，Python又引入了按目录来组织模块的方法，称为包（Package）
    # - 包目录下面必须有一个__init__.py的文件，否则被认为是目录


# 文件www.py的模块名就是mycompany.web.www，两个文件utils.py的模块名分别是mycompany.utils和mycompany.web.utils。
# mycompany
#  ├─ web
#  │  ├─ __init__.py
#  │  ├─ utils.py
#  │  └─ www.py
#  ├─ __init__.py
#  ├─ abc.py
#  └─ utils.py

# 命令行直接执行hello模块时，Python解释器把一个特殊变量__name__置为__main__，如果在其他地方导入该模块时，if判断将失败，常用于运行测试。
# if __name__=='__main__':
#     test()


## 作用域
# - 公开(public)变量：可以被直接引用，比如：abc，x123，PI等；
# - 私有(private)变量：类似_xxx和__xxx这样的函数或变量就是非公开的（private），从编程习惯上不应该引用private函数或变量。

# private函数或变量作用示例：
def _private_1(name):
    return 'Hello, %s' % name
def _private_2(name):
    return 'Hello, %s' % name
def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
# 调用greeting()函数不用关心内部的private函数细节，这也是一种非常有用的代码封装和抽象的方法，即：
# 外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。


## 第三方模块使用pip安装，https://pypi.org/
# pip install xxx


## 模块搜索路径
# 默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中：
import sys
sys.path

# 如果我们要添加自己的搜索目录，有两种方法：
# 1.直接修改sys.path，添加要搜索的目录：
sys.path.append('/Users/michael/my_py_scripts')
# 2.设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。
