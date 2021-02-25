#  Copyright (c) 2021.
#  Vyacheslav Shchurov (diskoknife@gmail.com)
"""

Print input num by romanic num
Task 7.17, page 37. Convert arabic numerals into romanians

"""


def main():
    try:
        x = int(input('Énter the arabic numeral'))
        print(translate_to_romanic(x))
    except TypeError:  # check for exceptions (not integer)
        print('Nan')


def translate_to_romanic(x):
    result = ''
    for arabic, roman in zip(
            (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
            ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', "IX", 'V', 'IV',
             'I')):
        result += x // arabic * roman
        x %= arabic
    return result


if __name__ == "__main__":
    main()
