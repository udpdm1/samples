'''
Based upon a given purchase amount, create an amortization schedule for payoff
'''
from os import system,name

interest_rate = .12

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
        

clear()

my_purchase = float(input("What is the purchase price of the item you wish to charge? "))

my_balance = my_purchase * .9 #90% of purchase price will be on cred
flat_payment = my_balance * .05 #5% of the original purchase amount will be constant payment until loan is paid off.

print(f'Amount due today is: {my_purchase * .10}')
i = 0
print("")
print("")
print("Month Starting Balance Interest to Pay Principal to Pay Payment Ending Balance")
while my_balance:
    i += 1
    interest = my_balance * (interest_rate / 12)
    monthly_principle = flat_payment - interest
    start_bal = my_balance
    if my_balance >= monthly_principle:
        my_balance -= monthly_principle
    else:
        #At this point our balance is lower than the 5% monthly principle.
        #We set monthly principle to remaining balance and adjust last payment to cover that plus interest.
        monthly_principle = my_balance
        flat_payment = monthly_principle + interest
        my_balance = 0

    print(f'{i:5}{start_bal:12.2f}{interest:15.2f}{monthly_principle:15.2f}{flat_payment:15.2f}{my_balance:12.2f}')

print("Thank you for shopping at the TidBit Computer Store. Please come again soon!")