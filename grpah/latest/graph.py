class Graph:
    def __init__(self) -> None:
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(f"{vertex} : {self.adj_list[vertex]}")
        pass

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False
        pass

    def add_edge(self, v1, v2):
        if v1 not in self.adj_list:
            self.add_vertex(v1)
        if v2 not in self.adj_list:
            self.add_vertex(v2)
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)
        pass

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            if v2 in self.adj_list[v1]:
                self.adj_list[v1].remove(v2)
            if v1 in self.adj_list[v2]:
                self.adj_list[v2].remove(v1)
        pass

    def remove_vertex(self, vertex):
        for node in self.adj_list[vertex]:
            self.adj_list[node].remove(vertex)
        self.adj_list.pop(vertex)
        pass


# The below implementation is for O(1) lookup and removal
# as we use set for this


class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = set()  # Use a set instead of a list

    def add_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].add(v2)  # Adding to a set
            self.adj_list[v2].add(v1)  # Adding to a set

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].discard(
                v2
            )  # Removing from a set using discard (no error if not found)
            self.adj_list[v2].discard(
                v1
            )  # Removing from a set using discard (no error if not found)


my_graph = Graph()
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")

my_graph.add_edge("A", "B")
my_graph.add_edge("A", "C")
my_graph.add_edge("A", "D")
my_graph.add_edge("B", "D")
my_graph.add_edge("C", "D")


print("Graph before remove_vertex():")
my_graph.print_graph()
my_graph.remove_vertex("D")


print("\nGraph after remove_vertex():")
my_graph.print_graph()
