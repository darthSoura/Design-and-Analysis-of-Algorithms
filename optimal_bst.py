def optimal_bst(keys, frequencies):
    n = len(keys)
    cost = [[0] * n for _ in range(n)]
    root = [[0] * n for _ in range(n)]

    # Fill the diagonal elements with the frequencies
    for i in range(n):
        cost[i][i] = frequencies[i]
        root[i][i] = i

    # Build the optimal BST for all possible subarrays
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            cost[i][j] = float('inf')

            for k in range(i, j + 1):
                sub_cost = sum(frequencies[i:j+1])
                if k > i:
                    sub_cost += cost[i][k - 1]
                if k < j:
                    sub_cost += cost[k + 1][j]
                if sub_cost < cost[i][j]:
                    cost[i][j] = sub_cost
                    root[i][j] = k

    print(cost)
    return cost[0][n - 1], root


def construct_optimal_bst(keys, root, i, j, level=0):
    if i > j:
        return None
    root_idx = root[i][j]
    node = Node(keys[root_idx])
    print('  ' * level + f'Level {level}: {node.key}')
    node.left = construct_optimal_bst(keys, root, i, root_idx - 1, level + 1)
    node.right = construct_optimal_bst(keys, root, root_idx + 1, j, level + 1)
    return node


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Driver code
keys = [10, 20, 30, 40]
frequencies = [4, 2, 6, 3]

cost, root = optimal_bst(keys, frequencies)
print("Minimum cost of optimal BST:", cost)

print("\nOptimal BST structure:")
root_node = construct_optimal_bst(keys, root, 0, len(keys) - 1)
