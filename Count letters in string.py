def letter_count(s):
    outut ={}
    for i in s:
        outut[i] = s.count(i)
    return outut
