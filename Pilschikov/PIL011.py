"""

Task 11.20, page 63
we've got 3 real arrays filled by 50 numbers. Calculate the answer by description

"""
import random

list1 = [random.random() for i in range(0, 50)]
list2 = [random.random() for i in range(0, 50)]
list3 = [random.random() for i in range(0, 50)]

res = (min(list2)/max(list1) + max(list3)/(min(list2) + min(list3))
       if min(list1) < max(list2) else
       max(list2) + max(list3) + min(list3))

print(res)