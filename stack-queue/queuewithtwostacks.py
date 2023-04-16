from random import randint
class Queue:
    def __init__(self):
        self.stack_a = []
        self.stack_b = []
    def __str__(self):
        values_a = [str(val) for val in self.stack_a]
        res = "->".join(values_a)
        if len(self.stack_b):
            res+="\n"
            values_b = [str(val) for val in self.stack_b]
            res+= "->".join(values_b)
        return res
    def enqueue(self, value):
        self.stack_a.append(value)
    def dequeue(self):
        for _ in range(len(self.stack_a)):
            self.stack_b.append(self.stack_a.pop())
        val = self.stack_b.pop()
        for _ in range(len(self.stack_b)):
            self.stack_a.append(self.stack_b.pop())
        return val 
    def generate(self, n , a, b):
        for _ in range(n):
            self.enqueue(randint(a, b))
        return self
q1 = Queue()
q1.generate(9, 10, 100)
print(q1)
print(q1.dequeue())
print(q1)
print(q1.dequeue())
print(q1)
print(q1.dequeue())
print(q1)
print(q1.dequeue())
print(q1)
print(q1.dequeue())
print(q1)

        