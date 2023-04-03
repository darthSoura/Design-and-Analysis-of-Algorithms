def Binary(n):
    
    count = 1
    while n>1: 
        count += 1
        n = n//2
    return count
    
n = int(input("Enter an integer: "))
num = Binary(n)
print(f"Number of binary digits in the binary representation of {n}: {num}")