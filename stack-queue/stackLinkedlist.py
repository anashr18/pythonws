class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LList:
    def __init__(self):
        self.head=None
        # self.tail=None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
class Stack:
    def __init__(self):
        self.llist = LList()
    def __str__(self):
        values = [str(node.value) for node in self.llist]
        return "\n".join(values)
        # return str([node.value for node in self.llist])
    def push(self, value):
        node = Node(value)
        node.next = self.llist.head
        self.llist.head = node
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        value = self.llist.head.value
        self.llist.head = self.llist.head.next
        return value
    def isEmpty(self):
        return self.llist.head is None
stac = Stack()
stac.push(100)
stac.push(90)
stac.push(50)
stac.push(40)
stac.push(10)
print(stac)
stac.pop()
stac.pop()
stac.pop()
print(stac)