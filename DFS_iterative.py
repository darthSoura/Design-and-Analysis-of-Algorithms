from Graph import Graph
from collections import deque

def dfs(G, S):
    visited = [False] * G.num_vertices
    stack = deque()
    stack.append(S)

    while stack:
        V = stack.pop()
        if not visited[G.vertex_dict[V]]:
            print(V, end=" ")  # Print the visited vertex
            visited[G.vertex_dict[V]] = True

        curr = G.adj_list[G.vertex_dict[V]]
        while curr:
            if not visited[G.vertex_dict[curr.val]]:
                stack.append(curr.val)
            curr = curr.next
            
# Create a graph
vertices = ['S', 'A', 'B', 'C', 'D', 'E']
graph = Graph(vertices)

# Add edges
graph.add_edge('S', 'A', 1)
graph.add_edge('S', 'B', 2)
graph.add_edge('A', 'C', 3)
graph.add_edge('D', 'E', 5)
graph.add_edge('E', 'C', 4)
graph.add_edge('D', 'C', 4)
graph.add_edge('B', 'D', 4)
graph.add_edge('B', 'C', 4)

# Perform DFS starting from vertex 'A'
dfs(graph, 'S')
