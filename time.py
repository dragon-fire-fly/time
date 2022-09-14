import time

x = time.time()         # displays the current UNIX time

y = time.ctime(x)       # convert time - displays a user readable date stamp (e.g. Wed Sep 14 11:04:45 2022)


time.gmtime(0)          # shows detailed info about the date, seperated into year, month, day, hour, etc. 
                        # can be useful for calling specific units of time (e.g. minute)

time.gmtime()           # passing no arguments automatically shows todays date

time.sleep(1)           # pauses the time of the program for the argument number of seconds 


