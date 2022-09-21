# # Ex 4
# Event Day Calculator
# - takes date as input
# - prints out years, months, weeks & days until
import datetime
import re

user_year = int(input("What year is your event?: "))
user_month = input("What month is your event?: ")
user_day = int(input("What day is your event?: "))

# input for january may be "jan", "january" or 1

months_full = [
    "january", 
    "february", 
    "march", 
    "april", 
    "may", 
    "june", 
    "july", 
    "august", 
    "september", 
    "october", 
    "november", 
    "december",
    ]

months_short = [
    "jan", 
    "feb", 
    "mar", 
    "apr", 
    "may", 
    "jun", 
    "jul", 
    "aug", 
    "sep", 
    "oct", 
    "nov", 
    "dec",
    ]
def validate_date(user_month):
    month_invalid = True
    # year_pattern_1 = r"dddd"
    while month_invalid:
        if user_month.lower() in months_full:
            month_invalid = False
            return months_full.index(user_month)+1
        elif user_month.lower() in months_short:
            month_invalid = False
            return months_short.index(user_month)+1
        elif user_month.isdigit():
            month_invalid = False
            return int(user_month)
        else:
            print("That is an invalid month. Please try again")
            user_month = input("What month were you born?: ")

user_month_int = validate_date(user_month)

today = datetime.date.today()
event_date = datetime.date(year=user_year, month=user_month_int, day=user_day)

delta_event_date = event_date - today

years_difference = (delta_event_date.days//365)
months_difference = ((delta_event_date.days - years_difference * 365) // 30)
# weeks_difference
leap_years = years_difference//4
weeks_difference = (((delta_event_date.days - years_difference * 365) - months_difference * 30 - leap_years) // 7)
days_difference = (((delta_event_date.days - years_difference * 365) - months_difference * 30 - leap_years) - weeks_difference * 7)

if delta_event_date.days < 0:
    print("Your event is already over man!")
else:
    print(f"Your event is in {years_difference} years, {months_difference} months, {weeks_difference} weeks and {days_difference} days!")