#  Copyright (c) 2021.
#  Vyacheslav Shchurov (diskoknife@gmail.com)

"""

*Put some description for this file here*

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CreateList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head

