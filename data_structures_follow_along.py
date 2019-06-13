"""
title: data_structures_follow_along
author: isruthi
date: 2019-06-13 11:24
"""

my_friends = ["Rizzo", "French", "Danny", "Kenickie", "Marty", "Sandy", "Cha-Cha", "Patty", "Sonny", "Calhoun"]
print(len(my_friends))
print(my_friends[3])
print(my_friends[-1])
print(my_friends[4:9])
print(my_friends[-3:])
print(my_friends[:3])
print(my_friends[::2])
my_friends[7] = "Elizabeth"
print(my_friends)
my_friends.append("Danny")
del my_friends[6]
print(my_friends)
