#  Copyright (c) 2021.
#  Vyacheslav Shchurov (diskoknife@gmail.com)
"""

Task 17.5
Read the text from file, read the circle braces and print their nums in text
for every braces pair

"""

braces = []
num_braces = []

with open("PIL023.txt", "r") as f:
    text = f.read()
    for i in range(len(text)):
        if text[i] in ['(', ')']:
            braces.append(text[i])
            num_braces.append(i)

