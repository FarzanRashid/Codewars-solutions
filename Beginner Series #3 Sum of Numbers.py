def get_sum(a,b):
    num = 0
    if a == b:
        return b
    elif b > a:
        for i in range(a, b+1):
            num += i
        return num
    else:
        for i in range(b, a+1):
            num += i
    return num


print(get_sum(0, -1))







