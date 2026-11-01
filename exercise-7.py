#Price of a house is $1M. If buyer has good credit, they need to put down 10% otherwise they need to put down 20% . Print the down payment.

price = 1000000
good_credit = True  #just change it to true or false as u wish. The results in terminal will change accordingly.

if good_credit:
  down_payment = 0.1 * price

else: 
  down_payment = 0.2 * price
  
print(f'Down Payment: ${down_payment:,.2f}')    # , adds thousands separators and .2f means “2 decimal places, as a float.” So when True this  prints Down Payment: $100,000.00