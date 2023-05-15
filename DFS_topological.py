from Graph import Graph

def dfs(graph, start_vertex):
    visited = set()
    stack = []

    def dfs_helper(vertex):
        visited.add(vertex)

        curr = graph.adj_list[graph.vertex_dict[vertex]]
        while curr:
            if curr.val not in visited:
                dfs_helper(curr.val)
            curr = curr.next

        stack.append(vertex)

    for vertex in graph.vertices:
        if vertex not in visited:
            dfs_helper(vertex)

    # Print the topological ordering
    while stack:
        print(stack.pop(), end=" ")

# Create a graph
vertices = ['A', 'B', 'C', 'D', 'E']
graph = Graph(vertices)

# Add edges
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 2)
graph.add_edge('B', 'D', 3)
graph.add_edge('C', 'D', 4)
graph.add_edge('D', 'E', 5)

# Perform topological ordering using DFS
dfs(graph, 'A')
