# If user's name is less than three characters long , reply it must be atleast 3 characters , if the name is more than 50 characters long , reply name can be a maximum of 50 characters and no more, and otherwise reply name looks good!

name = input('Type your name: ')

if len(name) < 3:
  print('Name must be atleast 3 characters')
elif len(name) > 50:
  print('Name can be a maximum of 50 characters')
else:
  print('Name looks good!')
