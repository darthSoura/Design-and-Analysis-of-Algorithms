def mwis_bottom_up(graph):
    n = len(graph)    
    if n == 0:
        return 0, []

    if n == 1:
        return graph[0], [graph[0]]

    # Maximum weight calculation
    A = [0] * (n+1)
    A[0] = 0
    A[1] = graph[0]

    for i in range(2, n+1):
        A[i] = max(A[i-1], A[i-2] + graph[i-1])
    
    # Reconstruction
    S = []
    i = n
    while i>=2:
        if A[i-1] >= A[i-2] + graph[i-1]:
            i = i-1
        else:
            S = [graph[i-1]] + S
            i = i-2
    
    if i == 1:
        S = [graph[0]] + S

    return A[n], S

graph = [3, 2, 1, 6, 4, 5]
# graph = [1, 4, 5, 4]

max_weight, max_set = mwis_bottom_up(graph)
print("Maximum weight independent set weight:", max_weight)
print("Maximum weight independent set:", max_set)
