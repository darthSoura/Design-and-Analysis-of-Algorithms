from Graph import Graph
import random
import heapq

def prim(graph):
    X = set()
    T = []
    weight = 0
    
    random_vertex = random.choice(graph.vertices)
    X.add(random_vertex)

    edges_heap = []
    while True:
        for V in X:
            curr = graph.adj_list[graph.vertex_dict[V]]
            while curr:
                W = curr.val
                if W not in X:
                    heapq.heappush(edges_heap, (curr.weight, (V, W)))
                curr = curr.next

        if not edges_heap:
            break

        min_cost, selected_edge = heapq.heappop(edges_heap)
        v_star, w_star = selected_edge
        
        if w_star in X:
            continue
        
        X.add(w_star)
        T.append(selected_edge)
        weight += min_cost

    return T, weight

# graph = Graph(['A', 'B', 'C', 'D'])
# graph.add_edge('A', 'B', 1)
# graph.add_edge('A', 'C', 4)
# graph.add_edge('A', 'D', 3)
# graph.add_edge('D', 'B', 2)
# graph.add_edge('C', 'D', 5)

graph = Graph(['A', 'B', 'C', 'D', 'E'])
graph.add_edge('A', 'B', 4)
graph.add_edge('A', 'C', 2)
graph.add_edge('B', 'C', 1)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 8)
graph.add_edge('C', 'E', 10)
graph.add_edge('D', 'E', 2)


tree, weight = prim(graph)
print("Minimum Spanning Tree: ", tree, sep='\n')
print("Weight: ", weight)