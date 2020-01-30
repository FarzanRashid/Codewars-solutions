def tidyNumber(n):
    string = str(n)
    index = 0
    index2 = 1
    while index2 < len(string):
        if int(string[index]) - int(string[index2]) > 0:
            return False
        index += 1
        index2 += 1
    return True