def is_very_even_number(n):
    while len(str(n)) != 1:
        num = 0
        for i in str(n):
            num += int(i)
            n = num
    return n % 2 == 0

