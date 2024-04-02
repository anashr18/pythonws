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

    def print_list(self):
        print(("->").join([str(node.value) for node in self]))

    def append(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1

    def appendAll(self, *values):
        for value in values:
            self.append(value)
            # self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        node = self.head
        prev = node
        while node.next:
            prev = node
            node = node.next
        prev.next = None
        self.tail = prev
        self.length -= 1
        return node

    def prepend(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.head == self.tail:
            self.tail = None
        self.head = self.head.next
        self.length -= 1
        temp.next = None
        return temp

    def get(self, idx):
        if idx < 0 or idx > self.length - 1:
            return None
        pos = 0
        node = self.head
        while pos < idx:
            node = node.next
            pos += 1
        return node

    def set_value(self, idx, value):
        if self.length == 0:
            return
        node = self.head
        pos = 0
        while pos < idx:
            pos += 1
            node = node.next
        node.value = value

    def insert(self, idx, value):
        if idx < 0 or idx > self.length:
            return
        newNode = Node(value)
        if idx == 0:
            newNode.next = self.head
            self.head = newNode
        else:
            node = self.head
            pos = 0
            while pos < idx - 1:
                node = node.next
                pos += 1
            newNode.next = node.next
            node.next = newNode
            if newNode.next is None:
                self.tail = newNode
        self.length += 1

    def remove(self, idx):
        if idx < 0 or idx > self.length - 1:
            return
        node = self.head
        pos = 0
        temp = None
        if idx == 0:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            if self.tail == temp:
                self.tail = None
        else:
            while pos < idx - 1:
                node = node.next
                pos += 1
            if node.next == self.tail:
                temp = node.next
                self.tail = node
                self.tail.next = None
            else:
                temp = node.next
                node.next = node.next.next
        self.length -= 1
        return temp

    def reverse(self):
        if self.length == 0:
            return
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        while temp:
            # init after counter
            after = temp.next
            # reversing the link
            temp.next = before
            # incrementing before counters
            before = temp
            # incrementing temp counter
            temp = after


my_linked_list = LinkedList(2)
values = [2, 5, 6, 9, 10, 12, 13]
my_linked_list.appendAll(*values)
my_linked_list.appendAll(56, 43, 21, 90)

my_linked_list.print_list()


##########################################################
##   Test code below will print output to "User logs"   ##
##########################################################

# my_linked_list = LinkedList(1)
# my_linked_list.append(3)


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

print("LL before reverse():")
my_linked_list.print_list()

my_linked_list.reverse()

print("\nLL after reverse():")
my_linked_list.print_list()
