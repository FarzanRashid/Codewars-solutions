def tribonacci(signature, n):
    if n == 0:
        return []
    elif n < len(signature):
        return [signature[n]]
    output = signature
    index = 0
    index2 = 1
    index3 = 2
    a = output[index]
    b = output[index2]
    c = output[index3]
    #d = a + b + c
    while len(output) < n:
        d = a + b + c
        output.append(d)
        index += 1
        index2 += 1
        index3 += 1
        a = output[index]
        b = output[index2]
        c = output[index3]
    return output