class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.eos = False
class Trie:
    def __init__(self) -> None:
        self.root = None
    def __str__(self):
        current = self.root
        for childKey in current.children:
            print(childKey, end="")
            node = current.children[childKey]
            current = node
            
    def insert(self, word):
        if self.root is None:
            self.root = TrieNode()
        current = self.root
        for i in word:
            node = current.children.get(i)
            if node is None:
                node=TrieNode()
                current.children[i] = node
            current=node
        current.eos=True
    