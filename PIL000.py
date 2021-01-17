# task 4.1 page 18
from math import cos, sin, atan, log, asin, sqrt

x = float(input())
y = cos(x) ** 2 if 2 > x > 0 else 1 - sin(x) ** 2  # point A

a = sqrt(asin(1 + log(x)))  # point B
