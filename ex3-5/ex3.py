# # Ex 3
# Birthday Day Calculator
# - takes birthday as input
# - prints out years, months, weeks & days since

from curses.ascii import isdigit
import datetime

user_year = int(input("What year were you born?: "))
user_month = input("What month were you born?: ")
user_day = int(input("What day were you born?: "))

today = datetime.date.today()

this_year = today.year
this_month = today.month
this_day = today.day

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
def month(user_month):
    month_invalid = True
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

user_month_int = month(user_month)

today = datetime.date.today()
birthdate = datetime.date(year=user_year, month=user_month_int, day=user_day)

delta_birthdate = today - birthdate


years_difference = (delta_birthdate.days//365)
months_difference = ((delta_birthdate.days - years_difference * 365) // 30)
# weeks_difference
leap_years = years_difference//4
weeks_difference = (((delta_birthdate.days - years_difference * 365) - months_difference * 30 - leap_years) // 7)
days_difference = (((delta_birthdate.days - years_difference * 365) - months_difference * 30 - leap_years) - weeks_difference * 7)

print(f"You are {years_difference} years, {months_difference} months, {weeks_difference} weeks and {days_difference} days old!")