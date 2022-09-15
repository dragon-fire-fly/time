import datetime

# # current date and time
# today = datetime.datetime.today()
# print(today)

# # current date
# print(datetime.date.today())

# year = today.year()
# print(year)

current_time = datetime.datetime.now().strftime("%H:%m:%S")
print(current_time)

current_year = datetime.datetime.now().strftime("%Y")
print(current_year)

current_day = datetime.datetime.today().strftime("%A")
print(current_day)

# convert a string into a datetime object

date_as_string = "2022-09-15"
date_as_object = datetime.datetime.fromisoformat(date_as_string)

print(date_as_string)
print(date_as_object)
print(type(date_as_object))


# leap year
# crieria:
# evenly divisible by 4
# if the number is evenly divisible by 100, it must also be evenly divisible by 400

current_year = datetime.datetime.today().strftime("%Y")

def leap_year_calculator(year):
    if year % 100 == 0:
        if year % 400 != 0:
            print(f"{year} is not a leap year!")
        else:
            print(f"{year} is a leap year!")
    elif year % 4 == 0:
        print(f"{year} is a leap year!")

    else:
        print(f"{year} is not a leap year!")

leap_year_calculator(2012)
leap_year_calculator(2021)
leap_year_calculator(1900)
leap_year_calculator(2000)