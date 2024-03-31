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

    def append(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1

    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next

    def printll(self):
        print(("->").join([str(node.value) for node in self]))

    def insert(self, value, loc=-1):
        # assert loc < self.length, "loc should be within length of LL"
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
            self.length = 1
        elif loc == -1:
            self.tail.next = newNode
            self.tail = newNode
            self.length += 1
        else:
            tempNode = self.head
            idx = 0
            while idx < loc - 1:
                tempNode = tempNode.next
                idx += 1
            newNode.next = tempNode.next
            tempNode.next = newNode
            self.length += 1
            if tempNode == self.tail:
                self.tail = newNode

    def delete(self, loc=-1):
        if self.length == 0:
            print("LL is empty")
            return
        else:
            tempNode = self.head
            idx = 0
            if loc == -1:
                loc = self.length - 1
            while idx < loc - 1:
                tempNode = tempNode.next
                idx += 1
            if loc == 0:
                temp = self.head.next
                self.head.next = None
                self.head = temp
                if self.head is None:
                    self.tail = None
            else:
                tempNode.next = tempNode.next.next
            self.length -= 1


ll = LinkedList(3)
ll.append(22)
ll.append(21)
ll.append(26)
ll.printll()
ll.insert(100)
ll.insert(200)
ll.printll()
ll.insert(300, 0)
ll.insert(400, 0)
ll.printll()
ll.insert(500, 4)
ll.insert(98100, 7)
ll.printll()
print(f"{ll.head.value} {ll.tail.value}")
# ll.delete(0)
# ll.printll()
ll.delete()
ll.delete()
ll.delete()
ll.delete()
ll.delete(0)
ll.delete(0)
ll.delete(2)
ll.delete(2)
ll.printll()
ll.delete()
ll.printll()
ll.delete()
ll.delete()
ll.printll()
