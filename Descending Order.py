def Descending_Order(num):
    _str = str(num)
    output = ""
    lst_of_str = []
    for i in _str:
        lst_of_str.append(i)
    lst_of_str.sort()
    lst_of_str.reverse()
    for i in lst_of_str:
        output += str(i)
    return int(output)