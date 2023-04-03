def sequentialSearch2(A, K):
    
    n = len(A)
    A.append(K)
    i = 0
    while A[i] != K:
        i += 1
    
    if i<n:
        return i
    else:
        return -1

K = int(input("Enter key to be searched for in array: "))
A = [89, 45, 68, 90, 29, 34, 17]
print("Array: ", A)

index = sequentialSearch2(A, K)
print("Key found at index: ", index)