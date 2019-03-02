#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Stack:

    def __init__(self, capacity):
        assert capacity > 0
        self.__capacity = capacity
        self.__arr = [None] * capacity
        self.__count = 0

    def pop(self):
        assert not self.isEmpty()
        top = self.top()
        self.__count = self.__count - 1
        return top

    def push(self, val):
        assert not self.isFull()
        self.__arr[self.__count] = val
        self.__count = self.__count + 1

    def isEmpty(self):
        return self.__count == 0

    def isFull(self):
        return self.__count >= self.__capacity

    def size(self):
        return self.__count

    def top(self):
        return self.__arr[self.__count - 1]

    def bottom(self):
        return self.__arr[0]



if __name__ == "__main__":
    str = '{(1)}'
    map = {
        '}': '{',
        ')': '(',
        ']': ']'
    }
    stack = Stack(len(str))
    for c in str:
        if c in map.values():
            stack.push(c)
        elif c in map.keys():
            val = stack.pop()
            if map[c] != val:
                raise Exception("括号匹配错误")

