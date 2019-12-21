#!/usr/bin/env python3

## Import only the functions we need
from time import localtime, mktime, strftime

### Since we only called the functions we need from time, we can call the function directly
### Example: module()
### Example: localtime()

## Start the timer:
start_time = localtime()

## Wait for user to stop the Timer
input("Press the 'Return' key to stop the timer ")

## Collect When Timer stopped
stop_time = localtime()

## Calculate The difference
difference = mktime(stop_time) - mktime(start_time)

## Notify User of results
print(f"Start Time: {strftime('%X', start_time)}")
print(f"Stop Time: {strftime('%X', stop_time)}")
print(f"Total Time: {difference} seconds")
