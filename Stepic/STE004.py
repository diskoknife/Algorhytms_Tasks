"""

Calculate sum of all input elements

"""

n = int(input("Enter number of elements:"))
res = 0
for i in range(0, n):
    res += int(input("Enter next element"))

print("Sum is ", res)