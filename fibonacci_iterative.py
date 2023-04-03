def Fib(n):
    
    F = [0]*(n+1)
    F[0] = 0
    F[1] = 1
    
    for i in range(2, n+1):
        F[i] = F[i-1] + F[i-2]
    
    return F[n]

n = int(input("Enter n (for the nth Fibonacci number): "))
num = Fib(n)
print(f"The {n}th Fibonacci number: {num}")