from random import randint
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    def __str__(self):
        return str(self.value)
class stackl:
    def __init__(self):
        self.top = None
        self.minNode = None
    def push(self, val):
        if self.minNode and (val > self.minNode.value):
            self.minNode = Node(value = self.minNode.value, next=self.minNode)
        else:
            self.minNode = Node(value = val, next=self.minNode)
        self.top = Node(value=val, next=self.top)
    def __iter__(self):
        temp = self.top
        while temp:
            yield temp
            temp = temp.next
    def __str__(self):
        values = [str(value) for value in self]
        return "->".join(values)
    def isEmpty(self):
        if self.top is None:
            return True 
    def pop(self):
        if self.isEmpty(): 
            return "The stack is Empty"
        value = self.top   
        self.top = self.top.next
        self.minNode = self.minNode.next
        return value
    def getminNode(self):
        return self.minNode
    def generate(self, n , minNodeVal, maxVal):
        self.top = None
        self.tail = None
        for i in range(n):
            self.push(randint(minNodeVal, maxVal))
        return self

stac = stackl()
stac.generate(10, -100, 20)
print(stac)
print(stac.getminNode())
print(stac.pop())
print(stac)
print(stac.getminNode())
print(stac.pop())
print(stac)
print(stac.getminNode())
print(stac.pop())
print(stac)
print(stac.getminNode())
print(stac.pop())
print(stac)
print(stac.getminNode())
print(stac.pop())
print(stac)
print(stac.getminNode())
print(stac.pop())
print(stac)
print(stac.getminNode())
print(stac.pop())
print(stac)
print(stac.getminNode())
print(stac.pop())
print(stac)
print(stac.getminNode())
print(stac.pop())
print(stac)
print(stac.getminNode())
print(stac.pop())
print(stac)
print(stac.getminNode())
print(stac.pop())
        
        


        
        
        
        
        