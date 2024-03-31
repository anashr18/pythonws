class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value) -> None:
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def printall(self):
        print(("->").join([node.value for node in self]))
