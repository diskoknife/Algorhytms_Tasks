#  Copyright (c) 2021.
#  Vyacheslav Shchurov (diskoknife@gmail.com)
"""

Task5.8 page 23
fill array with rand values and find difference between max and min

"""
import random

x_list = [random.randrange(1, 100000) for i in range(1, 100)]
ans = max(x_list) - min(x_list)
print("This func used to fill array with rand nums and find difference "
      "between min and max elem\n"
      "Array:" + x_list +
      "difference between min and max is", ans)
