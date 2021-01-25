# print input num by romanic num
from math import floor

try:
    x = int(input('Énter the arabic numeral'))
except:
    print('Nan')

def translate_to_romanic(x):
    numeral = []
    m = floor(x / 1000)
    c_p = x % 1000
    d = 1 if c_p >= 500 else 0
    c = floor(c_p / 100) if d == 0 else floor(c_p / 100) - 5    #check if we have d state
    x_p = c_p % 100
    l = 1 if x_p >= 50 else 0
    x = floor(x_p - 5/10) if l == 0 else floor(x_p/10) - 5
    i_p = x_p % 10
    v = 1 if i_p >= 5 else 0
    i_ = i_p if v == 0 else i_p - 5
    for i in range(0, m):
        numeral.append('M')
    if d == 1:
        numeral.append('D')
    for i in range(0, c):
        numeral.append('C')
    if l == 1:
        numeral.append('L')
    for i in range(0, x):
        numeral.append('X')
    if v == 1:
        numeral.append('V')
    for i in range(0, i_):
        numeral.append('Í')
    str1 = ""
    for obj in numeral:
        str1 += obj
    return print('Romanic numeral:',  str1)

translate_to_romanic(x)