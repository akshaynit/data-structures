# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 14:56:57 2019

@author: AK389016
"""

a = [0, 2, -3, 0, 12, 11, 9]

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
    if index >= len(a):
        return
    print(index)
    bitTree[index] += value

    update(getNext(index), value)
        
for i in range(1, len(a)):
    update(i, a[i])

def getPrefixSum(index):
    prefixSum = 0
    while (index > 0):
        prefixSum += bitTree[index]
        index = getParent(index)
    return prefixSum
getPrefixSum(6)
