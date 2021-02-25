#  Copyright (c) 2021.
#  Vyacheslav Shchurov (diskoknife@gmail.com)
"""

Task 4.1 page 18
Need to find max or min depending on the conditions

"""
from math import cos, sin, log, asin, sqrt


# Here we define start of program and all the inputs
def main():
    choice = int(input("Choose the branch of solution between 1-5\n"
                       "You can read the description of solution in the "
                       "Pilschikov book\n"))
    args = map(float, input("Write an arguments for function\n").split())
    print(choose_branch(choice)(*args))


# Choose the right lambda func
def choose_branch(x):
    case = {
        1: task_a,
        2: task_b,
        3: task_c,
        4: task_d,
        5: task_e
    }
    return case.get(x)


# Field for lamda functions based on description to exercise
task_a = lambda x: cos(x) ** 2 if 2 > x > 0 else 1 - sin(x) ** 2
task_b = lambda x: sqrt(asin(1 + log(x)))
task_c = lambda x, y: max(x, y)
task_d = lambda x, y, z: max(x, y, z)
task_e = lambda x, y: max(x, y) if x > 0 else min(x, y)

if __name__ == "__main__":
    main()
