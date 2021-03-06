"""#

Recursive task
Calculate the number of combinations from n to k
Formula: C(n, k) = C(n-1, k) + C(n-1, k-1)

"""


def combnk(n, k):
    if k == 0 or k > n:
        return 0
    elif k is n:
        return 1
    else:
        cnk = combnk(n - 1, k) + combnk(n - 1, k - 1)
        return cnk


if __name__ == '__main__':
    n, k = map(int, input("Enter the num of elems and k replacements")
               .split())  # read two numbers splitted by space
    print(combnk(n + 1, k + 1))
