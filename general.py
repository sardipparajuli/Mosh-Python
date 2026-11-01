name = 'sardip'
age = 23
rating = 4.7
is_jobless = True
print(type(name), type(age), type(rating), type(is_jobless))

name = input('What is your name? ')
print('Hi', name)
course = 'Python for Beginners'
course = "Python's course for beginners"
print(course)
course = 'Python course for "Beginners"'
print(course)
course = '''Python's course for "Beginners"'''
print(course)
print(course[0], course[5], name[4], course[-1], course[-4])




print('Hi ' + name + ',' + '\nHere is our first email to you.\nThank you,\nThe support team')

fruit = 'watermelon'
print(fruit[0:4]) #actually prints from index 0 to 3
print(fruit[0:]) #prints from index 0 to end
print(fruit[3:]) #prints from index 3 to end
print(fruit[:7]) #prints from index 0 to 6
print(fruit[:]) #prints the whole string

another = fruit
print(another)


friend = 'Jennifer'
print(friend[1:-1]) #answer is ennife

first = 'John'
last = 'Smith'
#How to print John [Smith] is a coder? because [] represents list and not string.

message = first + ' [' + last +'] is a coder' #it can be done this way but a better way is to use formatted string aka f string.
print(message)

#better way to solve it using f-string :
message = f'{first} [{last}] is a coder'
print (message)

college = 'Trinity International College'
print(len(college))  #counts the length of characters or the no. of characters including spaces.

print(college.upper())  #converts the whole string to upper case.
print(college) #will still display the original string and doesn't display the upper cased string.

print(college.lower())  #converts the whole string to lower case.

print('sARdip'.title())  #converts it to Sardip , i.e capitalizes only the first letter.
course = 'pyTHon FoR bEginnErS'
print(course.title()) #capitalizes all first letters of each word of the string and makes all other letters lowercase.

print('  hello world  '.strip())   # converts it to "hello world" and trims the spaces on the edges. Spaces in the middle stay.

print(college.find('y'))  #returns the index of the character 'y' in the string.

print(college.find('x'))  #returns -1 since 'x' doesn't exist in the string.

print(college.find('College'))  #returns the index of 'C' in the string because thats where 'College' starts.

print(college.replace('International', 'National'))  #replaces International with National

print('International' in college)  #returns a boolean value : True or False after checking whether 'International' exists in variable 'college'


