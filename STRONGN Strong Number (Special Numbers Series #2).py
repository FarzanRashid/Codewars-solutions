def strong_num(number):
    string = str(number)
    total = 0
    for i in string:
        num = int(i)
        tempval = 1
        for j in range(1, num +1):
            tempval *= j
        total += tempval
    if total == number:
         return "STRONG!!!!"
    else:
        return "Not Strong !!"
