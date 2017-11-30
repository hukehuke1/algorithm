# -*- coding:utf-8 -*-
"""
Created on 2017.11.8

@author: huke
"""
import threading
from time import ctime, sleep


def music(func):
    for i in range(2):
        print("I was listening to %s. %s" % (func, ctime()))
        sleep(1)


def move(func):
    for i in range(2):
        print("I was at the %s! %s" % (func, ctime()))
        sleep(5)


threads = []
t1 = threading.Thread(target=music, args=(u'爱情买卖',))
threads.append(t1)
t2 = threading.Thread(target=move, args=(u'阿凡达',))
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()#在子线程完成运行之前，这个子线程的父线程将一直被阻塞。

    print("all over %s" % ctime())
