def uniqueElements(A):
    
    n = len(A)
    
    for i in range(0, n-1):
        for j in range(i+1, n):
            if A[i] == A[j]:
                return False
    return True

A = [89, 45, 68, 90, 29, 34, 45]
print("Array: ", A)
unique = uniqueElements(A)
print("All elements in the array are unique: ", unique)