def persistence(num):
    output=0
    while num>9:
        output+=1
        num_str=str(num)
        total=1
        for i in num_str:
            total=total* int(i)
        num=total
    return output