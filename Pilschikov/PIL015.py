#  Copyright (c) 2021.
#  Vyacheslav Shchurov (diskoknife@gmail.com)
"""

Task 16.35 page 107
check if input text is symmetric

"""

text = input("Введите текст\n")
half_text = text[len(text)//2:]
half_text = half_text[::-1]
print(half_text + " //is reversed")
print(text[len(text)//2:] + " //second half origin")
print(text[:len(text)//2] + " //first half")
if half_text == text[:len(text)//2]:
    print("is symmetric")
else:
    print("non symmetric")