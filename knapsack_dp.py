def knapsack_dp(S, V, C):
    # S - Sizes, V - Values, C - Knapsack Capacity
    n = len(S)

    A = [[0] * (C + 1) for _ in range(n + 1)]

    # Table Filling
    for i in range(1, n + 1):
        for c in range(1, C + 1):
            if S[i - 1] > c:
                A[i][c] = A[i - 1][c]
            else:
                A[i][c] = max(A[i - 1][c], A[i - 1][c - S[i - 1]] + V[i - 1])

    # Set reconstruction
    items = []
    c = C
    for i in range(n, 0, -1):
        if S[i-1] <= c and A[i-1][c-S[i-1]] + V[i-1] >= A[i - 1][c]:
            items = [i] + items
            c -= S[i - 1]

    return A[n][C], items

# Example usage:
values= [3, 2, 4, 4]
sizes = [4, 3, 2, 3]
capacity = 6

max_value, selected_items = knapsack_dp(sizes, values, capacity)
print("Maximum value:", max_value)
print("Selected items:", selected_items)
