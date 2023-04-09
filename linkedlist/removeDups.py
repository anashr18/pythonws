# import Node from LinkedList
# import CustomLL from LinkedList
import LinkedList as LList

ll = LList.CustomLL([12, 14, 17 , 19 , 20, 31, 102, 56, 109, 19])

def removeDups(ll):
    # print(ll.head)
    visited = {}
    currNode = ll.head
    visited[ll.head.value] = 0
    while currNode.next:
        if currNode.next.value in visited:
            currNode.next = currNode.next.next
            break
        else:
            visited[currNode.next.value] = 0
            currNode = currNode.next   
    return ll

print(removeDups(ll))

def kThFromTheLast(ll, n):
    currNode1 = ll.head
    currNode2 = ll.head
    for i in range(n):
        if currNode2 is None:
            return None
        currNode2 = currNode2.next
    while currNode2:
        currNode2 = currNode2.next
        currNode1 = currNode1.next
    return currNode1
print(kThFromTheLast(ll,9))

# def kThFromTheLast(ll, n):
#     currNode = ll.head
#     value = 0
#     print(len(ll))
#     for i in range(len(ll)-n+1):
#         value = currNode
#         currNode = currNode.next
#     return value
# print(kThFromTheLast(ll,3))



