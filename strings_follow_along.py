"""
title: strings_follow_along
author: isruthi
date: 2019-06-13 09:46
"""

# strings follow-along
phrase = "Don't count your chickens before they hatch"
slogan = "For Everything Else, There's MasterCard"
combined = f"{phrase}. {slogan}"
print(combined)
print((phrase + "\n") * 3)
print(slogan[6])
print(combined[-1])
print(phrase[::2])
print(phrase[17:25])
print(combined[::2])
print("m" in slogan)
print(combined.upper())
print(combined.lower())
print(" ".join(combined))
print(slogan[::-1])