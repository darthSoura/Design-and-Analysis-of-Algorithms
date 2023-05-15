from Graph import Graph
def kruskal_straightforward(graph):
    edges = []
    for i in graph.vertices:
        curr = graph.adj_list[graph.vertex_dict[i]]
        while curr:
            dest = curr.val
            weight = curr.weight

            if (dest, i) not in [t[:2] for t in edges]: # avoid duplicates
                edges.append((i, dest, weight))
            curr = curr.next
    
    edges.sort(key=lambda x: x[2])  # Sort edges by weight in ascending order

    mst = []  # Minimum Spanning Tree
    parent = {v: v for v in graph.vertices}
    visited = {v: False for v in graph.vertices}

    def dfs(source):
        visited.add(source)
        for i in range(len(graph.vertices)):
            if graph.vertices[i] == source:
                curr = graph.adj_list[i]
                break
        while curr:
            neighbor = curr.val
            if neighbor not in visited:
                mst.append((source, graph.vertices[neighbor], curr.weight))
                dfs(graph.vertices[neighbor])
            curr = curr.next

    for edge in edges:
        src, dest, weight = edge
        if src not in visited or dest not in visited:
            mst.append(edge)
            dfs(src)
    return mst

# Example usage
# vertices = ['A', 'B', 'C', 'D', 'E']
# g = Graph(vertices)
# g.add_edge('A', 'B', 1)
# g.add_edge('A', 'C', 2)
# g.add_edge('B', 'D', 3)
# g.add_edge('C', 'D', 4)
# g.add_edge('C', 'E', 5)
# g.add_edge('D', 'A', 6)

# tree, weight = kruskal_straightforward(g)
# print("Minimum Spanning Tree: ", tree, sep='\n')
# print("Weight: ", weight)


graph = Graph(['A', 'B', 'C', 'D', 'E'])
graph.add_edge('A', 'B', 4)
graph.add_edge('A', 'C', 2)
graph.add_edge('B', 'C', 1)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 8)
graph.add_edge('C', 'E', 10)
graph.add_edge('D', 'E', 2)

tree = kruskal_straightforward(graph)
print("Minimum Spanning Tree: ", tree, sep='\n')
# print("Weight: ", weight)
