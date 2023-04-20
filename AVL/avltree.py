class AVLNode:
    def __init__(self, value):
        self.value=value
        self.leftChild=None
        self.rightChild=None
        self.height=1
    def __str__(self):
        return str(self.value)
def preOrderTraversal(root):
    if root is None:
        return
    print(root.value)
    preOrderTraversal(root.leftChild)        
    preOrderTraversal(root.rightChild)        
def inOrderTraversal(root):
    if root is None:
        return
    inOrderTraversal(root.leftChild)        
    print(root.value)
    inOrderTraversal(root.rightChild)        
def postOrderTraversal(root):
    if root is None:
        return
    postOrderTraversal(root.leftChild)        
    postOrderTraversal(root.rightChild)        
    print(root.value)
# def levelOrderTraversal(root):
#     if root is None:
#         return
#     print(root.value)
#     levelOrderTraversal(root.left)        
#     levelOrderTraversal(root.right)     
def getHeight(root):
    if root is None:
        return 0
    return root.height   
def getBalance(root):
    balance = getHeight(root.leftChild)-getHeight(root.rightChild)
    return balance
def insert(root, value):        
    # add node
    # check if imbalnce
        # height difference of nodes 
    # rotate if required 
        # LL-right roation at disbalance node
        # RR-left roation at disbalance node
        # LR-left rotation at child node and then it becomes RR, Consequently perform left rotation at disbalance node.
        # RL-right rotation at child node and then it becomes LL, Consequently perform right rotation at disbalance node.
    if root is None:
        root = AVLNode(value)
        print(str(root)+" inserting node ")
        return root
    else:
        if value<root.value:
            root.leftChild =insert(root.leftChild, value)
        else:
            root.rightChild=insert(root.rightChild, value)
    # check if imbalnce
    # height is calculated in such a way that node has the highest height
    root.height = 1+max(getHeight(root.leftChild), getHeight(root.rightChild))
    balance = getBalance(root)
    print("root "+str(root)+" Balance "+str(balance))
    if balance>1 and getBalance(root.leftChild)==1:
        # LL--right rotate
        print("LL Right Rotating "+str(root))
        root=rightRotate(root)
    elif balance>1 and getBalance(root.leftChild)==-1:
        # LR
        print("LR Left Rotating "+str(root.leftChild))
        root=leftRotate(root.leftChild) #leftrotate at child
        # now it becomes LL
        print("LL Left Rotating "+str(root))
        root=rightRotate(root)
    elif balance<-1 and getBalance(root.rightChild)==-1:
        # RR--left rotate
        print("RR Right Rotating "+str(root))
        root=leftRotate(root)
    elif balance<-1 and getBalance(root.rightChild)==1:
        # RL
        print("RL right Rotating "+str(root.rightChild))
        root.rightChild=rightRotate(root.rightChild) #rightrotate at child
        # now it becomes RR
        print("RR left Rotating "+str(root))
        root=leftRotate(root)
    return root
def leftRotate(root):
    newRoot = root.rightChild
    root.rightChild=None
    newRoot.leftChild=root
    newRoot.height=1+max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    root.height=1+max(getHeight(root.leftChild), getHeight(root.rightChild))
    return newRoot
def rightRotate(root):
    newRoot = root.leftChild
    root.leftChild=None
    newRoot.rightChild=root
    newRoot.height=1+max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    root.height=1+max(getHeight(root.leftChild), getHeight(root.rightChild))
    return newRoot
def delete(root, value):
    if root is None:
        return root
    if value<root.value:
        root.leftftChild=delete(root.leftChild, value)
    elif value>root.value:
        root.rightChild=delete(root.rightChild, value)
    else:
        if root.leftChild is None:
            temp=root.rightChild
            root=None
            return temp
        elif root.rightChild is None:
            temp=root.leftChild
            root=None
            return temp
        temp=getMinValue(root.rightChild)
        root.value = temp
        # delete the minvalue node
        root.rightChild = delete(root.rightChild, temp)
    balance = getBalance(root)
    if balance > 1 and getBalance(root.leftChild) >= 0:
        return rightRotate(root)
    if balance < -1 and getBalance(root.rightChild) <= 0:
        return leftRotate(root)
    if balance > 1 and getBalance(root.leftChild) < 0:
        root.leftChild = leftRotate(root.leftChild)
        return rightRotate(root)
    if balance < -1 and getBalance(root.rightChild) > 0:
        root.rightChild = rightRotate(root.rightChild)
        return leftRotate(root)
    
    return root

def getMinValue(root):
    while root.leftChild:
        root=root.leftChild
    return root.value
avl = AVLNode(100)
avl = insert(avl, 200)
avl = insert(avl, 90)
avl = insert(avl, 800)
avl = insert(avl, 700)
avl = insert(avl, 80)
avl = insert(avl, 70)
preOrderTraversal(avl)