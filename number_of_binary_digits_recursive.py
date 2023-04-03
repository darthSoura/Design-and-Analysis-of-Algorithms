def BinRec(n):
    if n == 1:
        return 1
    else:
        return BinRec(n//2) + 1

n = int(input("Enter an integer: "))
num = BinRec(n)
print(f"Number of binary digits in the binary representation of {n}: {num}")