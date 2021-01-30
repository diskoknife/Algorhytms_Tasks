"""

Create a simulation of namespaces
Requirements:
1. Creation of namespaces
2. Add variables into the namespace
3. Get variables from namespace like: get<namespace> <var>

"""

namesp = {}  # Init a dictionary to namespaces
command = str(input("enter your command"))
command_arr = command.split()


def get():  # get
    pass


def add():  # adding variable to the namespace like: add <namespace> <var>
    pass


def create():  # creating a namespace
    pass


if command_arr[0] == 'get':  # unfortunattely in Python we don't have switch statement so I use elif
    get()
elif command_arr[0] == 'add':
    add()
