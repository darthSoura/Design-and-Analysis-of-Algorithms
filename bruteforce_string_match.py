def BruteForceStringMatch(T, P):
    
    n = len(T)
    m = len(P)
    
    for i in range(0, n-m+1):
        j = 0
        while j<m and P[j] == T[i+j]:
            j = j+1
            
        if j==m:
            return i
    
    return -1

T = "NOBODY_NOTICED_HIM"
P = "NOT"

print("String: ", T)
print("Pattern: ", P)

match = BruteForceStringMatch(T, P)

print((f"Pattern {P} in String {T} at index: {match}"))