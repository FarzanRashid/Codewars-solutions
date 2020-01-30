def add_binary(a,b):
    output = (a + b)
    final = str(bin(output))
    print(type(final))
    return final[2:]
