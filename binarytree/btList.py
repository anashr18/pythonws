class BinaryTree:
    def __init__(self, size):
        self.list = size*[None]
        self.maxSize = size
        self.lastUsedIndex=0
    def insertNode(self, value):
        if self.lastUsedIndex+1==self.maxSize:
            print("The tree is full")
            return
        self.list[self.lastUsedIndex+1] = value
        self.lastUsedIndex+=1
    def preOrderTraversal(self, index=1):
        if index >= self.maxSize:
            return 
        print(self.list[index])
        self.preOrderTraversal(2*index)
        self.preOrderTraversal(2*index+1)
    def inOrderTraversal(self, index=1):
        if index > self.lastUsedIndex:
            return 
        self.inOrderTraversal(2*index)
        print(self.list[index])
        self.inOrderTraversal(2*index+1)
    def postOrderTraversal(self, index=1):
        if index > self.lastUsedIndex:
            return 
        self.postOrderTraversal(2*index)
        self.postOrderTraversal(2*index+1)
        print(self.list[index])
    def levelOrderTraversal(self, index=1):
        print([val for val in self.list])
    def deleteNode(self, value):
        for idx, val in enumerate(self.list):
            if val==value:
                self.list[idx] = self.list[self.lastUsedIndex]
                self.list[self.lastUsedIndex]= None
                self.lastUsedIndex-=1
                print("node deleted")
                return
        print("not found.")

        
# newBT = BinaryTree(6)
newBT = BinaryTree(8)
newBT.insertNode("Drinks")
newBT.insertNode("Hot")
newBT.insertNode("Cold")
newBT.insertNode("Tea")
newBT.insertNode("Coffee")
newBT.preOrderTraversal()
newBT.inOrderTraversal()
newBT.postOrderTraversal()
newBT.levelOrderTraversal()
newBT.deleteNode("Hot")
newBT.levelOrderTraversal()
