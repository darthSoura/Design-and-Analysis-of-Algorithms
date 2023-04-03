def partition(A, l, r):
     
    p = A[l]
    i = l - 1
    j = r + 1
 
    while (True):
 
        i += 1
        while (A[i] < p):
            i += 1
 
        j -= 1
        while (A[j] > p):
            j -= 1
 
        if (i >= j):
            return j
 
        A[i], A[j] = A[j], A[i]
 
 
 
def quicksort(A, l, r):
    if (l < r):
 
        s = partition(A, l, r)
        quicksort(A, l, s)
        quicksort(A, s + 1, r)
    
