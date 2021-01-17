# Task5.8 page 23
import random

x_list = [random.randrange(1, 100000) for i in range(1, 100)]
ans = max(x_list) - min(x_list)
print("difference between min and max is", ans)
