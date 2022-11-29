#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_d = str(number)[-1]
if int(last_d) > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, last_d))
elif int(last_d) == 0:
    print("Last digit of {} is {} and is 0".format(number, last_d))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, last_d))
