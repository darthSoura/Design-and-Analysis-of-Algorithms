def countSplitInv(C, D):
    numInv = 0
    p = len(C)
    q = len(D)
    
    for i in range(0,p):
        for j in range(0, q):
            if C[i] > D[j]:
                numInv = numInv +1
    
    return numInv

def countInv(A):
    
    n=len(A)
    if n==0 or n==1:
        return 0
    
    C = A[:n//2]
    D = A[n//2:]
    
    leftInv = countInv(C)
    rightInv = countInv(D)
    
    splitInv = countSplitInv(C,D)
    
    return leftInv + rightInv + splitInv

A = [1,8,5,7,4,6]
inv = countInv(A)
print(f"Number of inversions: {inv}")