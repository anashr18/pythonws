from icecream import ic


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value) -> None:
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        # self.length = 1

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def print_list(self):
        print(("->").join([str(node.value) for node in self]))

    def append(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        # self.length += 1

    def appendAll(self, *values):
        for value in values:
            self.append(value)

    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def has_loop(self):
        slow = self.head
        fast = self.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def partition_list(self, x):
        less_head = less_tail = None
        greater_head = greater_tail = None
        current = self.head

        while current:
            nextNode = current.next
            current.next = None
            if current.value < x:
                if not less_head:
                    less_head = less_tail = current
                else:
                    less_tail.next = current
                    less_tail = current
            else:
                if not greater_head:
                    greater_head = greater_tail = current
                else:
                    greater_tail.next = current
                    greater_tail = current
            current = nextNode
        if not less_head:
            self.head = greater_head
        else:
            less_tail.next = greater_head
            self.head = less_head

    def remove_duplicates(self):
        if self.head is None or self.head.next is None:
            return self.head
        currNode = self.head.next
        prevNode = self.head
        item_set = set()
        item_set.add(prevNode.value)
        while currNode:
            if currNode.value in item_set:
                prevNode.next = currNode.next
            else:
                item_set.add(currNode.value)
                prevNode = currNode
            currNode = currNode.next
        # print(item_set)
        # pass

    def binary_to_decimal(self):
        result = 0
        node = self.head
        while node:
            result = 2 * result + node.value
            node = node.next
        return result

    def reverse_between(self, start, end):
        # adding a dummy
        dummy = Node(0)
        dummy.next = self.head
        before = dummy
        for _ in range(start):
            ic(before.value)
            before = before.next
            ic(before.value, dummy.next.value)
        temp = before.next
        for _ in range(end - start):
            after = temp.next
            temp.next = after.next
            after.next = before.next
            before.next = after
            ic(before.value, temp.value, after.value, self.head.value, dummy.next.value)
        if start == 0:
            # self.head = before.next
            self.head = dummy.next


def find_kth_from_end(ll, k):
    slow = ll.head
    fast = ll.head
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    return slow


my_linked_list = LinkedList(4)
values = [2, 5, 6, 9, 10, 12, 13]
my_linked_list.appendAll(*values)
# my_linked_list.appendAll(56, 43, 21, 98)

my_linked_list.print_list()
my_linked_list.reverse_between(2, 6)
my_linked_list.print_list()
