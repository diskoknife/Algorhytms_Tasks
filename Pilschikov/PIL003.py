# table of TRUTH, page 26, task 5.30
a = bool(0)
b = bool(0)
c = bool(0)


def f_x(a, b, c):
    f = bool((a and b) or not (b or c))
    return f


table = ["{0:b}".format(i) for i in range(0, 8)]
print(table[0])

# TODO: make real table of truth please
