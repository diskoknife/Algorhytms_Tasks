"""

Task 17.3, page 110
define some functions that are appending stack(list)
def clear_stack(list):
    #make a clear(fill with nulls?) list with size of input list

def check_clear_stack(list):
    #check if input stack are null

def instack(list, x):
    #append to stack elem x

def fromstack(list, x):
    #delete from stack last elem and put in x elem

"""


def clear_stack(list):
    nullstack = [0 for i in range(len(list))]
    return nullstack

def check_clear_stack(list):
    is_clear = True
    for i in range(len(list)):
        if list[i] is not 0:
            is_clear = False
    return is_clear

def instack(list, x):
    list += x
    return list

def fromstack(list, x):
    list[-1] = x
    return list