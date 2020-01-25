def square_digits(num):
    string = str(num)
    num = ""
    for i in string:
        inte = int(i) ** 2
        num += str(inte)
    return int(num)