class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.weight = None

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.num_vertices = len(vertices)
        self.adj_list = [None] * self.num_vertices
        self.vertex_dict = {vertices[i]: i for i in range(self.num_vertices)}

    def add_edge(self, src, dest, weight):
        # Add edge from src to dest
        node = Node(dest)
        node.weight = weight
        node.next = self.adj_list[self.vertex_dict[src]]
        self.adj_list[self.vertex_dict[src]] = node

        # Add edge from dest to src
        node = Node(src)
        node.weight = weight
        node.next = self.adj_list[self.vertex_dict[dest]]
        self.adj_list[self.vertex_dict[dest]] = node

    def print_graph(self):
        for i in range(self.num_vertices):
            print(f"Adjacency list of vertex {self.vertices[i]}:")
            curr = self.adj_list[i]
            # print(curr.val, curr.weight)
            while curr:
                print(f" -> {curr.val} ({curr.weight})")
                curr = curr.next
            print()

# vertices = ['A', 'B', 'C', 'D']
# g = Graph(vertices)
# g.add_edge('A', 'C', 10)
# g.add_edge('A', 'B', 5)
# g.add_edge('B', 'C', 3)
# g.add_edge('C', 'D', 7)
# g.add_edge('D', 'B', 8)

# g.print_graph()

