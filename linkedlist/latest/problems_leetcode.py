class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def print_list(self):
        print(("->").join([str(node.value) for node in self]))

    def appendAll(self, values):
        pass

    def insert(self, value, idx):
        newNode = Node(value)
        dummy = Node(0)
        dummy.next = self.head
        currNode = dummy
        for _ in range(idx):
            currNode = currNode.next
        newNode.next = currNode.next
        currNode.next = newNode
        if idx == 0:
            self.head = dummy.next


my_linked_list = LinkedList(4)
values = [2, 5, 6, 9, 10, 12, 13]
# my_linked_list.appendAll(*values)
# my_linked_list.appendAll(56, 43, 21, 98)

my_linked_list.print_list()
my_linked_list.insert(2, 1)
my_linked_list.print_list()
my_linked_list.insert(6, 1)
my_linked_list.print_list()
my_linked_list.insert(10, 0)
my_linked_list.print_list()
