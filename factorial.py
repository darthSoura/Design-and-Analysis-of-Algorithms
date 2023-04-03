def F(n):
    if n == 0:
        return 1
    else:
        return F(n-1)*n
    
n = int(input("Enter an integer: "))
fact = F(n)
print(f"Factorial of {n}: {fact}")