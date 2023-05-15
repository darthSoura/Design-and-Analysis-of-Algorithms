def is_safe(board, row, col, n):
    
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
    # Check lower diagonal
    i = row
    j = col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    
    return True


def solve_n_queens_util(board, row, n, solutions):
    # Base case: All queens have been placed
    if row >= n:
        solution = []
        for i in range(n):
            solution.append(board[i][:])
        solutions.append(solution)
        return
    
    # Recursive case: Try placing the queen in each column of the current row
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens_util(board, row + 1, n, solutions)
            board[row][col] = 0


def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)
    return solutions


n = int(input("Enter n: "))
solutions = solve_n_queens(n)
print(f"Number of solutions for {n}-Queens problem: {len(solutions)}")
for solution in solutions:
    print("Solution:")
    for row in solution:
        print(row)
    print()
