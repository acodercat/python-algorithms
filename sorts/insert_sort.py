#!/usr/bin/env python
# -*- coding: utf-8 -*-

def insertSort(arr):
    for i in range(1, len(arr)):
        e = arr[i]
        for j in reversed(range(i + 1)):
            if e > arr[j - 1] or j == 0:
                break
            arr[j] = arr[j - 1]
        arr[j] = e
    return arr

if __name__ == "__main__":
    arr = insertSort([1, 2, 3, 12, 451, 0, 11, 134, 2314, 1])
    print(arr)


