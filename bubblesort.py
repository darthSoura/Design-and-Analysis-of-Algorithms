def bubblesort(A):
    
    n = len(A)
    for i in range(0, n-1):
        for j in range(0, n-1-i):
            if A[j+1] < A[j]:
                A[j], A[j+1] = A[j+1], A[j]
    
    return A
