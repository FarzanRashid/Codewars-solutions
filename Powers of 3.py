def largestPower(N):
    i=0
    while 3**i<N:
        i+=1
    return i-1


