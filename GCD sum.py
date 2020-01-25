def solve(s,g):
    if s % g == 0:
        return g, s - g
    else:
        return -1