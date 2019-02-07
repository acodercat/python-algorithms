#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Node:

    def __init__(self, value = None, isKey = False):
        self.__value = value
        self.__isKey = isKey
        self.__childNodes = {}

    def addNode(self, c, node):
        self.__childNodes[c] = node

    def isKey(self):
        return self.__isKey

    def childNodes(self):
        return self.__childNodes

    def value(self):
        return self.__value

    def setValue(self, value):
        self.__value = value

    def setIsKey(self, isKey):
        self.__isKey = isKey

class Trie:

    def __init__(self):
        self.__rootNode = Node()
        self.__size = 0

    def insert(self, key, value):
        currentNode = self.__rootNode
        for c in key:
            if c not in currentNode.childNodes():
                currentNode.childNodes()[c] = Node()
            currentNode = currentNode.childNodes()[c]

        if not currentNode.isKey():
            self.__size = self.__size + 1
            currentNode.setIsKey(True)
        currentNode.setValue(value)

    def find(self, key):
        currentNode = self.__rootNode
        for c in key:
            if c not in currentNode.childNodes():
                return False
            currentNode = currentNode.childNodes()[c]
        if currentNode.isKey():
            return currentNode.value()
        return False

    def size(self):
        return self.__size



if __name__ == "__main__":
    trie = Trie()
    trie.insert("cat", '1212')
    # trie.insert("cat", 'asdasd')
    print(trie.find("cat"))
