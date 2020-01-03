# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 11:56:45 2019

@author: AK389016
"""
n, m = map(int, input().split(' '))
edges = list()
distances = dict()

for i in range(m):
    
    u, v, w = [int(x) for x in input().split(' ')]
    
    edges.append((u, v, w))
    distances[u] = 1000000000
    distances[v] = 1000000000
    distances[1] = 0
    
    for i in range(n - 1):
        for edge in edges:
            if distances[edge[1]] > distances[edge[0]] + edge[2]:
                distances[edge[1]] = distances[edge[0]] + edge[2]
    
    

for v, dist in distances.items():
    if v == 1:
        continue
    print(dist, end = ' ')
