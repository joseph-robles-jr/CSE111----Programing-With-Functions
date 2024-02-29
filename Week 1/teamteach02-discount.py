print('Hello!! Welcome to the Store Emporium Store! \nCustomers who shop on Tuesdays and Wednesdays get a discount!')

from datetime import datetime
sub = float(input('What is your subtotal? '))
#if day of week == 2 or 3, and the total is at least $50 , subtract 10%

#add sales tax of %6
#print discount amount if applicable, the sales tax amount, and the total amount due
now = datetime.now()
day = now.weekday()

if sub >= 50:
    if day == 2 or day == 3:
        total = .9 * sub
        print(f'Your subtotal after the discount is {total}')
        discount = sub * .1
        print(f'Your discount is ${discount:.2f}.')
        
tax = sub * .06
total = tax + sub
print(f'Your tax is ${tax:.2f}')
print(f'Your total is ${total:.2f}')
