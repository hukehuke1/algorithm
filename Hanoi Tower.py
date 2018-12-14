# -*- coding:utf-8 -*-
'''
Created on 2018.11.26

@author: huke
'''

def move(n,a,b,c):
    if n == 1 :
        print(a, '-->', c)
    elif n >=1 :
        move((n-1), a, c, b)
        print(a, "->", c)
        move((n-1), b, a, c)


if __name__ == '__main__':
    move(5,'A','B','C')