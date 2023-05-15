from Graph import Graph
from collections import deque

def bfs(G, S):
    visited = [False] * G.num_vertices
    queue = deque()

    # Mark the starting vertex as visited and enqueue it
    visited[G.vertex_dict[S]] = True
    queue.append(S)

    while queue:
        V = queue.popleft()
        print(V, end=" ")

        adj_list = G.adj_list[G.vertex_dict[V]]

        curr = adj_list
        while curr:
            W = curr.val
            if not visited[G.vertex_dict[W]]:

                visited[G.vertex_dict[W]] = True
                queue.append(W)
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
bfs(graph, 'S')
