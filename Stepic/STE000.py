"""

Calculate predicted population on Earth by year.
Using predicting formula of S.Kapitsa:
N(t) = C/tau * arcctg((T1-t)/tau)
where C = 172*10^9
T1 - 2000 yr
t = 45 yr
t - prediction yr

"""
import math


def arcctg(x):  # Math module isn't have an arcctg func so realise it here
    actg = math.pi / 2 - math.atan(x)
    return actg


def pred(year):
    x_1 = 172 / 45
    x_2 = (2000 - year) / 45
    popul = x_1 * arcctg(x_2)
    return popul


line = input("Input year to predict population: ")

years_str_list = line.split()

n = len(years_str_list)
for x in range(0, n):
    years_list = [int(x) for x in years_str_list]
    popul = pred(years_list[x])
    population_list = [popul for x in years_list]
    print(f"{years_list[x]:5d} - {population_list[x]:6.3f} billions")
