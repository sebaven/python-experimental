"""
You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

import datetime

start = datetime.datetime.strptime("01-01-1901", "%d-%m-%Y")
end = datetime.datetime.strptime("31-12-2000", "%d-%m-%Y")
range_length = (end-start).days
date_array = [start + datetime.timedelta(days=x) for x in range(0, range_length)]

count = 0
for date in date_array:
    if date.day == 1 and date.weekday() == 6:
        count = count + 1

print("Amount of sundays falling on the first of the month: %s" % count)

