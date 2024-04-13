class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1
        pass

    def _right_child(self, index):
        return 2 * index + 2
        pass

    def _parent(self, index):
        return (index - 1) // 2
        pass

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
        pass

    def insert(self, value):
        self.heap.append(value)
        curr_idx = len(self.heap) - 1
        while curr_idx > 0 and self.heap[curr_idx] > self.heap[self._parent(curr_idx)]:
            self._swap(curr_idx, self._parent(curr_idx))
            curr_idx = self._parent(curr_idx)

    def print_heap(self):
        print(("->").join(map(str, self.heap)))

    def sink_down(self, idx):
        max_idx = len(self.heap) - 1
        while idx <= max_idx:
            left_child_idx = self._left_child(idx)
            right_child_idx = self._right_child(idx)
            largest_idx = idx
            if self.heap[left_child_idx] > self.heap[largest_idx]:
                largest_idx = left_child_idx
            if self.heap[right_child_idx] > self.heap[largest_idx]:
                largest_idx = right_child_idx
            if largest_idx == idx:
                break
            self._swap(largest_idx, idx)
            idx = largest_idx
        pass

    def remove(self):
        if len(self.heap) == 0:
            return None
        temp = self.heap[0]
        last_element = self.heap.pop()
        if len(self.heap) > 0:
            self.heap[0] = last_element
            self.sink_down(0)
        return temp
        pass


my_heap = MaxHeap()
my_heap.insert(95)
my_heap.insert(80)
my_heap.insert(75)
my_heap.insert(55)
my_heap.insert(60)
my_heap.insert(50)
my_heap.insert(65)

my_heap.print_heap()
my_heap.remove()
# my_heap.insert(100)
my_heap.print_heap()
