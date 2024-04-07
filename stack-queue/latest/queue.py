class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue:
    def __init__(self, value):
        newNode = Node(value)
        self.first = newNode
        self.last = newNode
        self.length = 1

    def enqueue(self, value):
        newNode = Node(value)
        if self.first is None:
            self.first = self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        self.length += 1

    def dequeue(self):
        if self.first is None:
            return None
        node = self.first
        if self.first == self.last:
            self.first = self.last = None
        self.first = node.next
        node.next = None
        return node


my_queue = Queue(1)
my_queue.enqueue(2)

# (2) Items - Returns 2 Node
print(my_queue.dequeue().value)
# (1) Item -  Returns 1 Node
print(my_queue.dequeue().value)
# (0) Items - Returns None
print(my_queue.dequeue())
