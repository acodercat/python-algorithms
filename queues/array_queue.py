#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ArrayQueue:

    def __init__(self, capacity):
        assert capacity > 0
        self.__capacity = capacity
        self.__arr = [None] * capacity
        self.__count = 0

    def enqueue(self, val):
        assert not self.isFull()
        self.__arr[self.getSize()] = val
        self.__count = self.__count + 1

    def dequeue(self):
        assert not self.isEmpty()
        front = self.getFront()
        for i in range(1, self.getSize()):
            self.__arr[i - 1] = self.__arr[i]
        self.__count = self.__count - 1
        return front

    def isFull(self):
        return self.__count >= self.__capacity

    def isEmpty(self):
        return self.__count == 0

    def getSize(self):
        return self.__count

    def getFront(self):
        return self.__arr[0]


if __name__ == "__main__":
    arrayQueue = ArrayQueue(5)
    arrayQueue.enqueue(1)
    arrayQueue.enqueue(2)
    arrayQueue.enqueue(3)
    front = arrayQueue.getFront()
    print(front)

