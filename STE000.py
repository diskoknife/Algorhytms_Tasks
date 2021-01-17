import math


def arcctg(x):
    actg = math.pi / 2 - math.atan(x)
    return actg


def pred(year):
    x_1 = 172 / 45
    x_2 = (2000 - year) / 45
    popul = x_1 * arcctg(x_2)
    return popul


line = input()

years_str_list = line.split()

n = len(years_str_list)
for x in range(0, n):
    years_list = [int(x) for x in years_str_list]
    popul = pred(years_list[x])
    population_list = [popul for x in years_list]
    print(f"{years_list[x]:5d} - {population_list[x]:6.3f} миллиард(ов)")




