# Paste your code into this box
def balance_unpaid_scenario(balance, int_rate, minimum_):
    month = 0
    while(month < 12):
        min_payment = minimum_
        unpaid_balance = balance - min_payment
        interest_payment = unpaid_balance * int_rate / 12
        balance = unpaid_balance + interest_payment
        month += 1
    return balance

def find_monthly_min_payment(lower, upper, int_rate):
    middle = (upper - lower) / 2 + lower
    balance_unpaid_middle = balance_unpaid_scenario(balance, int_rate, middle)
    if balance_unpaid_middle < -10:
        upper = middle
        return find_monthly_min_payment(lower, upper, int_rate)
    elif balance_unpaid_middle > 10:
        lower = middle
        return find_monthly_min_payment(lower, upper, int_rate)
    else:
        return middle

def main(balance, annualInterestRate):
    import math
    lower = balance / 12
    upper = lower + lower * annualInterestRate
    answer = find_monthly_min_payment(lower, upper, annualInterestRate)
    print('Lowest payment: ', int(math.ceil(answer / 10.0)) * 10)


balance = 3329
annualInterestRate = 0.2
main(balance, annualInterestRate) # >> 310


balance = 4773
annualInterestRate = 0.2
main(balance, annualInterestRate) # >> 440



balance = 3926
annualInterestRate = 0.2
main(balance, annualInterestRate) # >> 360


