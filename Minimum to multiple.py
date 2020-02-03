def minimum(a, x):
    mod = a % x
    return min(mod , x - mod)


print(minimum(9,4))