# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 11:16:22 2019

@author: AK389016
"""
heapsize = 0

def parent_index(pos):
    return int((pos - 1) / 2)

def lchild_index(pos):
    return int(2 * pos) + 1

def rchild_index(pos):
    return 2 * pos + 2

def insert_heap(heap, x):
    heap.append(x)
    global heapsize
    heapsize += 1
    i = heapsize - 1
    
    while i >= 0 and heap[i] < heap[parent_index(i)]:
        temp = heap[i]
        heap[i] = heap[parent_index(i)]
        heap[parent_index(i)] = temp
        i = heap[parent_index(i)]

def extractTop(heap):
    global heapsize
    if heapsize <= 0:
        return "Heap is empty"
    top = heap[0]
    heap[0] = heap[heapsize - 1]
    heapsize -= 1
    minHeapify(heap, 0)
    return top

def minHeapify(heap, n):
    l = lchild_index(n)
    r = rchild_index(n)
    smallest = n
    
    global heapsize
    if l < heapsize and heap[l] < heap[smallest]:
        smallest = l
    if r < heapsize and heap[r] < heap[smallest]:
        smallest = r
    
    if smallest != n:
        temp = heap[smallest]
        heap[smallest] = heap[n]
        heap[n] = temp
        minHeapify(heap, smallest)
     
heap = []

insert_heap(heap, 10)
insert_heap(heap, 15)
insert_heap(heap, 0)
insert_heap(heap, 25)
insert_heap(heap, 17)
insert_heap(heap, 5)

extractTop(heap)

