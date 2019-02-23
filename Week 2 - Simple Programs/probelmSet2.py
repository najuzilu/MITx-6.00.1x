# Paste your code into this box
'''def main(balance, int_rate, min_rate):
    month = 0
    while(month < 12):
        min_payment = balance * min_rate
        unpaid_balance = balance - min_payment
        interest_payment = unpaid_balance * int_rate / 12
        balance = unpaid_balance + interest_payment
        month += 1
    print('Remaining balance: {:.2f}'.format(balance))

# Test Case 1
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
main(balance, annualInterestRate, monthlyPaymentRate)

# Test Case 2
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
main(balance, annualInterestRate, monthlyPaymentRate)'''

#Actually submited:
# Paste your code into this box
def main(balance, int_rate, min_rate):
    month = 0
    while(month < 12):
        min_payment = balance * min_rate
        unpaid_balance = balance - min_payment
        interest_payment = unpaid_balance * int_rate / 12
        balance = unpaid_balance + interest_payment
        month += 1
    print('Remaining balance: {:.2f}'.format(balance))

main(balance, annualInterestRate, monthlyPaymentRate)



