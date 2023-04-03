def insertionsort(A):
    
    n = len(A)
    
    for i in range(1,n):
        v = A[i]
        j = i-1
        
        while j>=0 and A[j] > v:
            A[j+1] = A[j]
            j = j-1
        
        A[j+1] = v
        