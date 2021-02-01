"""

Create a simulation of namespaces
Requirements:
1. Creation of namespaces
2. Add variables into the namespace
3. Get variables from namespace like: get<namespace> <var>

"""

info = dict({'global': [None]})


def create(namespace, parent):
    info.update({namespace: [parent]})


def add(namespace, var):
    info[namespace].append(var)


def get(namespace, var):
    while namespace != None and var not in info[namespace][1:]:
        namespace = info[namespace][0]
    print(namespace)


operations = {'create': create, 'add': add, 'get': get}
for i in range(int(input())):
    inp = input().split()
    operations[inp[0]](inp[1], inp[2])
