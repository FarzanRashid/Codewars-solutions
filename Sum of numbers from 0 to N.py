def show_sequence(n):
    asd = "="
    num = 0
    output = "0"
    if n == 0:
        return "0=0"
    elif n < 0:
        return "{}<0".format(n)
    else:
        for i in range(1, n +1):
            output += "+{}".format((str(i)))
            num += i
        return output + " = {}".format(num)