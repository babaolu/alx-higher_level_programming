#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_num = int(f"{number}"[-1])
print(f"Last digit of {number:n} is {last_num:n}", end = " ");
if last_num > 5:
    print("and is greater than 5")
elif last_num == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
