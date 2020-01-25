def balanced_num(number):
    string = str(number)
    if len(string) <= 2:
        return "Balanced"
    else:
        leftsum = 0
        rightsum = 0
        if len(string) % 2 != 0:
            midnum = len(string) // 2
            left = string[:midnum]
            right = string[midnum + 1:]
            for i in left:
                leftsum += int(i)
            for i in right:
                rightsum += int(i)
            if leftsum == rightsum:
                return "Balanced"
            else:
                return "Not Balanced"
        if len(string) % 2 == 0:
            midnum = len(string) // 2
            left = string[:midnum - 1]
            right = string[midnum + 1:]
            for i in left:
                leftsum += int(i)
            for i in right:
                rightsum += int(i)
            if leftsum == rightsum:
                return "Balanced"
            else:
                return "Not Balanced"
