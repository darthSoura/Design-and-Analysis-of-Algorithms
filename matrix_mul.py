def MatrixMultiplication(A, B):
    
    n = len(A[0])
    
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            C[i][j] = 0.0
            for k in range(0,n):
                C[i][j] = C[i][j] + A[i][k]*B[k][j]
                
    return C

A = [
    [1, 2, 3],
    [1, 4, 5],
    [2, 3, 6]
]

B = [
    [6, 3, 3],
    [7, 5, 2],
    [1, 1, 0]
]

print("Matrix A: ", A)
print("Matrix B: ", B)

C = MatrixMultiplication(A,B)

print("C=AB: ", C)
