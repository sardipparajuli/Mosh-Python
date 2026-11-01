# create identifiers with different datatypes and find the datatypes they are.

#Type 1: Basic ones-->(single values)
name = 'sardip' #string-->(holds text)
age = 23  #integer-->(holds whole number)
height = 5.7  #float-->(holds decimal numbers)
is_jobless = True  #boolean-->(holds yes/no)
profile_picture = None  #NoneType-->(holds none value)

#Type 2: The collections(many values in one box)
fruits = ["apple", "banana", "mango"]  #list-->(holds ordered collections, you can change it)
animals = ("dog", "cat", "elephant")  #tuple-->(holds ordered collections, locked/can't change)
details = {"name": "Sardip", "age": 22}  #dictionary-->(label->value pairs, like a real dictionary)
numbers = {1, 2, 3}  #set-->(no duplicates, no order)


print(type(name), type(age), type(height), type(is_jobless), type(profile_picture), type(fruits), type(animals), type(details), type(numbers))
