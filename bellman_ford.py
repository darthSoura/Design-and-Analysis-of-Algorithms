from Graph import Graph

def bellman_ford(graph, start):
    distances = {vertex: float('inf') for vertex in graph.vertices}
    distances[start] = 0

    # Keep track of paths
    paths = {vertex: [] for vertex in graph.vertices}

    # Relax edges |V - 1| times
    for _ in range(graph.num_vertices - 1):
        for vertex in graph.vertices:
            curr_node = graph.adj_list[graph.vertex_dict[vertex]]
            while curr_node:
                neighbor = curr_node.val
                weight = curr_node.weight
                if distances[vertex] + weight < distances[neighbor]:
                    distances[neighbor] = distances[vertex] + weight
                    paths[neighbor] = paths[vertex] + [vertex]
                curr_node = curr_node.next

    # Check for negative cycles
    for _ in range(graph.num_vertices - 1):
        for vertex in graph.vertices:
            curr_node = graph.adj_list[graph.vertex_dict[vertex]]
            while curr_node:
                neighbor = curr_node.val
                weight = curr_node.weight
                if distances[vertex] + weight < distances[neighbor]:
                    # Negative cycle found
                    raise ValueError("Graph contains a negative cycle")

                curr_node = curr_node.next

    # Add the destination vertex to paths
    for vertex in graph.vertices:
        paths[vertex].append(vertex)

    return distances, paths


# Example usage:

# Create a graph
vertices = ['A', 'B', 'C', 'D', 'E']
graph = Graph(vertices)

# Add edges to the graph
graph.add_edge('A', 'B', 5)
graph.add_edge('A', 'C', 2)
# graph.add_edge('B', 'C', -3)
graph.add_edge('B', 'D', 3)
graph.add_edge('C', 'D', 2)
graph.add_edge('C', 'E', 4)
# graph.add_edge('D', 'E', -1)

start_vertex = 'A'
try:
    distances, paths = bellman_ford(graph, start_vertex)
    # Print the shortest distances from the start vertex to all other vertices
    for vertex, distance in distances.items():
        print(f"Shortest distance from {start_vertex} to {vertex}: {distance}")

    # Print the shortest paths from the start vertex to all other vertices
    for vertex, path in paths.items():
        print(f"Shortest path from {start_vertex} to {vertex}: {' -> '.join(path)}")
except ValueError as e:
    print(str(e))
