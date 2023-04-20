# min or max binary heap can be made 
class BinaryHeap:
    def __init__(self, size):
        self.customList = (size+1)*[None]
        self.heapSize=0
        self.maxSize = size+1
def levelOrderTraversal(tree):
    for i in range(1, tree.heapSize+1):
        print(tree.customList[i], sep="->")
def insert(tree, value, heapType="min"):
    if tree.heapSize+1 == tree.maxSize:
        print("The heap is full")
        return tree
    tree.customList[tree.heapSize+1]=value
    tree.heapSize+=1
    tree = heapifyTree(tree, tree.heapSize, heapType)
    return tree
def heapifyTree(tree, index, heapType):
    if index<=1:
        return tree
    parentIndex=int(index/2)
    if tree.customList[parentIndex]>tree.customList[index]:
        temp = tree.customList[parentIndex]
        tree.customList[parentIndex]=tree.customList[index]
        tree.customList[index]=temp
    tree = heapifyTree(tree, parentIndex, heapType)
    return tree

# the below method is incomplete
def extract(tree, parentIndex=1):
    if tree.heapSize==0:
        print("Tree is empty.")
    extractElem = tree.customList[parentIndex]
    tree.customList[parentIndex] = tree.customList[-1]
    tree.customList[-1]=None
    # adjust the heap-tree
    child1 = tree.customList[2*parentIndex]
    child2 = tree.customList[2*parentIndex+1]
    if child1<child2:
        temp = tree.customList[parentIndex]
        tree.customList[parentIndex]=tree.customList[2*parentIndex]
        tree.customList[2*parentIndex]=temp
        parentIndex=2*parentIndex
    else:
        temp = tree.customList[parentIndex]
        tree.customList[parentIndex]=tree.customList[2*parentIndex+1]
        tree.customList[2*parentIndex+1]=temp
        parentIndex=2*parentIndex+1
    extract(tree, parentIndex)
    return extractElem
    

heap = BinaryHeap(7)
heap=insert(heap, 5)
heap=insert(heap, 10)
heap=insert(heap, 20)
heap=insert(heap, 30)
heap=insert(heap, 40)
heap=insert(heap, 50)
heap=insert(heap, 60)
heap=insert(heap, 80)
levelOrderTraversal(heap)
