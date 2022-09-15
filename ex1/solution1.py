import calendar
from datetime import datetime

# Task 1

current_datetime = datetime.now()
print(current_datetime)

# Introspect for more possible methods
print(dir(current_datetime))

# current year
print(current_datetime.year)

# Task 2

# current week day - 0, 1, 2, 3, 4, 5, 6
some_date = datetime(2021, 7, 14)
print(some_date.weekday())

# current hour (Extra credit)
# print(current_datetime.hour)


# Task 3

# https://www.wikihow.com/Calculate-Leap-Years
is_leap = datetime(2021, 1, 1)
if is_leap.year % 400 == 0:
    print(is_leap.year, "is a leap year")
elif is_leap.year % 100 == 0:
    print(is_leap.year, "is not a leap year")
elif is_leap.year % 4 == 0:
    print(is_leap.year, "is a leap year")
else:
    print(is_leap.year, "is not a leap year")


# Also acceptible is
if calendar.isleap(2021):
    print("2021 is a leap year")

# Task 4

date_as_string = "Feb 14 2021 8:30AM"
datetime_object = datetime.strptime(date_as_string, "%b %d %Y %I:%M%p")
print(datetime_object)


