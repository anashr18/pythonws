class MultiStack:
    def __init__(self, stackSize, numStacks):
        self.stacksize = stackSize
        self.numStacks = numStacks
        self.custList = [0]* (self.numStacks*self.stacksize)
        self.sizes = [0]* (self.numStacks)
    def isFull(self, stackNum):
        if self.sizes[stackNum] == self.stacksize:
            return True
        return False
    def isEmpty(self, stackNum):
        if self.sizes[stackNum] == 0:
            return True
        return False
    def push(self, stackNum, value):
        if self.isFull(stackNum):
            return "The stack " + str(stackNum) +" is full"
        else:
            index = self.stacksize*(stackNum)
            index += self.sizes[stackNum]
            self.custList[index] = value
            self.sizes[stackNum]+=1
    def pop(self, stackNum):
        if self.isEmpty(stackNum):
            return "The stack " + str(stackNum) +" is Empty"
        else:
            index = self.stacksize*(stackNum)
            index += self.sizes[stackNum]-1
            value = self.custList[index]
            self.sizes[stackNum]-=1
            return value
    
customStack = MultiStack(3,6)
print(customStack.isFull(0))
print(customStack.isEmpty(1))
customStack.push(0, 100)
customStack.push(0, 120)
customStack.push(0, 130)
customStack.push(0, 140)
customStack.push(1, 200)
customStack.push(3, 300)
print(customStack.pop(0))
print(customStack.pop(0))
print(customStack.pop(0))
print(customStack.pop(0))
