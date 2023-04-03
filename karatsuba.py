def num_length(n):
    return len(str(n))

def karatsuba(x, y):
    
    # base case
    if num_length(x) <= 1 or num_length(y) <= 1:
        return x*y
    
    # recursive case
    n = max(num_length(x), num_length(y))
    n2 = n // 2
    
    a, b = divmod(x, 10**n2)
    c, d = divmod(y, 10**n2)
    p, q = a+b, c+d
    
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    pq = karatsuba(p, q)
    
    adbc = pq - ac - bd
    
    result = ac * (10 ** (2*n2)) + adbc * (10 ** n2) + bd
    
    return result

x, y = map(int, input("Enter two integers: ").split())
print("Answer: ", karatsuba(x,y))