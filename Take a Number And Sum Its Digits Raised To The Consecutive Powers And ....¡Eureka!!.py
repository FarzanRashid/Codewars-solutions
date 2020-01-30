def valid(num):
    _str= str(num)
    total = 0
    for i, char in enumerate(_str, 1):
        digit = int(char)
        total += digit ** i
    return total == num




def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    output = []
    for i in range(a, b+1):
        if valid(i):
            output.append(i)
    return output