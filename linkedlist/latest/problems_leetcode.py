from icecream import ic


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

    def appendAll(self, *values):
        node = self.head
        while node.next:
            node = node.next
        for value in values:
            newNode = Node(value)
            node.next = newNode
            node = node.next
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

    def remove(self, idx):
        if idx < 0:
            print("index can not be negative")
            return

        node = self.head
        prev = None
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        length = 0
        # for _ in range(idx):
        while node and length < idx:
            prev = node
            node = node.next
            length += 1
        if node is None and length < idx:
            print("index out of bounds")
            return
        prev.next = node.next
        if idx == 0:
            self.head = dummy.next

    def find_middle_node(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.value)
        pass

    def has_loop(self):
        slow = fast = self.head
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        pass

    def find_k_from_end(self, k):
        start = end = self.head
        length = 1
        # for _ in range(k):
        while end and length < k:
            end = end.next
            length += 1
        if length < k and end is None:
            print("index out of bounds in finding the kth term")
            return
        if end is None:
            print(start.value)
            return
        while end.next:
            start = start.next
            end = end.next
        print(start.value)

    def partition_list(self, value):
        node = self.head
        lessHead = greaterHead = lessTail = greaterTail = None
        while node:
            next_node = node.next
            node.next = None
            if node.value < value:
                if lessHead is None:
                    lessHead = lessTail = node

                else:
                    lessTail.next = node
                    lessTail = node
            else:
                if greaterHead is None:
                    greaterHead = greaterTail = node
                else:
                    greaterTail.next = node
                    greaterTail = node
            node = next_node
        if lessHead:
            lessTail.next = greaterHead
            self.head = lessHead
        else:
            self.head = greaterHead
        pass

    def remove_duplicate(self):
        if self.head is None or self.head.next is None:
            print("list has to be more than length of 1")
        listSet = set()
        node = self.head.next
        prev = self.head
        listSet.add(self.head.value)
        while node:
            if node.value in listSet:
                prev.next = node.next
            else:
                listSet.add(node.value)
                prev = node
            node = node.next
        pass

    def binary_to_decimal(self):
        node = self.head
        idx = sum = 0
        while node:
            sum += node.value * 2
            idx += 1
            node = node.next
        return sum
        pass

    def reverse_between(self, start, end):
        node = self.head
        before = None
        dummy = Node(0)
        dummy.next = self.head
        before = dummy
        for _ in range(start):
            before = node
            node = node.next
        for _ in range(end - start):
            after = node.next
            node.next = after.next
            after.next = before.next
            before.next = after
            # node=node.next
        if start == 0:
            self.head = dummy.next
        pass

    def reverse(self):
        node = self.head
        before = None
        while node:
            after = node.next
            node.next = before
            before = node
            node = after
        self.head = before


my_linked_list = LinkedList(84)
values = [120, 56, 67, 91, 48, 12, 13]
my_linked_list.appendAll(*values)
my_linked_list.appendAll(59)

my_linked_list.print_list()
my_linked_list.reverse_between(0, 8)
my_linked_list.print_list()
my_linked_list.reverse()
my_linked_list.print_list()
