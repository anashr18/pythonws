class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
        pass


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
        pass

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return True
        else:
            node = self.root
            while node:
                if value == node.value:
                    return False
                if value > node.value:
                    if node.right is None:
                        node.right = Node(value)
                        return True
                    node = node.right
                else:
                    if node.left is None:
                        node.left = Node(value)
                        return True
                    node = node.left

    def contains(self, value):
        if self.root is None:
            return False
        node = self.root
        while node:
            if value == node.value:
                return True
            if value > node.value:
                node = node.right
            else:
                node = node.left
        return False


def check(expect, actual, message):
    print(message)
    print("EXPECTED:", expect)
    print("RETURNED:", actual)
    print("PASS" if expect == actual else "FAIL", "\n")


print("\n----- Test: Contains on Empty Tree -----\n")
bst = BinarySearchTree()
result = bst.contains(5)
check(False, result, "Check if 5 exists in an empty tree:")

print("\n----- Test: Contains Existing Value -----\n")
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
result = bst.contains(10)
check(True, result, "Check if 10 exists:")
result = bst.contains(5)
check(True, result, "Check if 5 exists:")
result = bst.contains(15)
check(True, result, "Check if 15 exists:")

print("\n----- Test: Contains Not Existing Value -----\n")
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
result = bst.contains(15)
check(False, result, "Check if 15 exists:")

print("\n----- Test: Contains with Duplicate Inserts -----\n")
bst = BinarySearchTree()
bst.insert(10)
bst.insert(10)
result = bst.contains(10)
check(True, result, "Check if 10 exists with duplicate inserts:")

print("\n----- Test: Contains with Left and Right -----\n")
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(1)
bst.insert(8)
bst.insert(12)
bst.insert(20)
result = bst.contains(1)
check(True, result, "Check if 1 exists:")
result = bst.contains(8)
check(True, result, "Check if 8 exists:")
result = bst.contains(12)
check(True, result, "Check if 12 exists:")
result = bst.contains(20)
check(True, result, "Check if 20 exists:")