print(10 + 4)
print(10 / 2)
print(10 // 3)  #prints only integer without decimal values so this one prints only 3 instead of 3.333.....
print(10 % 3)  #prints remainder so 1 in this case.
print(10 ** 3) # ** is power so this is 10 power 3.
print(10 ^ 3) #it doesnt perform power , it performs XOR operation


x = 10 

x = x + 3 
x += 3 #same thing but shorter
print(x)

x = x - 3
x -= 3
print(x)

# #PEMDAS is the order of operations in math (and Python). It tells you which part of a math equation is calculated first.

# So the order is:

# Parentheses ( )

# Exponents ** (powers)

# Multiplication * and Division / (calculated left to right)

# Addition + and Subtraction - (calculated left to right)


y = 2.9
print(round(y))  #gives 3

y = -4.8
print(abs(y))  #always gives positive value so 4.8 


import math #allows usage of mathematical modules.
print(math.ceil(2.9))  #prints 3 and the thing is we could only use this function after we typed import math.
print(math.floor(4.7))  #prints 4


 
has_high_income = True
has_good_credit = False

if has_high_income and has_good_credit:  #and logical operator so both must be true for the message below to appear on the terminal.
  print('Eligible for loan')

else: 
  print('Not Eligible for loan')
  

temperature = 35

if temperature >= 30:
  print("It's a hot day")

elif temperature <= 15:
  print("It's a cold day")

else: 
  print("It's a lovely day")
  

age = 23
if age == 23:  #gotta use == , = doesnt work
  print('You are the same age as me')
elif age != 23:  # != means not equal to
  print('nah we not the same age')



i = 1
while i <= 5:
  print('*' * i)
  i = i + 1
print ('Done')

#car game practise

command = ''
started = False

while command != 'quit':
  command = input('>').lower().strip()
  
  if command == 'help':
    print('start - to start the car\nstop - to stop the car\nquit - to end the game')
    
  elif command == 'start':
    if started:
      print('The car is already running..🫩')
    else:  
      print('The car has started🚖🚖')
      started = True
      
  elif command == 'stop':
    if not started:
      print('The car has already been stopped..🫩') 
    else:
      print('The car has stopped🚫🚫') 
      started = False
      
  elif command == 'quit':
    print('Bye!')
    
  else:
    print('Invalid command , type help for commands list')  

       
for items in 'Sardip':
  print(items)
  
marks = [44, 57, 39, 27]
total = 0
for mark in marks:
  total = total + mark
print(f'Total Marks: {total}')  

for item in range(10):
  print(item)  #this will print from 0-9

for item in range(5, 10):
  print(item)  #this will print from 5-9 

for item in range(5, 10, 2):
  print(item)  #this will print 5 , 7 and 9 ...the 2 indicates difference of 2 between each numbers; from the range 5 to 10 in this case.
  
  
numbers = [5, 2, 5, 2, 2]

for x_count in numbers:
  output = ''
  for count in range(x_count):
    output += 'x'
    
  print(output)  
  
names = ['John', 'Bob', 'Mosh', 'Sardip', 'Anup']
print(names)
print(names[0])  #prints John
print(names[2:4])  #prints from Mosh to Sardip
names[4] = 'Ryan' #modifies the list by changing Anup to Ryan


matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
print(matrix[0]) #prints the first list [1, 2, 3]

print(matrix[0][0])  #prints 1

matrix[0][1] = 12  #modifies 2 to 12

matrix[0][1] = 2  #changing the value back to 2

for row in matrix:
  for item in row:
    print(item)  #prints 1-9
    
numbers = [5, 5, 1, 7, 4]
numbers.append(20) #adds 20 at the end of the list
print(numbers)
numbers.insert(0, 10)  #adds 10 to the 0th index without deleting the previous number in 0th index but pushing their positions. 
numbers.remove(5)  #removes only the first 5 in the list
numbers.clear()  #empties the list
numbers = [5, 5, 1, 7, 4]  #just resetting the list after clearing it
numbers.pop()  #removes the last item on the list
numbers.index(5) #when printed, shows the index where 5 first appeared in the list

# numbers.index(99) #when printed, gives error because 99 is not in the list .
 
print(99 in numbers)  # way to check existence of an item in a list. Displays boolean value so True or False. In this case, False
numbers.count(5)  #when printed, shows the number of times '5' appears in the list
numbers.sort()  #sorts the values in the list in ascending order
numbers.reverse()  #flips the current order of values in the list
numbers2 = numbers.copy() #numbers2 variable stores the copy of our original list in numbers variable. numbers.copy() copies the list as it is at that moment. 


numbers = (1, 2, 3)  #This is a tuple. Unlike lists, we cannot change a tuple 
numbers[0] # When printed, displays the item in the tuple at 0th index , so 1 in this case

#numbers[0] = 4 #When printed displays an error because tuples cannot be modified/changed

numbers.index(3) # Displays the index of number 3 in the tuple

coordinates = (1, 2, 3)
x, y, z = coordinates #this corresponds value x to 1 ( index 0), y to 2(index 1) and z to 3(index 2). We can use this with lists and anything else too. This is called unpacking


customer = {'name': 'Sardip Parajuli','age': 30, 'is_verified': True}  # This is a dictionary. It contains key-value pairs. So name is key and Sardip Parajuli is value, age is key and 30 is value and so on

customer['name']  #when printed displays the value associated with this key. So in this case, it displays Sardip Parajuli

#customer['birthdate']  #when printed displays an error (KeyError: 'birthdate') because this key doesn't exist in the dictionary

customer.get('birthdate')  #when printed displays None instead of an error.

customer.get('birthdate', 'Sep 14 2003') #this key-value pair doesn't exist in the original dictionary. When printed displays Sep 14 2003 but does NOT add/store the key-value pair in the original dictionary

customer['birthdate'] = 'Sep 14 2003' #adds this new key value pair to the dictionary unlike the above mentioned get method

customer['name'] = 'Jackie Chan'  #changes the value of the key 'name' from Sardip Parajuli to Jackie Chan


