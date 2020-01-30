def get_score(arr):
    lines_cleared = 0
    four_liners = 1200
    three_liners = 300
    two_liners = 100
    one_liners = 40
    points = 0
    for i in arr:
        if i == 4:
            points += four_liners
            lines_cleared += i
            if lines_cleared >= 10:
                four_liners += 1200
                three_liners += 300
                two_liners += 100
                one_liners += 40
                lines_cleared = lines_cleared % 10
        elif i == 3:
            points += three_liners
            lines_cleared += i
            if lines_cleared >= 10:
                four_liners += 1200
                three_liners += 300
                two_liners += 100
                one_liners += 40
                lines_cleared = lines_cleared % 10
        elif i == 2:
            points += two_liners
            lines_cleared += i
            if lines_cleared >= 10:
                four_liners += 1200
                three_liners += 300
                two_liners += 100
                one_liners += 40
                lines_cleared = lines_cleared % 10
        elif i == 1:
            points += one_liners
            lines_cleared += i
            if lines_cleared >= 10:
                four_liners += 1200
                three_liners += 300
                two_liners += 100
                one_liners += 40
                lines_cleared = lines_cleared % 10

    return points