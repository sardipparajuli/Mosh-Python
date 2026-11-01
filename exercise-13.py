#Create a car game where the user types help to get a list of commands, start to start the car, stop to stop the car, and quit to exit.

command = ''
started = False

while command != 'quit':
  command = input('>').lower().strip()
  if command == 'help':
    print('start - to start the car\nstop - to stop the car\nquit - to exit')
    
    
  elif command == 'start':
    if started:
      print('The car is already started!!')
    else:
      print('The car has started...Ready to go!')
      started = True  
      
    
    
  elif command == 'stop':
    if not started:
      print('The car is already stopped!')
    else:
      print('The car has stopped...')
      started = False 
    
  elif command == 'quit':
    print('Bye!')
    
  else:
    print('Invalid command, type help for list of commands!')