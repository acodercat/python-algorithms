#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

class HeapSort:

    def __init__(self, arr):
        self.__arr = arr
        self.__count = len(arr)
    def __shiftDown(self, n, k):
        assert k < n and k >= 0
        e = self.__arr[k]
        while True:
            leftChildNode = 2 * k + 1
            rightChildNode = leftChildNode + 1
            if leftChildNode >= n:
                break
            if rightChildNode < n and self.__arr[rightChildNode] > self.__arr[leftChildNode]:
                maxChildNode = rightChildNode
            else:
                maxChildNode = leftChildNode

            if e > self.__arr[maxChildNode]:
                break
            self.__arr[k] = self.__arr[maxChildNode]
            k = maxChildNode
        self.__arr[k] = e

    def sort(self):
        self.__heapify()
        for i in reversed(range(1, self.__count)):
            [self.__arr[0], self.__arr[i]] = [self.__arr[i], self.__arr[0]]
            self.__shiftDown(i, 0)
        return self.__arr


    def __heapify(self):
        nonLeafNode = math.floor(self.__count / 2) - 1
        for i in reversed(range(nonLeafNode + 1)):
            self.__shiftDown(self.__count, i)


if __name__ == "__main__":
    arr = [1, 2, 3, 43, 0, 99, 101, 0, 999]
    sortedArr = HeapSort(arr).sort()
    print(sortedArr)
