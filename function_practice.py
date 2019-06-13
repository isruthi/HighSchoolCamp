"""
title: function_practice
author: isruthi
date: 2019-06-12 11:27
"""

# function lab ex.1
def age_calculator(x,y):
    return int(x) - int(y)

x = int(input("Enter current year: "))
y = int(input("Enter birth year: "))
print(age_calculator(x,y))


# function lab ex.2 - averaging numbers
def avg_numbers (a,b,c):
    return (int(a) + int(b) + int(c))/3

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter another another number: "))
print(avg_numbers(a,b,c))