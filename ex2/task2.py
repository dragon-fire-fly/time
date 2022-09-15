import datetime

current_datetime = datetime.date.today()

print(current_datetime)

# subtract 15 days
tdelta = datetime.timedelta(15)
past_day = current_datetime - tdelta
print(past_day)

# add 7 days
tdelta = datetime.timedelta(7)

future_day = current_datetime + tdelta
print(future_day)


# Rent
start_date = datetime.date(year=2021, month=1, day=1)
due_date = datetime.date(year=2021, month=1, day=25)

due_days = due_date - start_date
due_days_reformat = due_days.days

date_reformatted = due_date.strftime("%d %B, %Y")

print(start_date)
print(date_reformatted)
print(due_days)

print(f"Hello Friedrich, your rent of 300 € is due on {date_reformatted}. That's in {due_days_reformat} days!")