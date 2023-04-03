def merge_and_countSplitInv(C, D):
    
    i = 0
    j = 0
    k = 0
    splitInv = 0
    p,q = len(C), len(D)
    n = p+q
    B = [0]*n
    
    while i<p and j<q:
        if C[i] < D[j]:
            B[k] = C[i]
            i += 1
        else:
            B[k] = D[j]
            j += 1
            splitInv += (n//2 - i)
        k += 1
    
    while i < p:
        B[k] = C[i]
        i += 1
        k += 1

    while j < q:
        B[k] = D[j]
        j += 1
        k += 1
        splitInv += (n//2 - i)
        
    return (B, splitInv)

def sort_and_countInv(A):
    
    n = len(A)
    if n == 0 or n == 1:
        return (A, 0)
    
    C = A[:n//2]
    D = A[n//2:]
    
    (C, leftInv) = sort_and_countInv(C)
    (D, rightInv) = sort_and_countInv(D)
    
    (B, splitInv) = merge_and_countSplitInv(C, D)
    
    return (B, leftInv+rightInv+splitInv)

A = [9,3,5,2,4,6]
inv = sort_and_countInv(A)[1]
print(f"Number of inversions: {inv}")