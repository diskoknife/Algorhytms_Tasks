# find nearest y that mod 5 equals 0
def closest_mod_5(x):
    y = 0
    while (y < x):
        y += 5
    print(y)
    return y


closest_mod_5(9)
