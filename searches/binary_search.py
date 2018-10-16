import math


def binarySearch(arr, v):
    leftIndex = 0
    rightIndex = len(arr) - 1
    while (leftIndex <= rightIndex):
        middleIndex = leftIndex + math.floor((rightIndex - leftIndex) / 2)
        if v == arr[middleIndex]:
            return middleIndex
        if v > arr[middleIndex]:
            leftIndex = middleIndex + 1
        elif v < arr[middleIndex]:
            rightIndex = middleIndex - 1

arr = [i for i in range(100)]



found = binarySearch(arr, 99)
print(found)
