def num_length(n):
    return len(str(n))

def recursively_multiply(x, y):
    
    # base case
    if num_length(x) <= 1 or num_length(y) <= 1:
        return x*y
    
    # recursive case
    n = max(num_length(x), num_length(y))
    n2 = n // 2
    
    a, b = divmod(x, 10**n2)
    c, d = divmod(y, 10**n2)
    
    ac = recursively_multiply(a, c)
    bd = recursively_multiply(b, d)
    ad = recursively_multiply(a, d)
    bc = recursively_multiply(b, c)
        
    result = ac * (10 ** (2*n2)) + (ad+bc) * (10 ** n2) + bd
    
    return result

x, y = map(int, input("Enter two integers: ").split())
print("Answer: ", recursively_multiply(x,y))