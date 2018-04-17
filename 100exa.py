# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     100exa
   Description :   python100例 http://www.runoob.com/python/python-exercise-example1.html
   Author :       huke
   date：          2018/4/16
-------------------------------------------------
   Change Activity:
                   2018/4/16:
-------------------------------------------------
"""

def exa1():
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                if (i != k) and (j != k) and (i != j):
                    print(i,j,k)


def exa2():   #数轴来分界 比if else来判断分支要有效率
    i = int(input("净利润:"))
    arr = [1000000,600000,400000,200000,100000,0]
    rat = [0.01,0.015,0.03,0.05,0.075,0.1]
    r = 0
    for idx in range(0,6):
        if i > arr[idx]:
            r+=(i-arr[idx])*rat[idx]
            print((i-arr[idx])*rat[idx])
    print(r)


def exa4():  #输入某年某月某日，判断这一天是这一年的第几天？
    year = int(input('year:\n'))
    month = int(input('month:\n'))
    day = int(input('day:\n'))
    months = (0,31,59,90,120,151,181,212,243,273,304,334)
    if (0< month <=12):
        sum = months[month-1]
    else:
        print('data error')
    sum += day
    leap = 0
    if (year%400 == 0) or(year%4 == 0) and (year % 100 !=0):
        leap = 1
    if (leap == 1 )and (month >2):
        sum += 1
    print("今天是第%s天"%sum)

def exa5():
    pass

if __name__ =='__main__':
    exa4()