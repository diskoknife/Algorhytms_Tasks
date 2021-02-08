"""

In first input line we put date in format: YYYY MM DD
In second input line we put value of days
Output: date after *days*

"""

from datetime import date, timedelta

idate = list(map(int, input().split()))  # split sequence and turn it to the int
days = int(input())

date = date(*idate)  # translate list into the date
days = timedelta(days)
res = date + days
print(res.year, res.month, res.day)
