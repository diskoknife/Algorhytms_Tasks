# task 11.19
# calculate sum of arrays based on descriptioñ
from random import randint
list1 = [randint(-1000, 1000) for i in range(20)]
list2 = [randint(-1000, 1000) for i in range(20)]
res1 = 0
for i in range(0, 15):
    res1 += list1[i] + list2[i]

u = sum(list1)**2 if res1 > 0 else sum(list2, 10)**2
print(list1, res1, u)