def house_numbers_sum(inp):
    sum = 0
    for i in inp:
        if i == 0:
            break
        sum += i
    return sum