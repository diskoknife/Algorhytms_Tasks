"""

Task 9.10, page 51
We have 7x4 matrix. Shuffle her elements to make bigger elem in left upper corner.

"""
import random

def sort(matr):
    for i in range(len(matr)):
        horizontal_swap = True  #define bool to run while at least once
        while horizontal_swap:
            horizontal_swap = False # if we don't swap anything - this is our last cycle
            for j in range(len(matr[i])):
                try:
                    if matr[i][j] < matr[i][j+1]:
                        horizontal_swap = True
                        matr[i][j], matr[i][j+1] = matr[i][j+1], matr[i][j]
                except IndexError:
                    pass
    """Now do same swap for columns
    We already have max value in every row at [0] position"""
    for i in range(len(matr)):
        vertical_swap = True
        while vertical_swap:
            vertical_swap = False
            try:
                if matr[i][0] < matr[i+1][0]:
                    vertical_swap = True
                    matr[i][0], matr[i+1][0] = matr[i+1][0], matr[i][0]
            except:
                pass
    return matr

a = [[random.randrange(-100, 100)for i in range(7)] for i in range(4)]

print(sort(a))