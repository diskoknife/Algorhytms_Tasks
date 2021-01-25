# calculate estimate payment for loan
def compute_payment(sum, dur, perc, n):
    pay = sum / dur + (sum - (n - 1) * sum / dur) * (perc / 1200)
    return pay


s = int(input())  # sum of credit
n = int(input())  # credit duration
k = int(input())  # percentage of credit

if s <= 1 or n <= 1 or k <= 0:
    print("Unexpected loan values")
else:
    months_list = [range(1, n)]

    print("-" * 21)
    payment_list = [compute_payment(s, n, k, months_list[n]) for n in months_list]
    for i in range(len(months_list)):
        print("%2d month - %8.2f rub")
