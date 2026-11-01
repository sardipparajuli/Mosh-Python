# Write a program to remove the duplicates in a list

numbers = [3, 8, 7, 6, 5, 4, 5, 5, 4, 2, 3]
unique = []
for number in numbers:
  if number not in unique:
    unique.append(number)
print(unique)