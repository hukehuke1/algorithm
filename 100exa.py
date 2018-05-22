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
import random


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
    l = []
    for i in range(1,4):
        x = input("请输入数字")
        l.append(int(x))
    l.sort()    
    print(l)

def exa6(n):
    a ,b = 1 ,1
    for i in range(n-1):
        a,b = b,a+b
    return a

def exa6b(n):  #递归
    if n ==1 or n == 2:
        return 1
    else :
        return exa6b(n-1)+exa6b(n-2)

def exa7():
    a = [1,2,3]
    b = a[:]
    print(b)

def exa8():
    for i in range(1,10):
        print()
        for j in range(1,i):
            print("%s*%s=%s"%(j,i,str(i*j)),end = ' ')


import time
def exa9():
    for i in range(10):
        print(i)
        time.sleep(1)
        print(time.time())
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))



def exa11(n):
    a ,b = 1,1
    for i in range(n-1):
        a ,b = b, a+b
        print(a)

from math import sqrt

def exa12():#判断101-200之间有多少个素数，并输出所有素数。
    leap = 1
    h = 0
    for i in range(101,201):
        sqt = int(sqrt(i+1))

        for j in range(2,sqt+1):
            if i % j == 0:
                leap = 0
                break
        if leap == 1:
            print('%s是素数'%i)
            h += 1
        leap = 1
    print('一共有%s个数'%h)


def exa13(): #打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身
    for n in range(100,1000):
        i = int(n / 100)
        j = int((n % 100)/10)
        k = int((n % 10))
        if n == i**3 + j**3 + k**3:
            print("%s是水仙花数"%n)



import datetime
def exa16():
    print(datetime.date.today().strftime('%d/%m/%Y'))

    myBirthday = datetime.datetime(1988,5,10)
    print(myBirthday.strftime('%d/%m/%Y'))
    myBirthday = myBirthday.replace(year = myBirthday.year + 1)
    print(myBirthday)


def exa17():
    
    pass

def twoSum(nums,target):
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if (int(nums[i]) + int(nums[j]) == int(target)) & (i != j) :
                print(nums[i])
                print(nums[j])              
                print("和是%s"%target)
                return[i,j]



# 用python实现链表 并且计算 https://leetcode-cn.com/problems/add-two-numbers/description/


class ListNode():
    def __init__(self,value = None,nextnode = None):
        self._val = value
        self._nextnode = nextnode
    
    def append(self,n):
        if not isinstance(n,ListNode):
            n = ListNode(n)
        self._nextnode, n = n,self._nextnode
        self._nextnode._nextnode = n

    def __repr__(self):
        '''
        用来定义Node的字符输出，
        print为输出data
        '''
        return str(self._val)

    def getValue(self):
        return self._val


class Solution:
    def addTwoNumbers(self, l1, l2):
        rsum = self.analysis(l1)+self.analysis(l2)
        length = len(str(rsum))
        for i in str(rsum):
            l3 = ListNode()
            l3 = l3.append(i)
            pass
            


    def analysis(self,l1):
        rsum = int(l1.getValue())
        digit = 1
        while True:
            if l1._nextnode != None:
                l1 = l1._nextnode
                digit += 1
                rsum = rsum + int(l1.getValue())*(pow(10,digit-1))
            else:
                break
        return(rsum)





# def internationalStandardDanceTraining():
#     trainingGroup = ["珂妈","台柱子","鹫峰大仙","加班狗"]  #训练成员名单
#     for i in trainingGroup:
#         goto209(i)

# def goto209(i):
#     t = datetime.datetime(2018, 5, 17, 20, 0)
#     print("%s 请在%s来209训练啦"%(i,t))
#     #TODO 调用itchat库分别给好友发微信消息



if __name__ =='__main__':
    #print(int(random.uniform(1,211)))
    l1 = ListNode('2',ListNode('4',ListNode('3')))
    l2 = ListNode('5',ListNode('6',ListNode('4')))

    #print(Solution.analysis(l2,l1))  #TODO 为什么这里还要传入第一个参数？
    # while True:
    #     print(l1)
    #     if l1._nextnode != None:
    #         l1 = l1._nextnode
    #     else:
    #         break
