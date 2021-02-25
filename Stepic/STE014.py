"""

Write a PositiveList class which inherit from list class and can append only positive nums
Also write a NonPositiveException which throwing when you try  to add non positive num to list

"""


class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, x):
        if x > 0:
            super(PositiveList, self).append(x)
        else:
            raise NonPositiveError
