import os
import time
import random

dash_list = [
    "-","-","-","-","-","-","-","-","-","-",
    "-","-","-","-","-","-","-","-","-","-",
    ]

# print the dash_list
def dash_bar(dash_list, percent):
    progress = ""
    for dash in dash_list:
        progress += dash
    print("Downloading...")
    print(progress, percent, "%")


# for each "-" in dash_list, replace with a "#"
def progress_bar(dash_list):
    percent = 0
    for i in range(0,19):
        dash_list[i] = "✔️"
        percent += 5
        dash_bar(dash_list, percent)
        time.sleep(random.random())
        os.system('clear')

# print the progress bar
print("Starting Download...")
time.sleep(1)
os.system('clear')
progress_bar(dash_list)

print("Download complete!")