"""

Exercise 4.18
Fill array with random nums from 1 to 50 and find max of them

"""
import random

x_list = [random.random() for i in range(1, 50)]
ans = max(x_list)
print(ans)