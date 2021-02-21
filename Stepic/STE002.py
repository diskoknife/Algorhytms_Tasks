"""

Calculate estimate payment and profit of the bank

"""

def compute_payment(s, n, k, t):
    pay = s / n + (s - (t - 1) * (s / n)) * (k / 1200)
    return pay


s = int(input())
n = int(input())
k = int(input())
month_payment = [compute_payment(s, n, k, i) for i in range(1, n + 1)]
if n <= 0 or s <= 0 or k <= 0:
    print("error")

else:
    for i in range(len(month_payment)):
        print("%2d месяц - %8.2f руб" % (i + 1, month_payment[i]))
    bank_profit = sum(month_payment) - s
    print("Доход банка - %6.2f руб" % (bank_profit))
