"""

MoneyBox class that can initialize the money box, set the capacity of it and add the coins into box.

"""


class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.num_of_coins = 0

    def can_add(self, v):
        if self.num_of_coins + v <= self.capacity:
            res = True
        else:
            res = False
        return res

    def add(self, v):
        if MoneyBox.can_add(self, v):
            self.num_of_coins += v
            return self.num_of_coins
        else:
            return print("Stack is over")