from collections import defaultdict

n, m = map(int, input().split(' '))
edges = dict()
distances = dict()

heapsize = 0

def empty(heap):
    global heapsize
    if heapsize <= 0:
        return True
    return False

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
    
    while i >= 0 and heap[i][1] < heap[parent_index(i)][1]:
        temp = heap[i]
        heap[i] = heap[parent_index(i)]
        heap[parent_index(i)] = temp
        i = heap[parent_index(i)]

def extractTop(heap):
    global heapsize
    if heapsize <= 0:
        return 1000000000
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
    if l < heapsize and heap[l][1] < heap[smallest][1]:
        smallest = l
    if r < heapsize and heap[r][1] < heap[smallest][1]:
        smallest = r
    
    if smallest != n:
        temp = heap[smallest]
        heap[smallest] = heap[n]
        heap[n] = temp
        minHeapify(heap, smallest)
     
heap = []

insert_heap(heap, ((1, 2), 5))
insert_heap(heap, ((1, 3), 2))
insert_heap(heap, ((3, 4), 1))
insert_heap(heap, ((1, 4), 6))
insert_heap(heap, ((3, 5), 5))

extractTop(heap)

for i in range(m):
    
    u, v, w = [int(x) for x in input().split(' ')]
    edges[u].append((v, w))
    distances[1] = 0
    
source = 0

for edge in edges[source]:
    insert_heap(((source, edge[0], edge[1])))
    
while (!empty(heap)):
    top = extractTop(heap)
    
    if distances[top[0][1]] > distances[top[0][0]] + distances[top[1]]:
        distances[top[0][1]] = distances[top[0][0]] + distances[top[1]]
    
    for edge in edges[top[0][1]]:
        insert_heap(((top[0][1], edge[0]), edge[1]))
    

for v, dist in distances.items():
    if v == 1:
        continue
    print(dist, end = ' ')
