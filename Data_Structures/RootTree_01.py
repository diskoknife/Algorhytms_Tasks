#  Copyright (c) 2021.
#  Vyacheslav Shchurov (diskoknife@gmail.com)

"""

Calculate the height of tree.
Input: Binary tree with the tops (0...n-1), preset as sequential (parent[0]...
...parent[n-1]) where parent[i] - parent of 'i' top.
Output: Height of tree
(Additional) Input:
    First string - size of tree
    Second string - sequence of $size integer values in range(parent[0]...
    ...parent[n-1]).
    For every 0<=i<=n-1 - parent[i] is parent of 'i' top. If parent[i] = -1 ->
    i is the root of tree.

"""
"""

e.g.:
input:                  
7
1 3 4 6 -1 1 2                  
    
    4
    |
    2
    |
    6
    |
    3
    |
    1
   / \
  0   5
  
Output: 6

"""


# This class uses only for fill tree. in input parents func we fill list with
# next values: parents[i]: parent. Also there must be a '-1' value
# to init the root
class Data:
    @staticmethod
    def set_size():
        size = int(input())
        return size

    @staticmethod
    def input_parents(size: int):
        parents = []
        for i in range(size):
            parents.append(int(input()))
        return parents


class Tree:
    # size = size of tree (max elem=size-1)
    # Left and Right params is no needed by task description, but we can use
    # it in the other tasks. Like a Find a nearest way etc.
    def __init__(self, size=None,root=None,
                 parents=None, ends=[]):
        self.ends = ends
        self.parents = parents
        self.root = root
        self.size = size

    # '-1' is the value for root by description. Actually, we can use more
    # softly dependencies
    def find_root(self, parents):
        for i in range(len(parents)):
            if parents[i] == -1:
                self.root = i
                return self.root
        raise NoRootException()

    # I don't know what is better: recursive function or iterable.
    # But iterable is more safety
    def find_ends(self, parents):
        for i in range(len(parents)):
            if i not in parents:
                self.ends.append(i)
        return self.ends

    # Iterate tree from bot to top. By every of ends
    def find_route(self, i, height=1):
        parent = self.parents[i]
        while parent != -1:
            parent = self.parents[parent]
            height += 1
        return height

    # height
    def calculate_height(self):
        heights = []
        for i in range(len(self.ends)):
            heights.append(self.find_route(self.ends[i]))
        return max(heights)


# If our tree has no roots there is no sense to continue our program
class NoRootException(Exception):
    pass


hello_message = "Please print in first string num of tree elems. " \
                "Every next string set parent to i element " \
                "(i = current string from 0 to num-1)." \
                " Please mark the root of tree by '-1' " \
                "value.\n "


def main():
    print(hello_message)
    size = Data.set_size()
    parents = Data.input_parents(size)
    tree = Tree(size=size, parents=parents)

    try:
        print("The root of tree is: ", tree.find_root(parents))
        print("Ends of the tree: ", tree.find_ends(parents))
        print("Height of tree: ", tree.calculate_height())
    except NoRootException:
        print("No root exception")


if __name__ == '__main__':
    main()
