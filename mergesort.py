def merge(C, D):
    i, j = 0, 0
    p = len(C)
    q = len(D)
    B = [0]*(p+q)
    
    i = j = k = 0
    while i < p and j < q:
        if C[i] < D[j]:
            B[k] = C[i]
            i += 1
        else:
            B[k] = D[j]
            j += 1
        k += 1

    while i < p:
        B[k] = C[i]
        i += 1
        k += 1

    while j < q:
        B[k] = D[j]
        j += 1
        k += 1
        
    return B
        
def mergesort(A):
    n = len(A)
    if(n>1):
        C = A[:n//2]
        D = A[n//2:]
        mergesort(C)
        mergesort(D)
        return merge(C, D)
    
    return A
