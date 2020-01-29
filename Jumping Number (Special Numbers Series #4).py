def jumping_number(number):
    string = str(number)
    index = 0
    index2 = 1
    diff = 1
    if len(string) > 1:
        while index2 < len(string):
            if abs(int(string[index]) - int(string[index2])) != 1:
                return "Not !!"
            index += 1
            index2 += 1
    return "Jumping !!"


