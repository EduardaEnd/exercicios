# solicitar 4 nomes e embaralhar as ordens
import random

no1 = input(' Digite o primeiro nome: ')
no2 = input(' Digite o segundo nome: ')
n03 = input(' Digite o terceiro nome: ')
no4 = input('Digite o quartio nome: ')
lista = [no4, n03, no2, no1]
random.shuffle(lista)
print(lista)