"""Write a recursive function for search Fibonacci's numbers"""

def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


x = int(input("Enter index number of needed Fibonacci's numeral:"))
print(fib(x))
