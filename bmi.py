#!/usr/bin/env python3

######################################
## Calculates users Body Mass Index ##
## Written By: Shawn Oseguera Goetz ##
##        Written On: 11/30/19      ##
######################################

## Gathering Info Function
def gather_info():
    height = float(input("What is your height? (inches or meters) "))
    weight = float(input("What is your weight? (pounds or kilograms) "))
    system = input("Are your measurements in metric or imperial units? ").lower().strip()
    return (height, weight, system)

## Calculating the BMI
def calculate_bmi(weight, height, system='metric'):
    """
    Return the Body Mass Index (BMI) for the
    given weight, height, and measurement system.
    """

    if system == 'metric':
        bmi = (weight / (height ** 2))
    else:
        bmi = 703 * (weight / (height ** 2))
    return bmi


## Testing Code MySelf
height, weight, system = gather_info()
print(f"You're weight is: {weight} You're height is: {height} You're choosen measurement system is: {system}")

bmi = calculate_bmi(weight, height, system)
print(f"You're bmi is: {bmi}")

## Testing Code With While Loop
while True:
    height, weight, system = gather_info()
    if system.startswith('i'):
        bmi = calculate_bmi(height, weight, system)
        print(f"Your calculcated BMI is: {bmi} , in imperial")
        break
    elif system.startswith('m'):
        bmi = calculate_bmi(height, weight, system)
        print(f"Your calculated BMI is: {bmi} , in metrics")
        break
    else:
        print("Error: Unknown measurement system. Please use imperial or metric.")


