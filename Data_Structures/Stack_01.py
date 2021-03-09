#  Copyright (c) 2021.
#  Vyacheslav Shchurov (diskoknife@gmail.com)

"""

On the input we have string with n-num braces. If all of the braces are open
and closed print "Success" if braces are not-correct - print first-num of
non-closed brace

"""
def main():
    user_string = input("Enter the random string with braces:\n")
    if check_closed(user_string):
        check_brackets()
    else:
        print("Starts with closed braces at position ", i + 1)
# define checking options
open_braces = ['(', '[', '{']
close_braces = [')', ']', '}']
braces = open_braces+close_braces
brace_stack = []
num_brace = []

def check_closed(user_string):
    for i in range(len(user_string)):
        if user_string[i] in close_braces and brace_stack == []:
            return False
        if user_string[i] in braces:
            brace_stack.append(user_string[i])
            num_brace.append(i)
    return True

def check_brackets():
    reverse_stack = list(brace_stack.pop())
    if reverse_stack in close_braces:
        if brace_stack[-1] ==


print(brace_stack)

if __name__ == '__main__':
    main()