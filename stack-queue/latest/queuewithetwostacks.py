class Stack:
    def __init__(self) -> None:
        self.stack_list = []

    def is_empty(self):
        return len(self.stack_list) == 0

    def push(self, value):
        self.stack_list.append(value)
        pass

    def pop(self):
        if len(self.stack_list) == 0:
            return None
        return self.stack_list.pop()
        pass

    def print_stack(self):
        print(*self.stack_list, sep="\n")


class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        # Always push new elements onto stack1
        self.stack1.push(value)

    def dequeue(self):
        # If stack2 is empty, move all elements from stack1 to stack2
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        # Pop from stack2, which contains the oldest element
        return self.stack2.pop()

    def print_queue(self):
        # Print the contents of stack2 (which needs to be reversed to show the queue order)
        # If stack2 is empty and elements are in stack1, they need to be moved for correct display
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        print(list(reversed(self.stack2.print_stack())))


my_queue = Queue()
my_queue.enqueue(2)
my_queue.enqueue(4)
my_queue.enqueue(5)
my_queue.print_queue()
my_queue.dequeue()
my_queue.print_queue()
my_queue.dequeue()
my_queue.print_queue()
my_queue.dequeue()
my_queue.print_queue()
