def count_letters_and_digits(s):
    low = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    up = []
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in low:
        up.append(i.upper())
    count = 0
    for i in s:
        if i in low or i in nums:
            count += 1
        if i in up:
            count += 1
    return count


print(count_letters_and_digits('n!!ice!!123'))