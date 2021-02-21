"""

Task 8.31, page 45
type num of months, count of day in months and make dict{month:days}

"""

months = ('January', 'February', 'Marth', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December')
days = (28, 30, 31)
datedict = {months[0]:days[2],
            months[1]:days[0]}
for i in range(2,12):
    datedict.update({months[i]: days[2 if i%2 == 0 else 1]})

print(datedict)