# -*- coding:utf-8 -*-
'''
Created on 2017.10.24

@author: huke
insertSort
'''

def insertSort(array):
    a1 = []#建立一个空的List
    for x in array: #对既有List的每一项进行循环,x是旧list的一项
        print("该次循环插入的x值是%s"%(x))
        if len(a1)==0:#如果新List是空的，先把既有List的第一个数拷贝进新List。y是新list的一项
            a1.append(x)
        elif len(a1)==1:#新List有一项的时候，把既有List 第二个数拷贝进新List一项的左边或者右边
            if x<a1[0]:
                a1.insert(0,x)
            else:
                a1.append(x)
        else:
            for y in a1:#拿既有list的每一项对新List的每一项对比，如果比新List的某个数大，就插入到该项的右边。
                if x<y:
                    a1.insert((a1.index(y)),x)
                    break
        print("新的List是")
        print(a1)
    print("排序结果")
    print(a1)
    
if __name__ == '__main__':
    try:
        array = [22, 1, 5, 3, 6, 8, 4,12]
        insertSort(array)
    except Exception as e:
        print(e)
