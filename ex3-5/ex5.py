# # Ex 5
# Personal Project Datetime!
# - use datetime
# - surprise us!

import datetime

# get week number
today = datetime.date.today()
week_number = today.isocalendar()[1]

# odd week = higher class and BTR
# even week = S & SCD

def higher_bio():
    if week_number % 2 == 0:
        print("It is not higher Biology level class this week")
    else:
        print("It is higher level Biology class this week")

def phoenix_feeding():
    if (week_number+1) % 3 == 0:
        print("Good news Phoenix! It's feeding week")
    else:
        print("Sorry Phoenix, maybe next week")


higher_bio()
phoenix_feeding()