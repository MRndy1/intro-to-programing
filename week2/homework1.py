# Exercise 6:
#
# Magic Dates
# The date June 10, 1960, is special because when it is written in the
# following format, the month times the day equals the year:
# 6/10/60
# Design a program that asks the user to enter a month (in numeric form),
# a day, and a two-digit year. The program should then determine whether
# the month times the day equals the year. If so, it should display a
# message saying the date is magic. Otherwise, t should display
# a message saying the date is not magic.

date = int(input("please input a date from 1-31: \n"))
month = int(input("please input a month from 1-12: \n"))
year = int(input("please input a two-digit year: \n"))

if (month * date) == year:
    print(f"the date {date}/{month}/{year} is special")
else:
    print(f"the date {date}/{month}/{year} is not special")


