"""

Task5.8 page 23
fill array with rand values and find difference between max and min

"""
import random

x_list = [random.randrange(1, 100000) for i in range(1, 100)]
ans = max(x_list) - min(x_list)
print("difference between min and max is", ans)

# Task 5.16 | Fibonacci's numbers
# write an algorithm to find inputed Fibonacci's num and find first bigger value
print("enter the ordinal of needed Fibonacci's number")
n = int(input())
fib_seq = []
fib_sum = int()
x = 0
y = 1
z = 0
print("enter the random positive number")
m = int(input())

for i in range(n):
    fib_seq.append(x + y)
    try:
        x = fib_seq[i - 1]
    except:
        pass
    y = fib_seq[i]
    if y > m and z == 0:
        z = fib_seq[i]
    print("|", fib_seq[i], "|")
    if fib_seq[i] < 1000:
        fib_sum = fib_sum + fib_seq[i]

if z != 0:
    print("first num that bigger than yours:", z)
else:
    print("There is no bigger nums than yours")

print("Sum of all Fibonacci's sequence above 1000 nums in your sequence:", fib_sum)
