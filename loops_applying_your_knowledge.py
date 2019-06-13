"""
title: loops_applying_your_knowledge
author: isruthi
date: 2019-06-13 13:40
"""

# part 1 - ex. 1
loop1 = [89, 41, 73, 90]
for i in loop1:
    print(i)


# part 1 - ex. 2
for i in range(5, 15):
    print(i, end=" ")
print()


# part 1 - ex. 3
for i in range(100, 201, 10):
    print(i, end=" ")
print()


# part 1 - ex. 4
for i in range(80, 31, -8):
    print(i, end=" ")
print()


# part 1 - ex. 5
for i in range(3):
    print("Alright", end=" ")
print()


# part 2 - ex. 1
number = 10
while number > 0:
    print(number, end=" ")
    number = number - 1
print()


# part 2 - ex. 2
response = int(input("Enter an integer greater than 0: "))

while response <= 0:
    print("Invalid")
    response = input("Enter an integer greater than 0: ")

print("This number is valid!")

# part 2 - ex. 3
response1 = int(input("Enter an integer: "))
response2 = int(input("Enter an integer larger than the last integer you entered: "))

while response1 > response2:
    print("Invalid. Second integer entered must be larger than the first integer entered.")
    response1 = int(input("Enter an integer: "))
    response2 = int(input("Enter an integer larger than the last integer you entered: "))

while response2 >= response1:
    print(response1, end=" ")
    response1 = response1 + 1
print()

# part 2 - ex. 4
response4 = input("Enter response: ")

while response4 not in ['Y', 'y', 'yes', 'YES', 'N', 'n', 'no', 'NO']:
    print("Invalid response")
    response4 = input("Enter response: ")

print("Valid response")