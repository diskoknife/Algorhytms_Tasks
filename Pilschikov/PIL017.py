"""

Task 8.31, page 45
type num of months, count of day in months and make dict{month:days}

"""

months = ('January', 'February', 'Marth', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December')
days = (28, 30, 31)
datedict = {months[0]:days[2],
            months[1]:days[0],
            months[2]:days[2],
            months[3]:days[1],
            months[4]:days[2],
            months[5]:days[1],
            months[6]:days[2],
            months[7]:days[2],
            months[8]:days[1],
            months[9]:days[2],
            months[10]:days[1],
            months[11]:days[2]}

print(datedict)