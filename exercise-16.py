# Program to find the largest number in a list.

numbers = [7,3,5,2,1,8,9,22,29,10,6,11]
max = numbers[0]  #initially assume the first number as max
for number in numbers:
  if number > max:
    max = number
print(max)    