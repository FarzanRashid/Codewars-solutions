def sum_triangular_numbers(n):
    if n < 0:
        return 0
    tri = 1
    num = 2
    output =[]
    while len(output) < n:
        output.append(tri)
        tri += num
        num += 1
    return sum(output)