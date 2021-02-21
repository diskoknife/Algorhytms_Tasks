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
    names = ('x', 'y', 'z')
    operands = ('=', '+', '-', '/', '*')
    is_operand = False
    if line[0] in names:
        for i in range(1, len(line)):
            if line[i] == " ":
                pass
            elif line[i] in operands and is_operand == False:
                is_operand = True
                pass
            elif line[i] in names and is_operand == True:
                is_operand = False
                pass
            else:
                break
            is_line = True
    return is_line

with open("PIL_021_1.txt", "r") as f:
    for line in f.readlines():
        if check_line_formula(line):
            print(line + " is formula\n")
        else:
            print(line + " is not a formula\n")