import QueueLinkedList as queue
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
    def __str__(self):
        return self.data
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
def inOrderTraversal(rootNode):
    if not rootNode:
        return 
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)
def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)    
    postOrderTraversal(rootNode.rightChild)    
    print(rootNode.data)
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    customQueue = queue.Queue()
    customQueue.enqueue(rootNode)
    while not(customQueue.isEmpty()):
        root = customQueue.dequeue()
        print(root.value.data)
        if (root.value.leftChild is not None):
            customQueue.enqueue(root.value.leftChild)
            
        if (root.value.rightChild is not None):
            customQueue.enqueue(root.value.rightChild)
def searchBT(rootNode, value):
    if not rootNode:
        return "The tree is empty"
    customQueue = queue.Queue()
    customQueue.enqueue(rootNode)
    while not customQueue.isEmpty():
        node = customQueue.dequeue()
        print(node.value.data)
        if node.value.data==value:
            return "Found the node successfully."
        if(node.value.leftChild is not None):
            customQueue.enqueue(node.value.leftChild)
        if(node.value.rightChild is not None):
            customQueue.enqueue(node.value.rightChild)
    return "Not Found"
def insertNodeBT(rootNode, value):
    if not rootNode:
        return "The tree is empty"
    customQueue = queue.Queue()
    customQueue.enqueue(rootNode)
    while not customQueue.isEmpty():
        node = customQueue.dequeue()
        print(node.value.data)
        if(node.value.leftChild is not None):
            customQueue.enqueue(node.value.leftChild)
        else:
            node.value.leftChild = TreeNode(value)
            return "Node added."
        if(node.value.rightChild is not None):
            customQueue.enqueue(node.value.rightChild)
        else:
            node.value.rightChild = TreeNode(value)
            return "Node added."
def getDeepestNodeBT(rootNode, deleteFlag=False):
    if not rootNode:
        return "The tree is empty"
    deepestNode = None
    parentNode = None
    newQueue = queue.Queue()
    newQueue.enqueue(rootNode)
    while not newQueue.isEmpty():
        node = newQueue.dequeue()
        if node.value.leftChild is not None:
            newQueue.enqueue(node.value.leftChild)
            parentNode = node
        if node.value.rightChild is not None:
            newQueue.enqueue(node.value.rightChild)
            parentNode = node
        deepestNode = node
    if deleteFlag:
        if parentNode is None:
            rootNode.data=None
            rootNode.leftChild=None
            rootNode.rightChild=None
        else:
            if parentNode.value.leftChild==deepestNode:
                parentNode.value.leftChild = None
            else:
                parentNode.value.rightChild=None 
    # else:   
    return deepestNode
# def deleteDeepestNode(rootNode):

def deleteNodeBT(rootNode, value):
    if rootNode is None:
        return "the tree is empty"
    newQueue = queue.Queue()
    newQueue.enqueue(rootNode)
    while not newQueue.isEmpty():
        node = newQueue.dequeue()
        if node.value.data==value:
            node.value.data = getDeepestNodeBT(rootNode, True).value.data
            # getDeepestNodeBT(rootNode, True)
            return "the node successfully Deleted"
        if node.value.leftChild is not None:
            newQueue.enqueue(node.value.leftChild)
        if node.value.rightChild is not None:
            newQueue.enqueue(node.value.rightChild)
newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
leftChild.leftChild = tea
leftChild.rightChild = coffee
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild
# preOrderTraversal(newBT)
# print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
# inOrderTraversal(newBT)
# print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
# postOrderTraversal(newBT)
# print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
# levelOrderTraversal(newBT)
print(searchBT(newBT, "Juice"))
# print(insertNodeBT(newBT, "Juice"))
# print(insertNodeBT(newBT, "Beer"))
levelOrderTraversal(newBT)  
print(getDeepestNodeBT(newBT))
print("))))))))))))))))))")
print(deleteNodeBT(newBT, "Drinks"))
levelOrderTraversal(newBT)



