import time
import os
import math

timer = True

countdown_time = int(input("How long would you like the timer to be?: "))
units = input("Is that in seconds(s), minutes(m) or hours(h)?: ")
if units == "m":
    countdown_time *= 60
elif units == "h":
    countdown_time *= 3600

while timer:
    print("Time remaining: ")
    
    if countdown_time >= 3600:
        hours = math.floor(countdown_time/3600)
        # minutes = math.floor(countdown_time-3600)%60
        seconds = (countdown_time-60) % 60
        minutes = 0
        print(hours, minutes, seconds)
    elif countdown_time >= 60:
        minutes = math.floor(countdown_time/60)
        seconds = (countdown_time-60) % 60
        print(minutes, seconds)
    elif countdown_time < 60:
        print(countdown_time)
    time.sleep(1)
    countdown_time -= 1
    os.system('clear')
    if countdown_time == 0:
        print("Time's up!")
        timer = False


# minutes = math.floor(stopwatch_time/5)
#             seconds = (stopwatch_time-5) % 5
#             stopwatch_time = f"{minutes} min {seconds}"