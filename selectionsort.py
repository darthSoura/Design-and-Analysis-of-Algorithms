
def selectionsort(A):
    
    n = len(A)
    for i in range(0,n-1):
        swap = i
        for j in range(i+1,n):
            if A[j] < A[swap]:
                swap = j
        
        A[i], A[swap] = A[swap], A[i]
    
    return A

