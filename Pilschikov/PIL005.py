#  Copyright (c) 2021.
#  Vyacheslav Shchurov (diskoknife@gmail.com)
"""

Print input num by romanic num
Task 7.17, page 37. Convert arabic numerals into romanians

"""

from math import floor


def main():
    try:
        x = int(input('Énter the arabic numeral'))
        print(translate_to_romanic(x))
    except TypeError:  # check for exceptions (not integer)
        print('Nan')


def translate_to_romanic(x):
    rom_letters = {1: 'I',
                   5: 'V',
                   10: 'X',
                   50: 'L',
                   100: 'C',
                   500: 'D',
                   1000: 'M'}
    rom_answer = ''
    while x > 1000:
        x -= rom_letters.get('M')
        rom_answer += 'M'
    return rom_answer


if __name__ == "__main__":
    main()
