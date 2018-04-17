# -*- coding: utf-8 -*-
'''
Created on 2018.4.9
求素数
@author: huke
'''


def prime():   #求素数
    num = []
    i = 2
    for i in range(2,100):
        for j in range(2,i):
            if (i%j==0):
                break
        else:
            num.append(i)
    print(num)

def multi():
    for i in range(1,10):
        for j in range(1,i):
            print("%d*%d=%d"%(j,i,i*j),end=' ') #python的print可以加入end参数，更改print将如何结束
        print(" ")

if __name__ == '__main__':
    #prime()
    multi()