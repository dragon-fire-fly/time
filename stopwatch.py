import time
import os
import math
# import keyboard
# import pynput
timer = False

start_timer = input("Press any key to start the stopwatch: ")

if start_timer != "":
    start_time = time.time()
    timer = True

while timer:
    try:
        print("Timer started.... ")
        stopwatch_time = int(time.time() - start_time)
        if stopwatch_time >= 5:
            minutes = math.floor(stopwatch_time/5)
            seconds = (stopwatch_time-5) % 5
            stopwatch_time = f"{minutes} min {seconds}"
        print(f"{stopwatch_time} s")
        time.sleep(1)
        os.system('clear')
    except KeyboardInterrupt:
        print(f"Time taken: {stopwatch_time} s")
        break
    #     print("key pressed")

# stop_time = input("Press any key and enter to stop the timer:")


# carriage return: end = "\r", flush = True