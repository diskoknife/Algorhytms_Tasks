#  Copyright (c) 2021.
#  Vyacheslav Shchurov (diskoknife@gmail.com)
"""

Task 11.20, page 63
we've got 3 real arrays filled by 50 numbers. Calculate the answer by description

"""
import random

list1 = [random.random() for i in range(0, 50)]
list2 = [random.random() for i in range(0, 50)]
list3 = [random.random() for i in range(0, 50)]

res = (min(list2) / max(list1) + max(list3) / (min(list2) + min(list3))
       if min(list1) < max(list2) else
       max(list2) + max(list3) + min(list3))

print(res)

if __name__ == '__main__':
    print("Actually, this is simple task from the student book.\n"
          "If you wanna some interaction... OK\n"
          "\nDo you want to see the random-filled arrays?\n"
          "print 'yes' if yes\n")
    command = input()
    if 'yes' in command:
        print('First array:\n', list1)
        print('Second array:\n', list2)
        print('Third array:\n', list3)
    print('By some magic maths(which you can read at the page 63, task 11.20, '
          'We\'ve got next result: ', res)
