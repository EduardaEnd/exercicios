n = input('digite algo: ')
print('O tipo primitivo desse valor é ', type(n),
      'É uma letra? ', n.isalpha(),
      '\n É um alfanumerico? ', n.isalnum(),
      '\n é um numero?', n.isdigit(),
      '\n pertencem ao conjunto ASCII? ', n.isascii())