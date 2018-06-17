def howManySundays(n, startDay):

    week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday']
    startIndex = -1

    for i in range(1, len(week) + 1):
        if week[i] == startDay:
            startIndex = i
            break

    return (n + startIndex) // len(week)
