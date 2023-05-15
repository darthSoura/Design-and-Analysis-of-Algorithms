def mwis_recursive(graph, vertex):
    if vertex < 0:
        return 
    if vertex == 0:
        return graph[0], [graph[0]]
    if vertex == 1:
        if graph[0] > graph[1]:
            return graph[0], [graph[0]]
        else:
            return graph[1], [graph[1]]

    weight_S2, S2 = mwis_recursive(graph, vertex - 2)
    weight_S1, S1 = mwis_recursive(graph, vertex - 1)
    
    if weight_S2 + graph[vertex] > weight_S1:
        return weight_S2 + graph[vertex],  S2 + [graph[vertex]]
    else:
        return weight_S1, S1

graph = [3, 2, 1, 6, 4, 5]

max_weight, max_set = mwis_recursive(graph, len(graph) - 1)
print("Maximum weight independent set weight:", max_weight)
print("Maximum weight independent set:", max_set)
