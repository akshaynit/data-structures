# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 23:04:10 2019

@author: AK389016
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 14:56:57 2019

@author: AK389016
"""

a = [2, -3, 0, 12, 11, 9]

bitTree = [0] * 7

def get2scomplement(x):
    return (~x) + 1

def getParent(childIndex):
    twosc = get2scomplement(childIndex)
    temp = childIndex & twosc
    return childIndex - temp

def getNext(childIndex):
    twosc = get2scomplement(childIndex)
    temp = childIndex & twosc
    return childIndex + temp

getParent(15)

getNext(2)

def update(index, value):
    if index >= len(a) + 1:
        return
    print(index)
    bitTree[index] += value

    update(getNext(index), value)
        
for i in range(1, len(a) + 1):
    update(i, a[i - 1])

def getPrefixSum(index):
    prefixSum = 0
    index  = index + 1
    while (index > 0):
        print(index)
        prefixSum += bitTree[index]
        index = getParent(index)
    return prefixSum
getPrefixSum(0)