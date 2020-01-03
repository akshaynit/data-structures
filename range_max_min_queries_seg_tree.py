# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
a = [2, 5, 3, 11, 9, 0, 17]

segTreeMax = [-1] * 14


def constMaxSegTree(i, j, segTreePos):
    if i == j:
        segTreeMax[segTreePos] = a[i]
        return

    mid = i + int((j - i) / 2)
    lChildIndex = segTreePos * 2 + 1
    rChildIndex = segTreePos * 2 + 2

    constMaxSegTree(i, mid, lChildIndex)
    constMaxSegTree(mid + 1, j, rChildIndex)

    segTreeMax[segTreePos] = max(
        segTreeMax[lChildIndex], segTreeMax[rChildIndex])


def max_range_query(arrayLeft, arrayRight, nodeL, nodeR, segTreePos):
    print(arrayLeft)
    print(arrayRight)
    print(nodeL)
    print(nodeR)
    print(segTreePos)

    if nodeL >= arrayLeft and nodeR <= arrayRight:
        return segTreeMax[segTreePos]

    if arrayRight < nodeL or arrayLeft > nodeR:
        return 0

    mid = nodeL + int((nodeR - nodeL) / 2)
    return max(max_range_query(arrayLeft, arrayRight, nodeL, mid, segTreePos * 2 + 1), max_range_query(arrayLeft, arrayRight, mid + 1, nodeR, segTreePos * 2 + 2))


def update_array(segTreePos, value, arrayLeft, arrayRight, index):
    print(arrayLeft)
    print(arrayRight)
    if arrayLeft == arrayRight:
        segTreeMax[segTreePos] = value
        print(segTreePos)
        return

    mid = arrayLeft + int((arrayRight - arrayLeft) / 2)
    lChildIndex = segTreePos * 2 + 1
    rChildIndex = segTreePos * 2 + 2

    if index <= mid:
        update_array(lChildIndex, value, arrayLeft, mid, index)
    else:
        update_array(rChildIndex, value, mid + 1, arrayRight, index)

    segTreeMax[segTreePos] = max(
        segTreeMax[lChildIndex], segTreeMax[rChildIndex])


constMaxSegTree(0, 6, 0)
max_range_query(3, 3, 0, 6, 0)

update_array(0, 25, 0, 6, 2)
