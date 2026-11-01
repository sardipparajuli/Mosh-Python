#Create a guessing game where the user gets three tries to guess a secret number.

secret_number = 8
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
  guess = int(input('Guess: '))
  guess_count += 1
  if guess == secret_number:
    print(f'You got it! The secret number was {secret_number}.')
    break  #the loop ends right here because of break
else:
  print('Sorry, You failed!')    