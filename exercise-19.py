# Emoji converter program which converts a user message involving :) to 😄 and :( to 😔

message = input('>')
words = message.split(' ')  # cuts the string at every space and returns a LIST of the pieces. The spaces themselves are removed, e.g. 'hi :) bye' becomes ['hi', ':)', 'bye']
emojis = {
  ':)': '😄',
  ':(': '😔'
}

output = ''
 
for word in words:
  output = output + emojis.get(word, word) + ' '

print (output)  