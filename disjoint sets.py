# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 20:10:34 2019

@author: AK389016
"""

#contains the parent of a given element
parent = dict()

def representative(x):
    if parent[x] == x:
        return x
    return representative[parent[x]]
    
def union(x, y):
    r1 = representative(x)
    r2 = representative(y)
    parent[r2] = parent[r1]
    
array = [1, 5, 3, 10, 14, 11]

for i in range(1, len(array)):
    union(array[i], array[ i + 1])



    
        