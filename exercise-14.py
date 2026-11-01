# calculate the total prices of items in a shopping cart, with prices 10, 20 and 30. Use for loop.
prices = [10, 20, 30]
total = 0
for price in prices:
  total = total + price #can also be written as total += price
print(f'Total: {total}')  


for x in range(4):
  for y in range(3):
    print(f'({x}, {y})')

