from icecream import ic


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self, value) -> None:
        self.top = Node(value)
        self.height = 1

    def push(self, value):
        newNode = Node(value)
        if self.top is None:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        self.height += 1

    def print_stack(self):
        result = []
        node = self.top
        while node:
            result.append(str(node.value))
            node = node.next
        print(("->").join(result))
        pass

    def pop(self):
        if self.top is None:
            return
        node = self.top
        self.top = node.next
        node.next = None
        return node
        pass


my_stack = Stack(4)
my_stack.push(3)
my_stack.push(2)
my_stack.push(1)

print("Stack before pop():")
my_stack.print_stack()

print("\nPopped node:")
print(my_stack.pop().value)

print("\nStack after pop():")
my_stack.print_stack()
