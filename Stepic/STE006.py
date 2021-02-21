"""

Write a list with rand values. Print a num of uniq values

"""

objects = [1, 2, 1, 2, 3, True, "asf", 4, 1, 214, 125, 125, 2465]
ans = 0
uniq_obj = []

for obj in objects:
    if obj not in uniq_obj:  # not in is return True if this object is not in needed list
        uniq_obj.append(obj)

ans = len(uniq_obj)
print(ans)
