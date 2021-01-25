# task 4.1 page 18
# need to find max or min depending on the conditions
from math import cos, sin, atan, log, asin, sqrt

x = float(input())
y = cos(x) ** 2 if 2 > x > 0 else 1 - sin(x) ** 2  # point A

a = sqrt(asin(1 + log(x)))  # point B

x_1 = input()
y_1 = input()
x_1 = max(x_1, y_1)  # point C

a_1 = input()
b_1 = input()
c_1 = input()
d = max(a_1, b_1, c_1)  # point D

x_2 = input()
y_2 = input()
z_2 = max(x_2, y_2) if x > 0 else min(x_2, y_2)  # point E
