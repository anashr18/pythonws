# class Node:
#     def __init__(self, value)

from icecream import ic


class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        print(("->").join(self.stack_list))

    def push(self, value):
        self.stack_list.append(str(value))

    def pop(self):
        if len(self.stack_list) == 0:
            return None
        return self.stack_list.pop()

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]


def is_balanced_parentheses(inputs):
    stack = Stack()
    for char in inputs:
        if char == "(":
            stack.push(char)
        else:
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()
    pass


def reverse(self, input):
    stack = Stack()
    result = ""
    for char in input:
        stack.push(char)
    while stack.is_empty():
        result += stack.pop()
    return result
    pass


def sort(stack: Stack):
    sorted_stack = Stack()
    while not stack.is_empty():
        temp = stack.pop()
        while not sorted_stack.is_empty() and sorted_stack.peek() > temp:
            ic(temp, sorted_stack.print_stack(), stack.print_stack())
            sorted_temp = sorted_stack.pop()
            stack.push(sorted_temp)
            ic(temp, sorted_stack.print_stack(), stack.print_stack())
        sorted_stack.push(temp)
        ic(temp, sorted_stack.print_stack(), stack.print_stack())
    return sorted_stack
    pass


my_stack = Stack()
inputs = "(()"
# print(is_balanced_parentheses(inputs))
my_stack.push(1)
my_stack.push(5)
my_stack.push(2)
my_stack.push(8)
my_stack.push(4)
my_stack.push(7)
my_stack.push(6)
my_stack.push(3)

# sorted_stack, stack = sort(my_stack)
sorted_stack = sort(my_stack)
sorted_stack.print_stack()
# stack.print_stack()
