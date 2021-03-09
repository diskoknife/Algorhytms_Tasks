#  Copyright (c) 2021.
#  Vyacheslav Shchurov (diskoknife@gmail.com)

"""

On the input we have string with n-num braces. If all of the braces are open
and closed print "Success" if braces are not-correct - print first-num of
non-closed brace

"""
def main():
    user_string = input("Enter the random string with braces:\n")
    add_brackets_to_stack(user_string)


def add_brackets_to_stack(user_string, round_enum=0, quad_enum=0, figure_enum=0, position = [0, 0, 0]):
    for c in range(len(user_string)):
        if user_string[c] == '(':
            round_enum += 1
            position[0] = c
        if user_string[c] == '[':
            quad_enum += 1
            position[1] = c
        if user_string[c] == '{':
            figure_enum += 1
            position[2] = c
        if user_string[c] == ')':
            round_enum -= 1
            position[0] = 0
        if user_string[c] == ']':
            quad_enum -= 1
            position[0] = 0
        if user_string[c] == '}':
            figure_enum -= 1
            position[0] = 0
        if round_enum < 0 or quad_enum < 0 or figure_enum < 0:
            return print("First unopened bracket: ", user_string[c])
    if round_enum == quad_enum == figure_enum == 0:
        return print("Success")
    else:
        return print("First unclosed bracket: ", position)


if __name__ == '__main__':
    main()