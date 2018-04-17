# -*- coding: utf-8 -*-
'''
Created on 2018.4.10

@author: huke
'''


import os


def getaverage(url,filename):
    l = []
    newL = []
    os.chdir(url)
    f = open(filename)
    for line in f:
        # print(line.rstrip("ms\n"))
        i1 = int(line.rstrip("ms\n"))
        l.append(i1)
    print("一共%s行"%len(l))
    l.sort()
    # 取10%-90%区间的数据
    l1 = round(len(l)*0.1)
    l2 = round(len(l)*0.9)
    for i in range (l1,l2):
        newL.append(l[i])
    s = 0
    for i in newL:
        s += i
    print(s)
    e = s/len(newL)
    print("一共%s行"%len(newL))
    print("平均值是%f"%e)
        

if __name__ == '__main__':
    desturl = "C:\\Users\\huke\\Desktop\\内网测试"
    filename = "157-haverule.txt"
    getaverage(desturl,filename)