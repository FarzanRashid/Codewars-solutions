def lottery(s):
    string = ""
    for i in s:
        if i.isdigit():
            if i not in string:
                string += i
    return string if len(string) > 0 else "One more run!"


print(lottery("ynMAisVpHEqpqHBqTrwH"))