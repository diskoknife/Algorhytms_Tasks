#  Copyright (c) 2021.
#  Vyacheslav Shchurov (diskoknife@gmail.com)
"""

Exercise 12.12, page 73
Calculate num of numbers in the text in the input file.

"""


def calc(input_file):
    f = open(input_file, 'r')
    inp_str = f.read()
    count = 0
    num_tuple = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    for i in range(len(inp_str)):
        if inp_str[i] in num_tuple:
            count += 1
    f.close()
    return count


print("Count of numeric elements: ", calc('sample.txt'))
