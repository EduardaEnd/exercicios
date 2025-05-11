#peça e calcule o valor do cateto adjacente e cateto oposto de um triangulo retangulo

oposto = float(input('comprimento do cateto oposto: '))
adjacente = float(input(' comprimento do cateto adjacente: '))

#calculo
hipo = (oposto ** 2 + adjacente ** 2) ** (1/2)

print(f' a hipotenusa vai medir {hipo:.2f}')