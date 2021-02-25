#  Copyright (c) 2021.
#  Vyacheslav Shchurov (diskoknife@gmail.com)
"""

Exercise 4.18
Fill array with random nums from 1 to 50 and find max of them

"""
import random

x_list = [random.random() for i in range(1, 50)]
answer = max(x_list)
print("Random generated list:\n")
print("Max from this list:\n" + answer)
