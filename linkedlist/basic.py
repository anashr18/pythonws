class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    def insertSLL(self, loc, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if loc==0:
                newNode.next = self.head
                self.head = newNode
            elif loc==-1:
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < loc-1:
                    tempNode = tempNode.next
                    index+=1
                newNode.next = tempNode.next
                tempNode.next = newNode
                if tempNode == self.tail:
                    self.tail = newNode
    def traverseSLL(self):
        if self.head is None:
            print("SLL is empty")
        else:
            node = self.head
            while node is not None:
                print(str(node.value)+" ")
                node = node.next
    def deleteSLL(self, loc):
        
        if loc==0:
            if self.head ==self.tail:
                self.head=None
                self.tail=None
            else:
                self.head = self.head.next
        elif loc==-1:
            if self.head ==self.tail:
                self.head=None
                self.tail=None
            else:
                node = self.head
                while node is not None:
                    if node.next == self.tail:
                        break
                    node = node.next
                self.tail = None
                self.tail = node
        else:
            tempNode = self.head
            index=0
            while index <loc-1:
                index+=1
                tempNode = tempNode.next
            nextNode = tempNode.next
            tempNode.next = nextNode.next
sll = SLL()
sll.insertSLL(0,100)
sll.insertSLL(0,80)
sll.insertSLL(0,50)
sll.insertSLL(0,10)
print([node.value for node in sll])
sll.traverseSLL()
sll.deleteSLL(1)
print([node.value for node in sll])
sll.deleteSLL(2)
print([node.value for node in sll])