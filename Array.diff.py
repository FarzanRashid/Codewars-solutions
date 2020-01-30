def array_diff(a, b):
    for i in b:
        if a.count(i) > 0:
            while a.count(i) > 0:
                a.remove(i)
    return a