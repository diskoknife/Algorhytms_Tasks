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

class BinaryTree:
    def set_size(self):
        size = int(input())
        return size

    def input_parents(self, size):
        parents = []
        for i in range(size):
            parents.append(int(input()))
        return parents

    def calculate_height(self, parents, size):
