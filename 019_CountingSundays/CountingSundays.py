'''
How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?
'''


def return_days_month(month, year):

    #             J, F,  M,  A,  M,  J,  J,  A,  S,  O,  N,  D
    days_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if leap_year(year) and month == 2:
        return 29
    return days_month[month - 1]


def leap_year(year):

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# 1 January 1901 => Tuesday
# 6 January 1901 => Sunday

accumulated = -5
# We need to subtract 5 days to initialize the first day of
# month on Sunday (the 6th of January 1901 was Sunday)
sundays = 0
registry = []

for year in range(1901, 2001):
    for month in range(1, 13):

        if accumulated % 7 == 0:
            sundays += 1
            registry.append([month, year])
        current = return_days_month(month, year)
        print(current, end=" ")
        accumulated += current
    print()
    print(year, accumulated, sundays)
print(registry)
print(sundays)
