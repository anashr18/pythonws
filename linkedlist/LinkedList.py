from random import randint
class Node:
    def __init__(self, value=None):
        self.value= value
        self.next = None
        self.prev = None
    def __str__(self):
        return str(self.value)
class CustomLL:
    def __init__(self, values=[]):
        self.head = None
        self.tail = None
        for value in values:
             self.addLL(value)
    def addLL(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next
    def __str__(self):
        values = [str(x.value) for x in self]
        return '->'.join(values)
    def __len__(self):
        node = self.head
        length = 0
        while node:
            length+=1
            node = node.next
        return length
    def generate(self, n , minVal, maxVal):
        self.head = None
        self.tail = None
        for i in range(n):
            self.addLL(randint(minVal, maxVal))
        return self

# ll = CustomLL([1,2,3,4,56,7])
# print(ll)