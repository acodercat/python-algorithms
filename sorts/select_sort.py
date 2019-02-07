#!/usr/bin/env python
# -*- coding: utf-8 -*-

def selectSort(arr):
    for i in range(len(arr)):
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr



if __name__ == "__main__":
    arr = selectSort([1, 2, 3, 12, 451, 0, 11, 134, 2314, 1])
    print(arr)
