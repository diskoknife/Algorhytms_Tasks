#  Copyright (c) 2021.
#  Vyacheslav Shchurov (diskoknife@gmail.com)
"""

Task 5.16 | Fibonacci's numbers
write an algorithm to find input Fibonacci's num and find first bigger value

"""


print("enter the ordinal of needed Fibonacci's number")
n = int(input())    # Ordinal of needed Fibonacci sequence
fib_seq = [0, 1]
fib_sum = sum(fib_seq)
z = 0
print("enter the random positive number")
rand_num = int(input())

for i in range(n):
    try:
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
    except IndexError:
        pass
    if fib_seq[i] > rand_num and z == 0:
        z = fib_seq[i]
    print("|", fib_seq[i], "|")
    if fib_seq[i] < 1000:
        fib_sum = fib_sum + fib_seq[i]

if z != 0:
    print("first num that bigger than yours:", z)
else:
    print("There is no bigger nums than yours")

print("Sum of all Fibonacci's sequence above 1000 nums in your sequence:", fib_sum)