#!/usr/bin/env python3

## Import Entire Time Function
import time
### Since we imported the entire TIME module we need to chain the module to get the submodules
### Example: module.submodules
### Example: time.localtime


## Start the timer
start_time = time.localtime()
print(f"Timer started at {time.strftime('%X', start_time)}")

## Wait for user to stop the Timer
input("Press return key to stop the timer ")

## Stop the Timer
stop_time = time.localtime()

## Calculate the difference
difference = time.mktime(stop_time) - time.mktime(start_time)

## Notify User when timer stopped
print(f"Timer stopped at {time.strftime('%X', stop_time)}")
print(f"Total Time: {difference} seconds")
