"""

Create a simulation of namespaces
Requirements:
1. Creation of namespaces
2. Add variables into the namespace
3. Get variables from namespace like: get<namespace> <var>

"""

namespaces = {'global': None}  # dictionary. Key - namespace, value - parent
variables = {'global': set()}  # dictionary. Key - namespace, value - variable

cmd = input().split(" ")

def add():
    variables[cmd[1]] = cmd[2]

def create():
    namespaces[cmd[1]] = cmd[2]

def get():


if cmd[0] == 'get':
    get()
elif cmd [0] == 'add':
    add()
elif cmd [0] == 'create':
    create()
else:
    pass

print(cmd)
print(namespaces)
print(variables)