#  Copyright (c) 2021.
#  Vyacheslav Shchurov (diskoknife@gmail.com)

"""

On the input we have string with n-num braces. If all of the braces are open
and closed print "Success" if braces are not-correct - print first-num of
non-closed brace

"""


def main():
    user_string = input("Enter the random string with braces:\n")
    print(add_brackets_to_stack(user_string))



brackets = {
    '(': ')',
    '[': ']',
    '{': '}'
}


def add_brackets_to_stack(user_string, stack=[]):
    for c in user_string:
        if c in brackets.keys():
            stack.append(c)
        try:
            if c in brackets.values():
                brace = stack.pop()  # we can del last elem in the stack right now. cuz right now we check it
                if c != brackets.get(brace):
                    return c
        except IndexError:
            return 'Case closed even not started'
    return "Success"


if __name__ == '__main__':
    main()
