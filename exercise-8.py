#If applicant has high income AND good credit they are eligible for loan , else they are not. In another case if applicant has high income OR good credit , they are eligible for loan.

#Case 1
has_high_income = True
has_good_credit = False

if has_high_income and has_good_credit:
  print('Eligible for loan')

else:
  print('Not Eligible for loan')
  

#Case 2
has_high_income = False
has_good_credit = True

if has_high_income or has_good_credit:
  print('Eligible for loan')
  
else:
  print('Not Eligible for loan')