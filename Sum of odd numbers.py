def row_sum_odd_numbers(n):
    val = 1
    for i, v in enumerate(range(n), 1):
        total = 0
        for v in range(i):
            total += val
            val += 2

    return  total