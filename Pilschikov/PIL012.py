"""

Recursion
We have logic operation on input
check if it right and calculate it

"""

logic = input("Enter logical operation \n").split()

def calculate(logic_):
    logic_ = True
    if logic[0] == 'True' or 'False':
        logic_ = logic[0]
    if logic == None:
        return print(logic_)
    logic.pop()
    calculate(logic_)