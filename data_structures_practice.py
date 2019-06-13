"""
title: data
author: isruthi
date: 2019-06-13 13:18
"""

# data structures lab ex. 1
import random

def shake_ball():
    input("Ask a question about your future: ")
    response = ["Yes definitely", "As I see it, yes", "Ask again later", "Cannot predict now", "Don't count on it",
                "Very doubtful", "You may rely on it", "Outlook good", "Reply hazy, try again", "My sources say no"]
    number = random.randint(0, len(response)-1)
    return response[number]

print(shake_ball())