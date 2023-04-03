def binary_addition(x, y):

    x_int = int(x, 2)
    y_int = int(y, 2)

    sum_int = x_int + y_int

    return bin(sum_int)[2:]


def karatsuba_binary(x, y):

    if len(x) == 1 or len(y) == 1:
        return bin(int(x, 2) * int(y, 2))[2:]

    n = max(len(x), len(y))
    if len(x) < n:
        x = '0' * (n - len(x)) + x
    if len(y) < n:
        y = '0' * (n - len(y)) + y

    n2 = n // 2
    a, b = x[:-n2], x[-n2:]
    c, d = y[:-n2], y[-n2:]

    p1 = karatsuba_binary(a, c)
    p2 = karatsuba_binary(b, d)
    p3 = karatsuba_binary(binary_addition(a, b), binary_addition(c, d))

    result = (int(p1, 2) << (2 * n2)) + ((int(p3, 2) - int(p1, 2) - int(p2, 2)) << n2) + int(p2, 2)

    return bin(result)[2:]

x, y = map(int, input("Enter two integers: ").split())

x_bin = bin(x)[2:]
y_bin = bin(y)[2:]

result = int(karatsuba_binary(x_bin, y_bin), 2)

print("Answer: ", result)