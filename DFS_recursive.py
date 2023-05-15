from Graph import Graph

def dfs(G, S):
    visited = set()

    def dfs_helper(V):
        visited.add(V)
        print(V, end=" ")  # Print the visited vertex
        
        curr = G.adj_list[G.vertex_dict[V]]
        while curr:
            if curr.val not in visited:
                dfs_helper(curr.val)
            curr = curr.next

    dfs_helper(S)

# Create a graph
vertices = ['A', 'B', 'C', 'D', 'E']
graph = Graph(vertices)

# Add edges
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 2)
graph.add_edge('B', 'D', 3)
graph.add_edge('C', 'D', 4)
graph.add_edge('D', 'E', 5)

# Perform DFS starting from vertex 'A'
dfs(graph, 'A')
