class Queue:
    def __init__(self, max_size):
        self.items = max_size*[None]
        self.max_size = max_size
        self.start = -1
        self.top = -1
    def __iter__(self):
        for value in self.items:
            yield value
    def isFull(self):
        if self.top+1 == self.start:
            return True
        if self.start==0 and self.top+1==self.max_size:
            return True
        return False
    def isEmpty(self):
        if self.top ==-1:
            return True
        return False
    def enqueue(self, value):
        if self.isFull():
            return "The queue is full"
        else:
            if self.top + 1 == self.max_size:
                self.top=0
            else:
                self.top+=1
                if self.start==-1:
                    self.start=0
            self.items[self.top] = value
    def dequeue(self):
        if self.isEmpty():
            return "The Queue is empty"
        else:
            firstElem = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start=-1
                self.top=-1
            elif self.start+1 ==self.max_size:
                self.start = 0
            else:
                self.start+=1
            self.items[start] = None

q1 = Queue(6)
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q1.enqueue(5)
print(q1.enqueue(6))
print(q1.enqueue(7))
print([value for value in q1])
q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.dequeue()
print([value for value in q1])
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
print([value for value in q1])

