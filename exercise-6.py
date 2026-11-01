#create 2 variables named first and last with first and last names of a person being John and Smith; and print the statement: John [Smith] is a coder. Remember [] is used for list and not strings so thats the challenge.

first = 'John'
last = 'Smith'

message = first + ' [' + last +'] is a coder.' #it can be done this way but a better way is to use formatted string aka f string.
print(message)

#better way to solve it using f-string :
message = f'{first} [{last}] is a coder.'
print (message)

print('John [Smith] is a coder')  #This will obviously work but its not what the question is asking us to do.