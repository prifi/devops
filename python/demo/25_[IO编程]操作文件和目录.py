#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@version:
author:fly
@time: 2021/03/04
@file: 25_[IO编程]操作文件和目录.py
@function:
@modify:
"""
## OS对象方法
import os
os.getcwd()
# os.system('id')           # 返回值是脚本的退出状态码
with os.popen('id') as p:  # 返回值是文件对象，既然是文件对象，使用完就应该关闭
    print(p.read())

ret = os.popen('ping 127.0.0.1')
# print(ret.readlines())  # 阻塞，程序会卡死
# os.popen()无法满足需求时，可以考虑subprocess.Popen();

## subprocess.Popen()执行linux命令;
import subprocess

def cmd(command):
    subp = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8")
    subp.wait(2)
    if subp.poll() == 0:
        print(subp.communicate()[0])
    else:
        print("失败")

# cmd('whoami') # vagrant


## Python中操作文件和目录
import os
print(os.name)      # 操作系统类型
print(os.uname())   # 系统详细信息
print(os.environ.get('PATH'))           # 获取环境变量
print(os.environ.get('x', 'default'))   # 获取环境变量（不存在使用default)
print(os.path.abspath('.'))             # 获取绝对路径
print(os.getcwd())                      # 获取绝对路径
print(os.path.join(os.getcwd(),'testdir'))    # 路径拼接 /data/xxx/testdir
# print(os.mkdir('testdir'))
# print(os.rmdir('testdir'))


## 拆分目录不需要真实存在的目录，需要先判断文件是否存在
print(os.path.split('/path/to/file.txt'))    # ('/path/to', 'file.txt') # 拆分路径
print(os.path.splitext('/path/to/file.txt')) # ('/path/to/file', '.txt') # 拆分获取文件名后缀
print(os.path.exists('/path/to/file.txt'))   # False # 是否存在
print(os.path.isfile('/path/to/file.txt'))   # False # 是否文件


## 文件重命名拷贝
# os.rename('hello.txt', 'test.py')  # 重命名，不存在报错：FileNotFoundError
# os.remove('test.py')  # 删除文件，不存在报错：FileNotFoundError
# import shutil # os模块补充
# shutil.copyfile('temp.py','test.py')  # 拷贝文件，不存在报错：FileNotFoundError


## 过滤当前目录下所有目录
print([x for x in os.listdir('.') if os.path.isdir(x)])

## 过滤当前目录下所有以.py结尾的文件
print([y for y in os.listdir('.') if os.path.isfile(y) and os.path.splitext(y)[1] == '.py'])


## 练习：编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
import os
def find_file_path(i, dir):
    for x in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, x)) and i in x:
            print(os.path.join(dir, x))
        if os.path.isdir(os.path.join(dir, x)):
            find_file_path(i, os.path.join(dir, x))
find_file_path('h', '.')