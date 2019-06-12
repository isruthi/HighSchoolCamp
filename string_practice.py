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
symbols = not "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
removing = check.lower().replace({symbols}, "")
print(removing)