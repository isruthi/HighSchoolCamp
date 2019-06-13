"""
title: strings_practice_function_version
author: isruthi
date: 2019-06-13 09:55
"""

# strings lab ex. 1
def is_letter(character):
    return character.lower() in "abcdefghijklmnopqrstuvwxyz"

character = input("Enter a character: ")
print(is_letter(character))
print(is_letter("i"))
print(is_letter("@"))


# strings lab ex. 2 - short hand
def short_hand(short):
    short = short.replace("and", "&").replace("too", "2").replace("you", "U").replace("You", "U").replace("for", "4")
    short = short.replace("a", "").replace("e", "").replace("i", ""). replace("o", "").replace("u", "")
    return short

phrase = input("Enter a phrase: ")
print(short_hand(phrase))
print(short_hand("Thank you for that! You are too sweet and kind!"))
print(short_hand("How are you today?"))


# strings lab ex. 3 - remove case and punctuation
def removing(check):
    check = check.lower().replace("`", "").replace("~", "").replace("!", "").replace("@", "").replace("#", "") \
        .replace("$", "").replace("%", "").replace("^", "").replace("&", "").replace("*", "").replace("(", "") \
        .replace(")", "").replace("-", "").replace("_", "").replace("+", "").replace("+", "").replace("[", "") \
        .replace("]", "").replace("{", "").replace("}", "").replace("|", "").replace(";", "").replace(":", "") \
        .replace("'", "").replace('"', "").replace(",", "").replace(".", "").replace("<", "").replace(">", "") \
        .replace("/", "").replace("?", "").replace(" ", "")
    return check

phrase2 = input("Enter a phrase: ")
print(removing(phrase2))
print(removing("Madam, I'm Adam"))


#strings lab ex. 4 - palindrome
def palindrome(check):
    check1 = check.lower().replace("`", "").replace("~", "").replace("!", "").replace("@", "")\
        .replace("#","").replace("$", "").replace("%", "").replace("^", "").replace("&", "").replace("*", "")\
        .replace("(", "").replace(")", "").replace("-", "").replace("_", "").replace("+", "").replace("+", "")\
        .replace("[", "").replace("]", "").replace("{", "").replace("}", "").replace("|", "").replace(";", "")\
        .replace(":", "").replace("'", "").replace('"', "").replace(",", "").replace(".", "").replace("<", "")\
        .replace(">", "").replace("/", "").replace("?", "").replace(" ", "")
    check2 = check1[::-1]
    return (check2 == check1)

phrase3 = input("Enter a phrase: ")
print(palindrome(phrase3))
print(palindrome("Madam, I'm Adam"))
print(palindrome("Computer"))

