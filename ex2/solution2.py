# Task 1

from datetime import datetime, timedelta


current_datetime = datetime.now()

current_datetime = current_datetime - timedelta(days=15)
print(current_datetime.strftime("%Y-%m-%d"))

# Task 2

current_datetime = datetime.now()
current_datetime += timedelta(days=7)
print(current_datetime.strftime("%Y-%m-%d"))


# Task 3
start_date = datetime(year=2020, month=1, day=1)
due_date = start_date + timedelta(days=25)
message = "Hello Friedrich, your rent of 199.00 € is due on {due_date}".format(
    due_date=due_date.strftime("%d %B, %Y"),
)
print(message)
