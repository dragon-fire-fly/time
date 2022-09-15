import datetime

# help(datetime.date)

# gvr = datetime.date(1956, 1, 31)
# print(gvr)

# print(gvr.year)
# print(gvr.month)
# print(gvr.day)

# mil = datetime.date(2000, 1, 1)
# dt = datetime.timedelta(100)
# print(mil + dt)

# print(gvr.strftime("%A, %B %d, %Y"))

# message = "GVR was born on {:%A, %B %d, %Y}."
# print(message.format(gvr))

# launch_date = datetime.date(2017, 3, 30)
# launch_time = datetime.time(22, 27, 0)
# launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0)

# print(launch_date)
# print(launch_time)
# print(launch_datetime)

# print(launch_time.hour)
# print(launch_time.minute)
# print(launch_time.second)

# print(launch_datetime.year)
# print(launch_datetime.month)
# print(launch_datetime.day)
# print(launch_datetime.hour)
# print(launch_datetime.minute)
# print(launch_datetime.second)

# now = datetime.datetime.today()
# print(now)

# moon_landing = "7/20/1969"
# moon_landing_datetime = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")
# print(moon_landing_datetime)
# print(type(moon_landing_datetime))


# # ISO 8601 standard date format = YYYY-MM-DD

# date_as_string = "2022-01-26"

# print(datetime.date.fromisoformat(date_as_string))

# valentines_day = datetime.datetime(2021, 2, 14, 8, 20, 30)
# print(valentines_day)

# # Can also add names for each argument
# date = datetime.date(year=2022, month=1, day=26)

# usa_meeting = "January 1, 2005"

# converted_date = datetime.datetime.strptime(usa_meeting, "%B %d, %Y")
# print(converted_date)
# print(type(converted_date))


# # changing the formatting of the object
# now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# print(now)

# # can cherrypick certain parts of the datetime object
# date = datetime.datetime.now().strftime("%D")
# year = datetime.datetime.now().strftime("%Y")
# month = datetime.datetime.now().strftime("%m")
# day = datetime.datetime.now().strftime("%d")
# hour = datetime.datetime.now().strftime("%H")
# minute = datetime.datetime.now().strftime("%M")
# second = datetime.datetime.now().strftime("%S")
# print(date)
# print(year)
# print(month)
# print(day)
# print(hour)
# print(minute)
# print(second)

# strptime is for working with strings (parsing strings)
# strftime is for working with datetime objects

# # returns a tuple containing ISO year, week number and weekday
# week_no = datetime.datetime.isocalendar()
# print(week_no)

# help(datetime.datetime.isocalendar)

chosen_date = "March 28 2011, 16:12"

converted_date = datetime.datetime.strptime(chosen_date, "%B $d %Y, %H:%M")

print(converted_date)