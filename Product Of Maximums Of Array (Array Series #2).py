def max_product(lst, n_largest_elements):
    output = 1
    lst.sort()
    lst.reverse()
    nums = []
    for i in range(0, n_largest_elements):
        nums.append(lst[i])
    for i in nums:
        output *= i
    return output


print(max_product([4, 3, 5], 2))

