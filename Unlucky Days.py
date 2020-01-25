def unlucky_days(year):
    cnt = 0
    for month in range(1,13):
        day = datetime.datetime(year, month, 13)
        if day.strftime("%A") == 'Friday':
            cnt += 1
    return cnt