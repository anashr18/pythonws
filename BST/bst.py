import QueueLinkedList as Queue
class bstNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
    def __str__(self) -> str:
        return str(self.value)
    def insertNode(self, value):
        if self is None:
            self.value = value
        else:
            node = self
            while node:
                if value<node.value:
                    if node.left is None:
                        node.left=bstNode(value)
                        break
                    node=node.left
                else:
                    if node.right is None:
                        node.right=bstNode(value)
                        break
                    node=node.right
        return self
def preOrderTraversal(root):
    if root is None:
        return 
    print(root.value)
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)
def inOrderTraversal(root):
    if root is None:
        return 
    inOrderTraversal(root.left)
    print(root.value)
    inOrderTraversal(root.right)
def postOrderTraversal(root):
    if root is None:
        return 
    postOrderTraversal(root.left)
    postOrderTraversal(root.right)
    print(root.value)
def levelOrderTraversal(root):
    if root is None:
        return 
    queue = Queue.Queue()
    queue.enqueue(root)
    while not queue.isEmpty():
        node = queue.dequeue()
        print(node.value.value)
        if node.value.left is not None:
            queue.enqueue(node.value.left)
        if node.value.right is not None:
            queue.enqueue(node.value.right)
def deleteNode(root, value):
    if root is None:
        return 
    parentNode=None
    node=root
    while True:
        if value< node.value:
            parentNode=node
            node=node.left
        elif value>node.value:
            parentNode=node
            node=node.right
        else:
            # found the node
            # leaf node
            if node.left==None and node.right==None:
                print("leaf node")
                if parentNode.left==node:
                    parentNode.left=None
                else:
                    parentNode.right=None
                break
            # node with two children -successor 
            
            elif node.left is not None and node.right is not None:
                print("successor")
                node.value = findSuccessor(root)
                break
            # node with 1 child
            else:
                print("1 child")
                if parentNode.left==node:
                    parentNode.left=node.left if node.left is not None else node.right
                else:
                    parentNode.right=node.right if node.right is not None else node.left
                # if node.left==None:
                #     parentNode.right=node.right
                # else:
                #     parentNode.left=node.left
                break
def findSuccessor(root):
    node=root.right
    parentNode=root
    while node.left:
        parentNode = node
        node = node.left
    if node.right is not None:
        parentNode.right=node.right
    # else:
    #     parentNode.left=None
    return node.value

bt = bstNode(100)
bt.insertNode(80)
bt.insertNode(180)
bt.insertNode(800)
bt.insertNode(10)
bt.insertNode(60)
bt.insertNode(5)
bt.insertNode(300)

# preOrderTraversal(bt)
# inOrderTraversal(bt)
# postOrderTraversal(bt)
levelOrderTraversal(bt)
print("^^^^^^^^^^^")
deleteNode(bt, 80)
levelOrderTraversal(bt)
