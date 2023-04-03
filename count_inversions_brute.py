def countBruteInv(A):
    numInv = 0
    n = len(A)
    
    for i in range(0,n-1):
        for j in range(i+1, n):
            if A[i] > A[j]:
                numInv = numInv +1
    
    return numInv

A = [1,3,5,2,4,6]
inv = countBruteInv(A)
print(f"Number of inversions: {inv}")