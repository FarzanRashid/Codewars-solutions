def min_sum(arr):
    arr.sort()
    total = 0
    begin = 0
    end = len(arr) - 1
    while end > begin:
        total += arr[end] * arr[begin]
        begin += 1
        end -= 1
    return total

print(min_sum([9,2,8,7,5,4,0,6]))