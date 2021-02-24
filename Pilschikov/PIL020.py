#  Copyright (c) 2021.
#  Vyacheslav Shchurov (diskoknife@gmail.com)
"""

Exercise 17.4, page 111
With using stack do next tasks:
a) line-by-line read text file and print all of strings in reverse
b) check if string are formula <formula> = <term>|<term>-<formula>|
<term>+<formula>
<term>=<name>|(<formula>)|[formula]
<name>=x|y|z
c) check if in text file printed without mistakes formula:
<formula>=<num>|M(<formula>, <formula>)|m(<formula>,<formula>

"""
# Here we make a) task

with open("PIL020_1.txt", "r") as f:    #task a
    for line in f.readlines():
        print(line[::-1])

