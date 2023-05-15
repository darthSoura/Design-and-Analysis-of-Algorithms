def matrix_chain_multiplication(dims):
    n = len(dims) - 1
    dp = [[float('inf')] * n for _ in range(n)]
    brackets = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 0

    for chain_len in range(2, n + 1):
        for i in range(n - chain_len + 1):
            j = i + chain_len - 1
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    brackets[i][j] = k

    return dp, brackets


def print_optimal_parentheses(brackets, i, j):
    if i == j:
        print(f"A{i+1}", end="")
        return
    print("(", end="")
    print_optimal_parentheses(brackets, i, brackets[i][j])
    print_optimal_parentheses(brackets, brackets[i][j] + 1, j)
    print(")", end="")


# Driver code
matrix_dims = [7, 1, 5, 4, 2]
dp_table, bracket_table = matrix_chain_multiplication(matrix_dims)

print("Minimum number of multiplications needed:", dp_table[0][len(matrix_dims) - 2])
print("Optimal Parentheses for Matrix Chain Multiplication: ", end="")
print_optimal_parentheses(bracket_table, 0, len(matrix_dims) - 2)
