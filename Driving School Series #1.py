def passed(lst):
    newlst = []
    for i in lst:
        if i <= 18:
            newlst.append(i)
    if len(newlst) == 0:
        return "'No pass scores registered.'"
    else:
        return sum(newlst) // len(newlst)


print(passed([3,22,9,13,20,18,2,14,20,8,23,12,7,21,21,19,20,11,18,7,13,22,11,20,9]))


