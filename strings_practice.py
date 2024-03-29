"""
title: string_practice
author: isruthi
date: 2019-06-11 13:45
"""

# strings lab ex. 1
answer = input("Enter a character:")
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
print(answer in alphabet)


# strings lab ex. 2 - short hand
short = input("Enter a phrase:")
short_hand = short.replace("and", "&").replace("too", "2").replace("you", "U").replace("You", "U").replace("for", "4")\
    .replace("a", "").replace("e", "").replace("i", ""). replace("o", "").replace("u", "")
print(short_hand)


# strings lab ex. 3 - remove case and punctuation
check = input("Enter a phrase:")
removing = check.lower().replace("`", "").replace("~", "").replace("!", "").replace("@", "").replace("#", "")\
    .replace("$", "").replace("%", "").replace("^", "").replace("&", "").replace("*", "").replace("(", "")\
    .replace(")", "").replace("-", "").replace("_", "").replace("+", "").replace("+", "").replace("[", "")\
    .replace("]", "").replace("{", "").replace("}", "").replace("|", "").replace(";", "").replace(":", "")\
    .replace("'", "").replace('"', "").replace(",", "").replace(".", "").replace("<", "").replace(">", "")\
    .replace("/", "").replace("?", "").replace(" ", "")
print(removing)


#strings lab ex. 4 - palindrome
palindrome = input("Enter a phrase:")
new_palindrome = palindrome.lower().replace("`", "").replace("~", "").replace("!", "").replace("@", "").replace("#", "")\
    .replace("$", "").replace("%", "").replace("^", "").replace("&", "").replace("*", "").replace("(", "")\
    .replace(")", "").replace("-", "").replace("_", "").replace("+", "").replace("+", "").replace("[", "")\
    .replace("]", "").replace("{", "").replace("}", "").replace("|", "").replace(";", "").replace(":", "")\
    .replace("'", "").replace('"', "").replace(",", "").replace(".", "").replace("<", "").replace(">", "")\
    .replace("/", "").replace("?", "").replace(" ", "")
backwards_palindrome = new_palindrome[::-1]
print(new_palindrome == backwards_palindrome)


#strings lab ex. 5 - credentials generator
import random

first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
birth_city = input("Enter Birth City: ")
university = input("Enter Alma Mater University: ")
relative = input("Enter a Relative's Name: ")
friend = input("Enter a Friend's Name: ")

employee_id1 = (first_name[:3])
employee_id2 = (last_name[-2:])
employee_id = f"{employee_id1}{employee_id2}"
user_name1 = (birth_city[:2])
user_name2 = (university[-3:])
user_name = f"{user_name1}{user_name2}"
number1 = random.randint(0, len(relative) - 1)
number2 = random.randint(0, len(friend) - 1)
password1 = (relative[number1:])
password2 = (friend[0:number2])
password = f"{password1}{password2}"

print(f"Employee ID: {employee_id}")
print(f"User Name: {user_name}")
print(f"Password: {password}")
