#  Copyright (c) 2021.
#  Vyacheslav Shchurov (diskoknife@gmail.com)
"""

task 9.16 page 51
fill array with integers

"""


def main():
    try:
        x = int(input(print("Choose the task num (1/2/3):\n")))
        print(switch_solution_branch(x))
    except TypeError:
        main()


def switch_solution_branch(x):
    solutions = {
        1: task_a(),
        2: task_b(),
        3: task_c()
    }
    return solutions.get(x)


n = 10

matrix1 = [[0 for i in range(n)] for j in range(n)]
matrix2 = [[0 for i in range(n)] for j in range(n)]
matrix3 = [[0 for i in range(n)] for j in range(n)]

def task_a(i=0):
    matrix1[i][i] = i
    if i < n - 1:
        return task_a(i + 1)
    else:
        return matrix1


def task_b(x=1):
    for i in range(n):
        for j in range(n):
            matrix2[i][j] = x
            x += 1
    return matrix2

def task_c():
    for i in range(n):
        for j in range(n):
            matrix3[i][9 - j] = 10 - i - j
    return matrix3


if __name__ == '__main__':
    main()
