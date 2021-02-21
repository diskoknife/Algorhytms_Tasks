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
# Here we make b) and c) tasks

def check_line_formula(line):
    is_line = False
    name = ('x', 'y', 'z')
    if line[0] in name:
        is_line = True
    return is_line

with open("PIL_021_1.txt", "r") as f:
    for line in f.readlines():
        check_line_formula(line)