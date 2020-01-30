def range_bit_count(a, b):
    nums =[]
    bins = []
    str = ''
    for i in range(a, b +1):
        nums.append(i)
    for i in nums:
       bins.append(bin(i))
    for i in bins:
        str += i
    return str.count("1")