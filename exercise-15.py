#Create this "F" shape using nested loop:
# xxxxx
# xx
# xxxxx
# xx
# xx

numbers = [5, 2, 5, 2, 2]  #number of x in each line to create 'F' shape

for x_count in numbers:
  #print('x' * x_count) -->This works as well but the question asks us to use nested loop.
  output = ''
  for count in range(x_count):
    output = output + 'x'  #can also be written as output += 'x'
  print(output)  



  