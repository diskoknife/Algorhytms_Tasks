#  Copyright (c) 2021.
#  Vyacheslav Shchurov (vschyurov@psystems.biz)
"""

task 8.1 page 40:
fill some arrays and show num of elements
show type of values
show the link to first and last element"""


from datetime import date

day = ['Yesterday', 'Today', 'Tomorrow']
vec = [x for x in range(31)]
print(vec)
print(day[1], date.today())


print(type(day))
print(type(vec))
print(date)