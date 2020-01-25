def disarium_number(number):
    string = str(number)
    num = 1
    num2 = 0
    output = 0
    while num2 < len(string):
        output += int(string[num2]) ** num
        num += 1
        num2 += 1
    if output == number:
        return "Disarium !!"
    else:
        return "Not !!"
