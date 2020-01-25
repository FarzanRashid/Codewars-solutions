def add_letters(*letters):
    if letters:
        lst = [0, "a", "b", "c", "d", "e", "f","g", "h", "i", "j", "k", "l", "m", "n", "o", "p", 'q', "r", "s", "t", "u", "v", "w", "x", "y", "z" ]
        sum = 26
        for i in letters:
            if i in lst:
                sum += lst.index(i)
        if sum > 26:
            if sum % 26 == 0:
                return lst[-1]
            return lst[sum % 26]
        return lst[sum]
    return "z"