#  Copyright (c) 2021.
#  Vyacheslav Shchurov (diskoknife@gmail.com)
"""

Task 9.10, page 51
We have 7x4 matrix. Shuffle her elements to make bigger elem in left upper corner.

"""
import random


def sort(matrix):
    for i in range(len(matrix)):
        horizontal_swap = True  # define bool to run while at least once
        while horizontal_swap:
            horizontal_swap = False  # if we don't swap anything - this is our last cycle
            for j in range(len(matrix[i])):
                try:
                    if matrix[i][j] < matrix[i][j + 1]:
                        horizontal_swap = True
                        matrix[i][j], matrix[i][j + 1] = matrix[i][j + 1], matrix[i][j]
                except IndexError:
                    pass
    """Now do same swap for columns
    We already have max value in every row at [0] position"""
    for i in range(len(matrix)):
        vertical_swap = True
        while vertical_swap:
            vertical_swap = False
            try:
                if matrix[i][0] < matrix[i + 1][0]:
                    vertical_swap = True
                    matrix[i][0], matrix[i + 1][0] = matrix[i + 1][0], matrix[i][0]
            except IndexError:
                pass
    return matrix


a = [[random.randrange(-100, 100) for i in range(7)] for i in range(4)]

print(sort(a))
