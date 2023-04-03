def heapify(A, n, i):
    root = i
    l = 2 * i + 1  
    r = 2 * i + 2  
  
  
    if l < n and A[i] < A[l]:
        root = l
  
  
    if r < n and A[root] < A[r]:
        root = r
  
  
    if root != i:
        A[i], A[root] = A[root], A[i]
    
        heapify(A, n, root)
  
  
  
def heapsort(A):
    n = len(A)
   
    for i in range(n // 2 - 1, -1, -1):
        heapify(A, n, i)
    
    for i in range(n - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heapify(A, i, 0)

