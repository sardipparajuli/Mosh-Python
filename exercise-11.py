#Ask the weight of the user , then ask whether that weight is in kilos and pounds and then return them with their weight in different unit to what they entered. So if user puts their weight in kg, terminal must return them their weight in lbs and vice versa.


weight = float(input('Weight: '))
unit = input('(L)bs or (K)g: ').strip().upper()
#strip function trims the edge spaces if user puts it, so there is no error when user puts ' l' for eg. and upper function allows usage of both lower and capital L and K.

if unit == 'L':
  print(f'You are {weight * 0.45:.2f} kg')
elif unit == 'K':
  print(f'You are {weight * 2.2:.2f} lbs')
else: 
  print('Invalid input. Type either L or K.')
 
 