from Graph import Graph 
from collections import deque

def shortest_path(G, V1, V2):
    visited = [False] * G.num_vertices
    queue = deque()
    distance = [float('inf')] * G.num_vertices

    start_index = G.vertex_dict[V1]

    visited[start_index] = True
    queue.append(V1)
    distance[start_index] = 0

    while queue:
        # Performing BFS
        V = queue.popleft()

        if V == V2:
            return distance[G.vertex_dict[V]]

        adj_list = G.adj_list[G.vertex_dict[V]]

        curr = adj_list
        while curr:
            W = curr.val
            if not visited[G.vertex_dict[W]]:
                visited[G.vertex_dict[W]] = True
                queue.append(W)
                distance[G.vertex_dict[W]] = distance[G.vertex_dict[V]] + 1
            curr = curr.next

    # No path exists from start_vertex to target_vertex
    return -1

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


start_vertex = 'S'
target_vertex = 'E'

fewest_edges = shortest_path(graph, start_vertex, target_vertex)
if fewest_edges != -1:
    print(f"The fewest number of edges from {start_vertex} to {target_vertex} is: {fewest_edges}")
else:
    print(f"There is no path from {start_vertex} to {target_vertex}")
