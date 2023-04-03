def F(n):
    if n<=1:
        return n
    else:
        return F(n-1) + F(n-2)

n = int(input("Enter n (for the nth Fibonacci number): "))
num = F(n)
print(f"The {n}th Fibonacci number: {num}")