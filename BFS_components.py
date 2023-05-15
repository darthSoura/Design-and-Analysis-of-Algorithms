from Graph import Graph 
from collections import deque

def count_connected_components(G):
    visited = [False] * G.num_vertices
    count = 0

    for vertex in range(G.num_vertices):
        if not visited[vertex]:
            count += 1
            visited[vertex] = True
            queue = deque([vertex])

            while queue:
                V = queue.popleft()
                adj_list = G.adj_list[V]

                curr = adj_list
                while curr:
                    W = curr.val
                    if not visited[G.vertex_dict[W]]:
                        visited[G.vertex_dict[W]] = True
                        queue.append(G.vertex_dict[W])
                    curr = curr.next

    return count

vertices = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
graph = Graph(vertices)

# Add edges
graph.add_edge('1', '3', 1)
graph.add_edge('1', '5', 2)
graph.add_edge('3', '5', 3)
graph.add_edge('2', '5', 5)
graph.add_edge('6', '5', 4)
graph.add_edge('7', '4', 4)
graph.add_edge('9', '8', 4)
graph.add_edge('9', '10', 4)
graph.add_edge('10', '8', 4)

num_connected_components = count_connected_components(graph)
print(f"The number of connected components in the graph is: {num_connected_components}")