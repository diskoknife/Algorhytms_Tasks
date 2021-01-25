# task 12.3 page 72
# create a recursive pow function

x, n = map(int, input().split())

def pow (x, n):

    if n == 0:
        x = 1
        return x
    elif n < 0:
        x = (1/pow(x, abs(n)))
        return x
    else:
        x = x * pow(x, n - 1)
        return x

print(pow(x, n))