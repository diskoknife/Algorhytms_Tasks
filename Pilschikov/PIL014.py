#  Copyright (c) 2021.
#  Vyacheslav Shchurov (diskoknife@gmail.com)
"""

Task 16.18 page 103
Something about lists

"""

l = []
e = "elem"
l.insert(0, e)  #task A
l.append(e)  #task B
l.insert(1, e)  #task C
e1 = "new elem"
l = [e + e1 for e in l if e == 'elem']  #task D
e2 = 'newfoundelem'
l.extend(e1 + e2)  #task E
l.sort()  #last task
print(l)