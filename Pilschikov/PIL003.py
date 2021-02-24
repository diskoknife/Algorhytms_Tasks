#  Copyright (c) 2021.
#  Vyacheslav Shchurov (vschyurov@psystems.biz)
"""

Table of TRUTH, page 26, task 5.30

"""

a = bool(0)
b = bool(0)
c = bool(0)


def f_x(a, b, c):  # here we define truth function by task
    f = bool((a and b) or not (b or c))
    return f


table = ["{0:b}".format(i) for i in range(0, 8)] # here i want to fill truth table for 3 variables
# TODO: find how to split integer to fill the table with booleans
print(table)

# TODO: make real table of truth please

