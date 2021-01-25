# task 7.1 page 33
# actually in task (and in paragraph at all) I must define new object-classes
season = ('winter', 'spring', 'summer', 'fall')  # make tuple cuz we have fixed num of seasons in the year
temp = ('cold', 'warm')  # here we use tuple to interpretate pascal

x = season[1]
y = x
t = temp[1]
# next 2 questions is unexpected tokens... So
try:
    t = temp['hot']
except:
    print('únavaiable value')
print(x, y, t)

ex_7_1_b = [season[1] < season[2], season[0] <= season[2]]
print(ex_7_1_b)
