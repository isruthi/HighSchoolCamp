"""
title: random_practice
author: isruthi
date: 2019-06-12 09:53
"""

import random

name = input("Enter your name: ")
salary = input("Enter your salary: ")
salary = int(salary)
print(f"{name}, your current salary is ${salary}.")

raise_per = (random.randint(0, 100))
print(f"Your raise is {raise_per}% of ${salary}")

raise_amount = int((salary * raise_per * 0.01)+salary)

print(f"{name}, your new salary is ${raise_amount}.")