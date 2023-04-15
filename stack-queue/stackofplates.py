# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next
from random import randint
class StackPlate:
    def __init__(self, capacity=2):
        self.capacity = capacity
        self.stack = []
    # def __iter__(self):
    #     temp = self.top
    #     while temp:
    #         yield temp
    #         temp = temp.next
    def __str__(self):
        values = [str(value) for value in self.stack]
        return "->".join(values)
    def push(self, value):
        if len(self.stack)>0 and len(self.stack[-1]) < self.capacity:
            self.stack[-1].append(value)
        else:
            self.stack.append([value])
    def pop(self):
        while len(self.stack) and len(self.stack[-1])==0:
            self.stack.pop()
        if len(self.stack)==0:
            return None
        else:
           return self.stack[-1].pop()
    def generate(self, n, min, max):
        for _ in range(n):
            self.push(randint(min, max))
        return self
    def popAtIndex(self, idx):
        # idx-=1  
        if len(self.stack)<=idx-1:
            print("The stack at index "+str(idx)+" does not exist")
            return
        if len(self.stack[idx-1]) >0:
            return self.stack[idx-1].pop()
        else:
            return None
sp = StackPlate()
sp = sp.generate(7, 100, 900)
print(sp)
print(sp.popAtIndex(4))
print(sp.popAtIndex(3))
print(sp.popAtIndex(2))
print(sp.popAtIndex(2))
print(sp)
print("here")
print(sp.pop())
print(sp)
print(sp.pop())
print(sp)
print(sp.pop())
print(sp)
print(sp.pop())
print(sp)
print(sp.pop())
print(sp)
print(sp.pop())
print(sp)
print(sp.pop())


        