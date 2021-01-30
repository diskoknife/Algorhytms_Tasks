"""

Create a simulation of namespaces
Requirements:
1. Creation of namespaces
2. Add variables into the namespace
3. Get variables from namespace like: get<namespace> <var>

"""

namespaces = {'global': None}  # dictionary. Key - namespace, value - parent
variables = {'global': set()}  # dictionary. Key - namespace, value - variable
str_iter = int(input())  # Number of strings to input


def add():
    variables[cmd[1]] = cmd[2]


def create():
    namespaces[cmd[1]] = cmd[2]


def get():
    print(variables[cmd[1]])


for i in range(str_iter):
    cmd = input().split(" ")
    if cmd[0] == 'get':  # Unfortunately Python didn't have switch statement so I use elif construction
        get()
    elif cmd[0] == 'add':
        add()
    elif cmd[0] == 'create':
        create()
    else:
        pass
