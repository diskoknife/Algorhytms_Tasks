#  Copyright (c) 2021.
#  Vyacheslav Shchurov (diskoknife@gmail.com)
"""

Table of TRUTH, page 26, task 5.30

"""


def main():
    args = map(bool, input(print("Enter the three logical values of a, b, "
                                 "c vars\n Supported only"
                                 "'True' or 'False' or '1' or '0' definition")
                           ).split())
    print("Answer for (a&b)|!(b|c):\n")
    print(f_x(*args))


def f_x(a, b, c):  # here we define truth function by task
    f = bool((a and b) or not (b or c))
    return f


if __name__ == '__main__':
    main()
