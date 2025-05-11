nome = input(' Qual o seu nome? ').title()
print(f' Prazer em te conhecer {nome:*^14}')

n1 = int(input(' Digite uma nota:'))
n2 = int(input(' Digite outra nota: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f' a soma é {s}, a multiplicação é {m}, a divisão é {d:.2f}', end='')
print(f' a divisão inteira é {di} e a expoenciação é {e:.2f}')
