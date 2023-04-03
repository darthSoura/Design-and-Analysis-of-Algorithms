def binarySearch(A, K):
    n = len(A)
    l, r = 0, n-1

    while l<=r:
        m = (l+r)//2
        if K == A[m]:
            return m
        elif K < A[m]:
            r = m-1
        else:
            l = m+1
    return -1

K = int(input("Enter key to be searched for in array: "))
A = [89, 45, 68, 90, 29, 34, 17]
A.sort()
print("Array: ", A)

index = binarySearch(A, K)
print("Key found at index: ", index)