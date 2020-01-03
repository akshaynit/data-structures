# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 15:40:54 2019

@author: AK389016
"""

import queue

adjlist = dict()
n = 4 #no of vertices

def addEdge(u, v):
    if u in adjlist:
        adjlist[u].append(v)
    else:
        adjlist[u] = list([v])
        
visited = [False] * n

def doDfs(visited, u):
    visited[u] = True
    print(u)
    if u in adjlist:
        for i in adjlist[u]:
            if visited[i] == False:
                doDfs(visited, i)

q = queue.Queue()

q.put(0)

def doBfs(visited, u):
    visited[u] = True
    print(u)
    
    for i in adjlist[u]:
        q.put(i)
        
    l = q.get()
    while q.empty() == False:
        i = q.get()
        if visited[i] == False:
            doBfs(visited, i)
        
addEdge(0, 1)
addEdge(0, 2)
addEdge(1, 3)
addEdge(2, 3)

doDfs(visited, 0)

visited = [False] * n

doBfs(visited, 0)

q = queue.Queue()

q.put(1)
q.put(2)
q.put(3)

print(q.get())
q.put(4)
print(q.get())
