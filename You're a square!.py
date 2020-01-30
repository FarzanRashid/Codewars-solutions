import math


def is_square(n):
    if n < 0:
        return False
    num = int(math.sqrt(n))
    return num ** 2 == n
