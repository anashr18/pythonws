# import Node from LinkedList
# import CustomLL from LinkedList
import LinkedList as LList

# ll = LList.CustomLL([12, 14, 17 , 19 , 20, 31, 102, 56, 109, 19])

# def removeDups(ll):
#     # print(ll.head)
#     visited = {}
#     currNode = ll.head
#     visited[ll.head.value] = 0
#     while currNode.next:
#         if currNode.next.value in visited:
#             currNode.next = currNode.next.next
#             break
#         else:
#             visited[currNode.next.value] = 0
#             currNode = currNode.next   
#     return ll

# print(removeDups(ll))

# def kThFromTheLast(ll, n):
#     currNode1 = ll.head
#     currNode2 = ll.head
#     for i in range(n):
#         if currNode2 is None:
#             return None
#         currNode2 = currNode2.next
#     while currNode2:
#         currNode2 = currNode2.next
#         currNode1 = currNode1.next
#     return currNode1
# print(kThFromTheLast(ll,9))

# def kThFromTheLast(ll, n):
#     currNode = ll.head
#     value = 0
#     print(len(ll))
#     for i in range(len(ll)-n+1):
#         value = currNode
#         currNode = currNode.next
#     return value
# print(kThFromTheLast(ll,3))

# def partition(ll, x):
#     node = ll.head
#     ll.tail = ll.head
#     while node:
#         next = node.next
#         if node.value <x:
#             node.next = ll.head
#             ll.head = node
#         else:
#             ll.tail.next = node
#             ll.tail = node
#         node = next    
#     if ll.tail.next is not None:
#         ll.tail.next = None

# ll1 = LList.CustomLL().generate(10, 1, 99)
# print(ll1)
# partition(ll1, 50)
# print(ll1)

lla = LList.CustomLL().generate(7,0,9)
llb = LList.CustomLL().generate(10,0,9)

def sumLists(lla, llb):
    print(lla)
    print(llb)
    n1 = lla.head
    n2 = llb.head
    ll = LList.CustomLL()
    carry = 0
    while n1 or n2  or carry!=0:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
        carry = int(result/10)
        ll.addLL(int(result%10))
    
    return ll

llA = LList.CustomLL()
llA.addLL(9)
llA.addLL(9)
llA.addLL(9)


llB = LList.CustomLL()
llB.addLL(9)
llB.addLL(9)
llB.addLL(9)
print(sumLists(lla, llb))
# print(sumLists(llA, llA))
    
def intersection(lla, llb):

    lenA = len(lla)
    lenB = len(llb)
    longerList = lla if lenA > lenB else llb
    shorterList = lla if lenA < lenB else llb
    longerNode = longerList.head
    shorterNode = shorterList.head
    for i in range(len(longerList)-len(shorterList)):
        longerNode=longerNode.next
    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next
    return longerNode

def addCommonNode(lla, llb, value):
    newNode = LList.Node(value)
    lla.tail.next = newNode
    lla.tail = newNode
    llb.tail.next = newNode
    llb.tail = newNode

llA = LList.CustomLL()
llA.generate(3,0, 10)

llB = LList.CustomLL()
llB.generate(7,0, 10)

addCommonNode(llA, llB, 11)
addCommonNode(llA, llB, 14)
addCommonNode(llA, llB, 23)
addCommonNode(llA, llB, 45)

print(llA)
print(llB)

print(intersection(llA, llB))
# print(intersection())