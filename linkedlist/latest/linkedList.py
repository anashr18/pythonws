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

        while pos < idx - 1:
            node = node.next
            pos += 1
        node.next = node.next.next


# ll = LinkedList(2)
# values = [2, 5, 6, 9, 10, 12, 13]
# ll.appendAll(*values)
# ll.appendAll(56, 43, 21, 90)

# ll.printall()


##########################################################
##   Test code below will print output to "User logs"   ##
##########################################################

my_linked_list = LinkedList(1)
my_linked_list.append(3)


print("LL before insert():")
my_linked_list.print_list()
print(my_linked_list.head.value, my_linked_list.tail.value)

my_linked_list.insert(1, 2)
print(my_linked_list.head.value, my_linked_list.tail.value)

print("\nLL after insert(2) in middle:")
my_linked_list.print_list()
print(my_linked_list.head.value, my_linked_list.tail.value)

my_linked_list.insert(0, 0)
print(my_linked_list.head.value, my_linked_list.tail.value)
print("\nLL after insert(0) at beginning:")
my_linked_list.print_list()
print(my_linked_list.head.value, my_linked_list.tail.value)

my_linked_list.insert(4, 4)

print("\nLL after insert(4) at end:")
my_linked_list.print_list()
print(my_linked_list.head.value, my_linked_list.tail.value)
