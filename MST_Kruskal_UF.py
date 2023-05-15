from Graph import Graph


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True


def kruskal(G):
    E = []
    for i in G.vertices:
        curr = G.adj_list[G.vertex_dict[i]]
        while curr:
            dest = curr.val
            weight = curr.weight

            if (dest, i) not in [t[:2] for t in E]: # avoid duplicates
                E.append((i, dest, weight))
            curr = curr.next

    E.sort(key=lambda x: x[2])  # Sort edges by weight in ascending order

    T = []  # Minimum Spanning Tree
    min_wt = 0
    uf = UnionFind(G.num_vertices)

    for edge in E:
        src, dest, weight = edge

        if uf.union(G.vertex_dict[src], G.vertex_dict[dest]):
            T.append((src, dest))
            min_wt += weight

    return T, min_wt


# Usage example:
graph = Graph(['A', 'B', 'C', 'D', 'E'])
graph.add_edge('A', 'B', 4)
graph.add_edge('A', 'C', 2)
graph.add_edge('B', 'C', 1)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 8)
graph.add_edge('C', 'E', 10)
graph.add_edge('D', 'E', 2)
  
tree, weight = kruskal(graph)
print("Minimum Spanning Tree: ", tree, sep='\n')
print("Weight: ", weight)

vertices = ['A', 'B', 'C', 'D', 'E']
g = Graph(vertices)
g.add_edge('A', 'B', 1)
g.add_edge('A', 'C', 2)
g.add_edge('B', 'D', 3)
g.add_edge('C', 'D', 4)
g.add_edge('C', 'E', 5)
g.add_edge('D', 'A', 6)

tree, weight = kruskal(g)
print("Minimum Spanning Tree: ", tree, sep='\n')
print("Weight: ", weight)