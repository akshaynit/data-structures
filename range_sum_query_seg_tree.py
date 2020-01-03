# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 15:19:06 2019

@author: AK389016
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
a = [2, 5, 3, 11, 9, 0, 17]

segTreeSum = [-1] * 14

def constSumSegTree(i, j, segTreePos):
    if i == j:
        segTreeSum[segTreePos] = a[i]
        return
        
    mid = i + int((j - i) / 2)
    lChildIndex = segTreePos * 2 + 1
    rChildIndex = segTreePos * 2 + 2
    
    constSumSegTree(i, mid, lChildIndex)
    constSumSegTree(mid + 1, j, rChildIndex)
    
    segTreeSum[segTreePos] = segTreeSum[lChildIndex] +  segTreeSum[rChildIndex]

def sum_range_query(arrayLeft, arrayRight, nodeL, nodeR, segTreePos):
    print(arrayLeft)
    print(arrayRight)
    print(nodeL)
    print(nodeR)
    print(segTreePos)
    
    if nodeL >= arrayLeft and nodeR <= arrayRight:
        return segTreeSum[segTreePos]
    
    if arrayRight < nodeL or arrayLeft > nodeR:
        return 0
    
    mid = nodeL + int((nodeR - nodeL) / 2)
    return sum_range_query(arrayLeft, arrayRight, nodeL, mid, segTreePos * 2 + 1) + sum_range_query(arrayLeft, arrayRight, mid + 1, nodeR, segTreePos * 2 + 2)

def update_sum_tree(segTreePos, value, arrayLeft, arrayRight, index):
    print("hello")
    if arrayLeft == arrayRight:
        segTreeSum[segTreePos] = value
        return
    
    mid = arrayLeft + int((arrayRight - arrayLeft) / 2)
    
    lChild = segTreePos * 2 + 1
    rChild = segTreePos * 2 + 2
    
    if index <= mid:
        update_sum_tree(lChild, value, arrayLeft, mid, index)
    else:
        update_sum_tree(rChild, value, mid + 1, arrayRight, index)
    
    segTreeSum[segTreePos] = segTreeSum[lChild] + segTreeSum[rChild]
    
constSumSegTree(0, 6, 0)
sum_range_query(5, 6, 0, 6, 0)
update_sum_tree(0, 50, 0, 6, 5)