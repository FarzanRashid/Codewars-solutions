def find_short(s):
    x = s.split()
    return len(min(x, key= len))