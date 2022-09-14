# Time

## What is UNIX time?

UNIX time is a system which is used for documenting a point in time. It is counting the number of seconds which have passed since the "UNIX Epoch" (00:00:00 UTC Jan 1st 1970). UNIX time excludes "leap seconds".

One day in UNIX time consists of 86,400 seconds.

At a point of time in 3.14.07 UTC 19th January 2038, the 32-bit UNIX clock will run out of units to continue counting. Therefore, systems will need to be upgraded to 64-bit UNIX clocks so that there are more units to continue counting.

In python, using the time module from the time library (time.time) displays the current UNIX time.

## The Y2K Problem/Millenium Bug

Years used to be stored as 2 digit numbers (89, 90, 91, etc.). This became a problem when the year crossed from 99 to 00 which would be interpreted as 1900.
300-600 billion $ spent to fix the problem! 