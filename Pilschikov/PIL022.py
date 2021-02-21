"""

Task 16.14, page 102
Write a function which:
a) Check list to emptyness
b) Calculate average of list
c) Replace all x to y
d) Swap first and last elems
e) Check sort by alphabet of list
f) Find sum of last and pre-last elems of list

"""


def check_empty(list):  # task A
    if len(list) == 0:
        return True
    else:
        return False


def average(list):  # task B
    average = sum(list) / len(list)
    return average


def replace(list, from_elem, to_elem):  # task C
    for i in range(len(list)):
        if list[i] == from_elem:
            list[i] == to_elem
    return list


def swap_ends(list):    #task D
    list[0], list[-1] = list[-1], list[0]
    return list


def check_alphabet_sort(list):  # task E
    newlist = sorted(list)
    return newlist == list


def both_last_sum(list):    # task F
    res = list[-1] + list[-2]
    return res
