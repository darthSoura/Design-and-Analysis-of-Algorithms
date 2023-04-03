def binarySearchRecur(A, l, r, K):
    n = len(A)

    if l<=r:
        m = (l+r)//2
        if K == A[m]:
            return m
        elif K < A[m]:
            return binarySearchRecur(A, l, m-1, K)
        else:
            return binarySearchRecur(A, m+1, r, K)
    return -1

K = int(input("Enter key to be searched for in array: "))
A = [89, 45, 68, 90, 29, 34, 17]
A.sort()
print("Array: ", A)

index = binarySearchRecur(A, 0, len(A)-1, K)
print("Key found at index: ", index)