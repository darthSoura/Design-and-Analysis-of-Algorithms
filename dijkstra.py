from Graph import Graph

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph.vertices}
    distances[start] = 0

    visited = set()
    paths = {vertex: [] for vertex in graph.vertices}

    while len(visited) < graph.num_vertices:
        min_dist = float('inf')
        min_vertex = None

        # Find the unvisited vertex with the smallest distance
        for vertex in graph.vertices:
            if vertex not in visited and distances[vertex] < min_dist:
                min_dist = distances[vertex]
                min_vertex = vertex

        if min_vertex is None:
            break

        visited.add(min_vertex)
        curr_node = graph.adj_list[graph.vertex_dict[min_vertex]]

        while curr_node:
            neighbor = curr_node.val
            weight = curr_node.weight
            distance = min_dist + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                paths[neighbor] = paths[min_vertex] + [min_vertex]

            curr_node = curr_node.next

    return distances, paths



# Create a graph
vertices = ['A', 'B', 'C', 'D']
graph = Graph(vertices)

# Add edges to the graph
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 6)
graph.add_edge('C', 'D', 3)

start_vertex = 'A'
distances, paths = dijkstra(graph, start_vertex)

# Print the shortest distances from the start vertex to all other vertices
for vertex, distance in distances.items():
    print(f"Shortest distance from {start_vertex} to {vertex}: {distance}")

# Print the shortest paths from the start vertex to all other vertices
for vertex, path in paths.items():
    print(f"Shortest path from {start_vertex} to {vertex}: {' -> '.join(path + [vertex])}")