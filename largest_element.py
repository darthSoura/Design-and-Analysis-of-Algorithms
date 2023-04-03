def MaxElement(A):
    
    n = len(A)
    maxval = A[0]
    
    for i in range(1,n):
        if A[i]>maxval:
            maxval = A[i]
    
    return maxval

A = [89, 45, 68, 90, 29, 34, 17]
print("Array: ", A)
largest = MaxElement(A)
print("Largest Element in the array: ", largest)