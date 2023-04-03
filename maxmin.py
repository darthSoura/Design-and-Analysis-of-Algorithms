def maxMin(S):
    
    n = len(S)
    if n == 2:
        return (max(S[0], S[1]), min(S[0], S[1]))
    
    S1 = S[:n//2]
    S2 = S[n//2:]
    
    (max1, min1) = maxMin(S1)
    (max2, min2) = maxMin(S2)
    
    return (max(max1, max2), min(min1, min2))

A = [4,1,2,8,9,7,6,3]
maxElm, minElm = maxMin(A)
print("Largest Element: ", maxElm)
print("Smallest Element: ", minElm)