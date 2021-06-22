#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@version:
author:fly
@time: 2021/03/05
@file: 27_[进程和线程]多进程.py
@function:
@modify:
"""

## 多进程

# 子进程永远返回0，而父进程返回子进程的ID，getppid()可以拿到父进程id:
'''
import os
print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
'''


# multiprrcessing 跨平台
# multiprocessing模块就是跨平台版本的多进程模块，支持Windows
# Process类来代表一个进程对象，下面的例子演示了启动一个子进程并等待其结束：
from multiprocessing import Process
import os
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
def mutiPcsTest():
    print('Parent: ', os.getpid())
    # 创建子进程时，只需要传入一个执行函数和函数的参数
    p = Process(target=run_proc, args=('test',))
    # 用start()方法启动，这样创建进程比fork()还要简单
    print('start...')
    p.start()
    p.join()
    print('end...')

# mutiPcsTest()
'''
结果：
Parent:  20949
start...
Run child process test (20964)...
end...
'''



## Pool 进程池
# 如需启动大量子进程，可以使用进程池Pool方式批量创建子进程
from multiprocessing import Pool
import os, time, random
def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    # print('Task %s run %0.2f seconds')
    print('Task {} run {:.2f} seconds'.format(name, (end - start)))

def poolTest():
    print('Parent process %s.' % os.getpid())
    # 最多同时执行4个进程，Pool的默认大小是CPU的核数
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done ...')
    p.close()
    p.join()
    print('All subprocesses done.')

# poolTest()
# 注意输出的结果，task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行（Pool(4)）



## 子进程
## 子进程不是自身，而是外部进程，控制子进程的输入输出
# subprocess方便创建子进程，控制输入输出
import subprocess
'''
print('$ nslookup www.python.org')
# 和命令行直接运行的效果一样
r = subprocess.call(['nslookup', 'www.puthon.org'])
print('Exit code',r)


# 子进程还需要输入，通过communicate()方法输入：
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)
'''



### 进程间通信
# Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
from multiprocessing import Process, Queue
import os, time, random
# 写数据进程执行代码
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue..' % value)
        q.put(value)
        time.sleep(random.random())
# 读数据进程代码
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

def main():
    # 父进程创建Queue，并传给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入
    pw.start()
    # 启动子进程pr，读取
    pr.start()
    # 等待pw结束
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强制终止
    pr.terminate()

# main()