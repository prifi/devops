#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@version:
author:fly
@time: 2021/03/05
@file: 28_[进程和线程]多线程.py
@function:
@modify:
"""

### 多线程
## 启动线程：将函数启动并传入Thread实例，然后调用start()开始执行
import time, threading
# 新线程执行代码
def loop():
    print('thread %s is running..' % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended' % threading.current_thread().name)

def main():
    # Python的threading模块有个current_thread()函数，它永远返回当前线程的实例。
    print('thread %s is running...' % threading.current_thread().name)
    # 线程创建时会自动创建主线程
    # 主线程实例的名字叫MainThread，子线程的名字在创建时指定，我们用LoopThread命名子线程。
    # 如果不起名字Python就自动给线程命名为Thread-1，Thread-2……
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()
    print('thread %s ended.' % threading.current_thread().name)


### Lock
## 多线程中，所有变量都由所有线程共享，多线程中同时修改一个变量，可能会导致数据不一致；
## 保证多线程操作数据一致性，创建一个锁就是通过threading.Lock()来实现：
    # - 获得锁的线程记得释放，防止死锁
## 多线程因为GIL锁不能利用多核CPU，可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响。
import time, threading
# 假设银行存款
balance = 0
lock = threading.Lock()
def change_it(n):
    # 先存后取，结果应该是0
    global balance
    balance += n
    balance -= n

def run_thread(n):
    for i in range(2000000):
        # 获取锁
        lock.acquire()
        try:
            # 线程操作数据
            change_it(n)
        finally:
            # 改完释放锁
            lock.release()

def main1():
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)

main1()


## Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。