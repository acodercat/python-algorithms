import math

class MaxHeap:

    def __init__(self, capacity):
        assert capacity > 0
        self.__capacity = capacity
        self.__arr = [None] * capacity
        self.__count = 0

    def __shiftDown(self, k = 0):
        assert k < self.size() and k >= 0
        e = self.__arr[k]
        while True:
            leftChildNode = 2 * k + 1
            rightChildNode = leftChildNode + 1
            if leftChildNode >= self.size():
                break
            if rightChildNode < self.size() and self.__arr[rightChildNode] > self.__arr[leftChildNode]:
                maxChildNode = rightChildNode
            else:
                maxChildNode = leftChildNode

            if e > self.__arr[maxChildNode]:
                break
            self.__arr[k] = self.__arr[maxChildNode]
            k = maxChildNode
        self.__arr[k] = e

    def __shiftUp(self, k):
        while True:
            parentNode = math.floor((k - 1) / 2)
            if k > 0 and (self.__arr[k] > self.__arr[parentNode]):
                [self.__arr[k], self.__arr[parentNode]] = [self.__arr[parentNode], self.__arr[k]]
                k = parentNode
            else:
                break

    def extract(self):
        assert not self.isEmpty()
        rootNode = self.rootNode()
        tailNode = self.tailNode()

        self.__arr[0] = tailNode
        self.__shiftDown()
        self.__count = self.__count - 1
        return rootNode

    def insert(self, val):
        assert not self.isFull()
        self.__arr[self.__count] = val
        self.__shiftUp(self.__count)
        self.__count = self.__count + 1

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.__count == 0

    def isFull(self):
        return self.__count >= self.__capacity

    def rootNode(self):
        return self.__arr[0]

    def tailNode(self):
        return self.__arr[self.size() - 1]

    def show(self):
        # print('==============')
        for i in range(self.size()):
            print(self.__arr[i])
        print('==============')






maxHeap = MaxHeap(6)
maxHeap.insert(1)
maxHeap.insert(2)
maxHeap.insert(9)
maxHeap.insert(13)
maxHeap.insert(99)
maxHeap.insert(66)
maxHeap.show()
maxHeap.extract()
maxHeap.extract()

# print(maxHeap.extract())
maxHeap.show()
# print(maxHeap.extract())
# print(maxHeap.extract())