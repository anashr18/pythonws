from icecream import ic


class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class Dll:
    def __init__(self, value) -> None:
        self.head = Node(value)
        pass

    def append(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
        else:
            prev = None
            node = self.head
            while node.next:
                prev = node
                node = node.next
            node.next = newNode
            node.prev = prev

    def print_list(self):
        result = []
        node = self.head
        while node:
            result.append(str(node.value))
            node = node.next
        print(("->").join(result))

    def appendAll(self, *values):
        for value in values:
            self.append(value)
        pass

    def pop(self):
        node = self.head
        prev = None
        while node.next:
            prev = node
            node = node.next
        prev.next = None
        node.prev = None
        pass

    def prepend(self, value):
        # node = self.head
        newNode = Node(value)
        self.head.prev = newNode
        newNode.next = self.head
        self.head = newNode
        pass

    def pop_first(self):
        node = self.head
        nextNode = node.next
        nextNode.prev = None
        node.next = None
        self.head = nextNode
        print(node.value)

    def insert(self, idx, value):
        # node = self.head
        # prev = None
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        # length = 0
        while node and length < idx:
            prev = node
            node = node.next
            length += 1
        if node is None and length < idx:
            print("idx out of bounds")
            return
        newNode = Node(value)
        newNode.next = node
        newNode.prev = prev
        prev.next = newNode
        if node:
            node.prev = newNode
        # else:
        if idx == 0:
            self.head = dummy.next
        if self.head:
            self.head.prev = None
        pass


my_linked_list = Dll(84)
values = [120, 56, 67, 91, 48, 12, 13]
my_linked_list.appendAll(*values)
my_linked_list.appendAll(59)
my_linked_list.print_list()
my_linked_list.insert(3, 99)
my_linked_list.print_list()
my_linked_list.insert(6, 88)
my_linked_list.print_list()
my_linked_list.insert(0, 188)
my_linked_list.print_list()
my_linked_list.insert(0, 111)
my_linked_list.print_list()
my_linked_list.insert(14, 222)
my_linked_list.print_list()
my_linked_list.insert(13, 333)
my_linked_list.print_list()
