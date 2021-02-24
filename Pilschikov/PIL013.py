#  Copyright (c) 2021.
#  Vyacheslav Shchurov (diskoknife@gmail.com)
"""

Hanoi towers
we have three sticks and n of disks every next of them are smaller of previous
all of disks are on the left stick. Throw all of disks to the right stick and print all of actions

"""

num = int(input("Enter the num of disks "))

def reshuffle(height, fromStick, toStick, withStick):
    if height >= 1:
        reshuffle(height - 1, fromStick, withStick, toStick)
        moveDisk(fromStick, toStick)
        reshuffle(height - 1, withStick, toStick, fromStick)

def moveDisk(fp, tp):
    print("moving disk from", fp, "to", tp)

reshuffle(num, "Ä", "B", "C")