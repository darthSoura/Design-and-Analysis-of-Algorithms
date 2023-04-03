def grade_school_mul(x, y):
    
    y_str = str(y)
    
    result = 0
    
    for i in range(len(y_str)):
        partial_product = x * int(y_str[i])
        result += partial_product * 10**(len(y_str)-i-1)
    
    return result

x, y = map(int, input("Enter two integers: ").split())

result = grade_school_mul(x,y)
print("Answer: ", result)