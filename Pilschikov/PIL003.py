# table of TRUTH, page 26, task 5.30
a = bool(0)
b = bool(0)
c = bool(0)

def f_x(a, b, c):
    f = bool((a and b) or not (b or c))
    return f


if not a:
    if not b:
        if not c:
            table_truth = [a, b, c, f_x(a, b, c)]
            c = not c


print(table_truth)