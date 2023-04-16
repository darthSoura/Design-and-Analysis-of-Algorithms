from itertools import combinations
from Graph import Graph
import math

def is_spanning_tree(graph, edges):
    
    if len(edges) != graph.num_vertices - 1:
        return False

    # Check that the edges form a connected graph
    vertices = set()
    for edge in edges:
        vertices.add(edge[0])
        vertices.add(edge[1])
    if len(vertices) != graph.num_vertices:
        return False

    # Check that there are no cycles in the graph
    parent = {vertex: vertex for vertex in vertices}
    for edge in edges:
        src, dest = edge[0], edge[1]
        while src != parent[src]:
            src = parent[src]
        while dest != parent[dest]:
            dest = parent[dest]
        if src == dest:
            return False
        parent[src] = dest

    return True

def find_MST(graph):
    
    edges = []
    for i in range(graph.num_vertices):
        curr = graph.adj_list[i]
        while curr:
            if (curr.val, graph.vertices[i], curr.weight) not in edges:  # check if edge already exists as (dest, src, weight) in edges
                edges.append((graph.vertices[i], curr.val, curr.weight))
            curr = curr.next
    
    edge_combinations = []
    for r in range(1, len(edges) + 1):
        for combination in combinations(edges, r):
            if is_spanning_tree(graph, combination):
                edge_combinations.append(combination)


    weight_MST = float(math.inf)
    MST_edges = []
    
    for combination in edge_combinations:

        weight_combination = sum([edge[2] for edge in combination])

        if weight_combination < weight_MST:
            MST_edges = combination
            weight_MST = weight_combination

    return MST_edges, weight_MST



# graph = Graph(['A', 'B', 'C', 'D', 'E'])
# graph.add_edge('A', 'B', 4)
# graph.add_edge('A', 'C', 2)
# graph.add_edge('B', 'C', 1)
# graph.add_edge('B', 'D', 5)
# graph.add_edge('C', 'D', 8)
# graph.add_edge('C', 'E', 10)
# graph.add_edge('D', 'E', 2)

graph = Graph(['A', 'B', 'C', 'D'])
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('A', 'D', 3)
graph.add_edge('D', 'B', 2)
graph.add_edge('C', 'D', 5)


tree, weight = find_MST(graph)
print("Minimum Spanning Tree: ", tree, sep='\n')
print("Weight: ", weight)