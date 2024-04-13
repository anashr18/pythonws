class MinHeap:
    def __init__(self) -> None:
        self.heap = []
        pass

    def _left_child_idx(self, idx):
        return 2 * idx + 1
        pass

    def _right_child_idx(self, idx):
        return 2 * idx + 2
        pass

    def print_heap(self):
        print(("->").join(map(str, self.heap)))
        pass

    def _parent_idx(self, idx):
        return (idx - 1) // 2
        pass

    def _swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def insert(self, value):
        self.heap.append(value)
        idx = len(self.heap) - 1
        while idx > 0 and self.heap[idx] < self.heap[self._parent_idx(idx)]:
            self._swap(idx, self._parent_idx(idx))
            idx = self._parent_idx(idx)
        pass

    def _sink_down(self, idx):
        max_idx = len(self.heap) - 1
        lowest_idx = idx = 0
        while idx <= max_idx:
            if (
                self._left_child_idx(idx) <= max_idx
                and self.heap[idx] > self.heap[self._left_child_idx(idx)]
            ):
                lowest_idx = self._left_child_idx(idx)
            if (
                self._right_child_idx(idx) <= max_idx
                and self.heap[lowest_idx] > self.heap[self._right_child_idx(idx)]
            ):
                lowest_idx = self._right_child_idx(idx)
            # if idx itself is the lowest that means heap
            # is alreay min heap and idx has min value
            if idx == lowest_idx:
                return
            # swap
            self._swap(idx, lowest_idx)
            idx = lowest_idx
        pass

    def remove(self):
        if self.heap is None:
            return None
        temp = self.heap[0]
        last_element = self.heap.pop()
        if len(self.heap) > 0:
            self.heap[0] = last_element
            self._sink_down(0)
        return temp
        pass


myheap = MinHeap()
myheap.insert(12)
myheap.insert(10)
myheap.insert(8)
myheap.insert(6)
myheap.insert(4)
myheap.insert(2)

print(myheap.heap)  # [2, 6, 4, 12, 8, 10]

removed = myheap.remove()
print(f"Removed: {removed}, Heap: {myheap.heap}")  # Removed: 2, Heap: [4, 6, 10, 12, 8]

removed = myheap.remove()
print(f"Removed: {removed}, Heap: {myheap.heap}")  # Removed: 4, Heap: [6, 8, 10, 12]

removed = myheap.remove()
print(f"Removed: {removed}, Heap: {myheap.heap}")  # Removed: 6, Heap: [8, 12, 10]
