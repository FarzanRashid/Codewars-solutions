def special_number(number):
    nums = [0, 1, 2, 3, 4, 5]
    string = str(number)
    for i in string:
        if int(i) not in nums:
            return "NOT!!"
    return "Special!!"
