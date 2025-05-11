# escolher um nome sorteado
import random

no1 = input('Digite o primeiro nome: ')
no2 = input(' Digite o segundo nome: ')
no3 = input(' Digite o terceiro nome: ')
no4 = input(' Digite o quarto nome: ')
lista = [no1, no2,no3, no4]
escolha = random.choice(lista)
print(f'o nome escolhido foi {escolha}')